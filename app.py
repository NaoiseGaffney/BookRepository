import logging  # Enable logging of application events (info, warning, error)
from logging.handlers import RotatingFileHandler
import os
from flask import Flask, render_template_string, render_template, redirect, url_for, request, flash, session
from flask_mongoengine import MongoEngine, MongoEngineSession, MongoEngineSessionInterface
from flask_user import login_required, UserManager, UserMixin, current_user, roles_required
from flask_login import logout_user
import datetime
from  datetime import timedelta
import requests
from flask_debugtoolbar import DebugToolbarExtension

from config import ConfigClass

from dotenv import load_dotenv
from pathlib import Path
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

""" Flask application factory """



# Setup Flask and load app.config
app = Flask(__name__, static_folder="static", template_folder="templates")
# app.config.from_object(ConfigClass)
app.config.from_object(__name__+".ConfigClass")
# app.debug = True


""" # Initialise rotating file logging - set after app initialisation
logging.basicConfig(
    handlers=[RotatingFileHandler("./logs/book_repository.log", maxBytes=100000, backupCount=10)],
    level=os.environ.get("LOGGING_LEVEL"),
    format="%(name)s - %(levelname)s - %(message)s"
    )
 """
# Initialize logging - set after app initialisation
app.logger.setLevel(logging.INFO)

# Setup Flask-MongoEngine
db = MongoEngine(app)

# Use Flask Sessions with Mongoengine
app.session_interface = MongoEngineSessionInterface(db)

# Initiate the Flask Debug Toolbar Extension
toolbar = DebugToolbarExtension(app)


class User(db.Document, UserMixin):
    # Active set to True to allow login of user
    active = db.BooleanField(default=True)

    # User authentication information
    username = db.StringField(default="")
    password = db.StringField()

    # User information
    first_name = db.StringField(default="")
    last_name = db.StringField(default="")
    email = db.StringField(default="")
    email_confirmed_at = db.DateTimeField()
    # Required for the e-mail confirmation, and subsequent login.

    # Relationships  (Roles: user or user and Admin)
    roles = db.ListField(db.StringField(), default=["user"])

    meta = {
        "auto_create_index": True,
        "index_background": True,
        "indexes": ["username"]
    }


class Book(db.Document):
    title = db.StringField(default="", maxlength=250)
    author = db.StringField(default="", maxlength=250)
    year = db.IntField(maxlength=4)
    ISBN = db.IntField(maxlength=13)
    short_description = db.StringField(default="", maxlength=2000)
    user = db.StringField(required=True)
    creation_date = db.DateTimeField(default=datetime.datetime.now)
    comments = db.StringField(default="", maxlength=3500)
    rating = db.IntField(choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    genre = db.StringField(default="")
    private_view = db.StringField(default="off")
    book_thumbnail = db.StringField(default="")

    meta = {
        "auto_create_index": True,
        "index_background": True,
        "indexes": ["title"],
        "ordering": ["title"]
    }


class Genre(db.Document):
    genre = db.StringField(default="")
    icon = db.StringField(default="")
    description = db.StringField(default="")

    meta = {
        "auto_create_index": True,
        "index_background": True,
        "indexes": ["genre"],
        "ordering": ["genre"]
    }


# Setup Flask-User and specify the User data-model
user_manager = UserManager(app, db, User)


# Create admin user as first/default user, if admin does not exist.
# Password is set using an environment variable.
if not User.objects.filter(User.username == "admin"):
    app.logger.info(
        "Admin user is created on application startup if user does not exist.")
    user = User(
        username="admin",
        first_name="Administrator",
        last_name="Administrator",
        email=os.environ.get("MAIL_DEFAULT_SENDER"),
        email_confirmed_at=datetime.datetime.utcnow(),
        password=user_manager.hash_password(os.environ.get("ADMIN_PASSWORD"))
    )
    user.roles.append("Admin")
    user.save()


@app.route("/")
def home_page():
    # Landing/Home Page, accessible before signing/logging in.
    if current_user.is_authenticated:
        return redirect(url_for("member_page"))
    return render_template("index.html")


# The Members page is only accessible to authenticated users via the
# @login_required decorator


@app.route("/members")
@app.route("/members/<int:page>")
@login_required
def member_page(page=1):
    # The "R" in CRUD, a virtual library or stack of books to browse.
    app.logger.info(f"{current_user.username} is accessing the Member's Page (members.html). Endpoint: member_page.")
    
    books_pagination = Book.objects.filter(user=current_user.username).paginate(page=page, per_page=7)
    return render_template("members.html", books_pagination=books_pagination, page_prev=(page - 1), page_next=(page + 1))


@app.route("/add_book")
@login_required
def add_book():
    # Preparing for the "C" in CRUD, filling in the add book form.
    app.logger.info(f"{current_user.username} is adding a book (add_book.html) by filling out the add book form. Endpoint: add_book.")
    genre = Genre.objects()
    return render_template("add_book.html", genre=genre)


@app.route("/save_book", methods=["POST"])
@login_required
def save_book():
    # The "C" in CRUD, save the filled in add book form.
    book = Book(
        title=request.form.get("title"),
        author=request.form.get("author"),
        year=request.form.get("year"),
        ISBN=request.form.get("isbn"),
        user=current_user.username,
        short_description=request.form.get("short_description"),
        comments=request.form.get("comments"),
        rating=request.form.get("rating"),
        genre=request.form.get("genre"),
        private_view=request.form.get("private_view")
    )

    payload = {}
    isbn_key = f"isbn:{book.ISBN}"
    payload["q"] = isbn_key
    payload["key"] = os.environ.get("GOOGLE_API_KEY")
    print(payload)

    try:
        book_request = requests.get("https://www.googleapis.com/books/v1/volumes", params=payload, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
        book_thumbnail_w_http = book_request.json()["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
        book_thumbnail_w_https = book_thumbnail_w_http.replace("http://", "https://")
        book.book_thumbnail = book_thumbnail_w_https
        app.logger.info(f"{current_user.username} has successfully requested the thumbnail image {book.book_thumbnail} for the book {book.title} with the id {book.id} (add_book.html). Endpoint: save_book.")
        print(book_request.json()["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"])
    except BaseException:
        book.book_thumbnail = "/static/images/BR_logo_no_thumbnail.png"
        app.logger.warning(f"{current_user.username} has not successfully requested the thumbnail image for the book {book.title} with the id {book.id} (add_book.html). Endpoint: save_book.")

    try:
        book.save()
        flash(f"The book {book.title} was saved!", "success")
        app.logger.info(f"{current_user.username} is saving the book {book.title} with the id {book.id} (add_book.html). Endpoint: save_book.")
    except BaseException:
        app.logger.warning(f"{current_user.username} did not succeed in saving the {book.title} (add_book.html). Endpoint: save_book.")
        flash(f"The book {book.title} was NOT saved!", "danger")
    return redirect(url_for("member_page"))


@app.route("/edit_book/<book_id>")
@login_required
def edit_book(book_id):
    # Preparing for the "U" in CRUD, updating the book form fields.
    book = Book.objects.get(id=book_id)
    genre = Genre.objects()
    app.logger.info(f"{current_user.username} is updating the book {book.title} with the id {book.id} (edit_book.html). Endpoint: edit_book.")
    return render_template("edit_book.html", book=book, genre=genre)


@app.route("/update_book/<book_id>", methods=["POST"])
@login_required
def update_book(book_id):
    # The "U" in CRUD, saving the changes made to the update book form fields.
    book = Book.objects.get(id=book_id)
    fields = {
        "title": request.form.get("title"),
        "author": request.form.get("author"),
        "year": request.form.get("year"),
        "ISBN": request.form.get("isbn"),
        "short_description": request.form.get("short_description"),
        "comments": request.form.get("comments"),
        "rating": request.form.get("rating"),
        "genre": request.form.get("genre"),
        "private_view": request.form.get("private_view")
    }

    if fields["private_view"] != "on":
        fields["private_view"] = "off"


    payload = {}
    isbn_field = fields["ISBN"]
    isbn_key = f"isbn:{isbn_field}"
    payload["q"] = isbn_key
    payload["key"] = os.environ.get("GOOGLE_API_KEY")
    print(payload)

    try:
        book_request = requests.get("https://www.googleapis.com/books/v1/volumes", params=payload, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
        book_thumbnail_w_http = book_request.json()["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
        book_thumbnail_w_https = book_thumbnail_w_http.replace("http://", "https://")
        fields["book_thumbnail"] = book_thumbnail_w_https
        app.logger.info(f"{current_user.username} has successfully requested the thumbnail image {book.book_thumbnail} for the book {book.title} with the id {book.id} (add_book.html). Endpoint: save_book.")
        print(book_request.json()["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"])
    except BaseException:
        fields["book_thumbnail"] = "/static/images/BR_logo_no_thumbnail.png"
        app.logger.warning(f"{current_user.username} has not successfully requested the thumbnail image for the book {book.title} with the id {book.id} (add_book.html). Endpoint: save_book.")

    try:
        book.update(**fields)
        flash(f"The book {book.title} is updated!", "success")
        app.logger.info(f"{current_user.username} updated the book {book.title} with the id {book.id} (edit_book.html). Endpoint: update_book.")
    except BaseException:
        app.logger.warning(f"{current_user.username} did not update the book {book.title} with the id {book.id} (edit_book.html). Endpoint: update_book.")
        flash(f"The book {book.title} was NOT updated!", "danger")
    return redirect(url_for("member_page"))


@app.route("/delete_book/<book_id>")
@login_required
def delete_book(book_id):
    # The "D" in CRUD, deleting the book based on 'id' after delete modal
    # confirmation.
    book = Book.objects.get(id=book_id)
    try:
        book.delete()
        flash(f"The book {book.title} is deleted!", "success")
        app.logger.info(f"{current_user.username} deleted the book {book.title} with the id {book.id} (members.html). Endpoint: delete_book.")
    except BaseException:
        flash(f"The book {book.title} was NOT deleted!", "danger")
        app.logger.warning(f"{current_user.username} did not delete the book {book.title} with the id {book.id} (members.html). Endpoint: delete_book.")
    return redirect(url_for("member_page"))


@app.route("/search_book")
@login_required
def search_book():
    # Preparing for the book search in Book Repository, filling in the search
    # book form.
    genre = Genre.objects()
    app.logger.info(f"{current_user.username} is filling out the book search form. (search_book.html). Endpoint: search_book.")
    return render_template("search_book.html", genre=genre)


@app.route("/save_search", methods=["GET", "POST"])
@login_required
def save_search():
    # Save the search book results in a session cookie, to use by
    # 'search_results' repeatedly to display the paginated search results.
    fields = {
        "title": request.form.get("title"),
        "author": request.form.get("author"),
        "year": request.form.get("year"),
        "ISBN": request.form.get("isbn"),
        "short_description": request.form.get("short_description"),
        "comments": request.form.get("comments"),
        "rating": request.form.get("rating"),
        "genre": request.form.get("genre"),
        "private_view": request.form.get("private_view")
    }
    session["fields"] = fields
    # {'title': '', 'author': '', 'year': None, 'ISBN': '', 'short_description': None, 'comments': None, 'rating': '', 'genre': None, 'private_view': None}

    app.logger.info(f"{current_user.username} is searching (saving search in session cookie) for books matching {fields} (search_results.html). Endpoint: save_search.")

    return redirect(url_for("search_results"))


@app.route("/administration", methods=["GET", "POST"])
@roles_required("Admin")
def administration():

    return render_template_string("Administration Page")


@app.route("/search_results", methods=["GET", "POST"])
@app.route("/search_results/<int:page>")
@login_required
def search_results(page=1):
    # Book search using a combination of form fields saved in the session
    # cookie in 'save_search', and based on the values in some key fields
    # decide which Book Repository BaseQuerySet to run.
    fields = session.get("fields")

    form_title = fields["title"]
    form_author = fields["author"]
    try:
        form_isbn = int(fields["ISBN"])
    except ValueError:
        form_isbn = 0
    except TypeError:
        form_isbn = 0
    try:
        form_rating = int(fields["rating"])
    except ValueError:
        form_rating = 1
    except TypeError:
        form_rating = 0
    form_genre = fields["genre"]
    form_private_view = fields["private_view"]

    # Query Book Repository based on the search form data
    # Private Search "form_private_view == "on"
    if form_private_view == "on":
        if form_isbn:
            book_query_results = Book.objects.filter(user=current_user.username, ISBN=form_isbn).paginate(page=page, per_page=7)
            app.logger.info(f"{current_user.username} found books matching {book_query_results} - 1: Private & ISBN Search (search_results.html). Endpoint: search_results.")
            return render_template("search_results.html", book_query_results=book_query_results, page_prev=(page - 1), page_next=(page + 1))
        elif form_genre is None:
            book_query_results = Book.objects.filter(user=current_user.username, title__icontains=form_title, author__icontains=form_author, rating__gte=form_rating).order_by("+title", "+author", "-rating").paginate(page=page, per_page=7)
            app.logger.info(f"{current_user.username} found books matching {book_query_results} - 2: Private, no Genre, no ISBN, Title, Author, and Rating Search (search_results.html). Endpoint: search_results.")
            return render_template("search_results.html", book_query_results=book_query_results, page_prev=(page - 1), page_next=(page + 1))
        else:
            book_query_results = Book.objects.filter(user=current_user.username, title__icontains=form_title, author__icontains=form_author, rating__gte=form_rating, genre=form_genre).order_by("+title", "+author", "-rating").paginate(page=page, per_page=7)
            app.logger.info(f"{current_user.username} found books matching {book_query_results} - 3: Private, no ISBN, Title, Author, Rating, and Genre Search (search_results.html). Endpoint: search_results.")
            return render_template("search_results.html", book_query_results=book_query_results, page_prev=(page - 1), page_next=(page + 1))
    # Public Search "form_private_view == None"
    else:
        if form_isbn:
            book_query_results = Book.objects.filter(ISBN=form_isbn, private_view="off").paginate(page=page, per_page=7)
            app.logger.info(f"{current_user.username} found books matching {book_query_results} - 4: Public & ISBN Search (search_results.html). Endpoint: search_results.")
            return render_template("search_results.html", book_query_results=book_query_results, page_prev=(page - 1), page_next=(page + 1))
        elif form_genre is None:
            book_query_results = Book.objects.filter(title__icontains=form_title, author__icontains=form_author, rating__gte=form_rating, private_view="off").order_by("+title", "+author", "-rating").paginate(page=page, per_page=7)
            app.logger.info(f"{current_user.username} found books matching {book_query_results} - 5: Public, no Genre, no ISBN, Title, Author, and Rating Search (search_results.html). Endpoint: search_results.")
            return render_template("search_results.html", book_query_results=book_query_results, page_prev=(page - 1), page_next=(page + 1))
        else:
            book_query_results = Book.objects.filter(title__icontains=form_title, author__icontains=form_author, rating__gte=form_rating, genre=form_genre, private_view="off").order_by("+title", "+author", "-rating").paginate(page=page, per_page=7)
            app.logger.info(f"{current_user.username} found books matching {book_query_results} - 6: Public, no ISBN, Title, Author, Rating, and Genre Search (search_results.html). Endpoint: search_results.")
            return render_template("search_results.html", book_query_results=book_query_results, page_prev=(page - 1), page_next=(page + 1))


@app.route("/delete_user.html")
@login_required
def delete_user():
    deleted_user = current_user.username
    find_user_books = Book.objects.filter(user=current_user.username)
    for book in find_user_books:
        print("\n\nBook:", book.to_json())
    find_user = User.objects.filter(username=current_user.username)
    print("\n\nUser:", find_user.to_json())
    print(deleted_user)

    try:
        logout_user()
        find_user_books.delete()
        find_user.delete()
        flash(f"We're sad to see you go {deleted_user}!", "success")
        app.logger.warning(f"{deleted_user} is has left the Book Repository (delete_user.html). Endpoint: delete_user.")
    except:
        flash(f"Your account is still alive and active {find_user.username}!", "danger")
        app.logger.warning(f"{deleted_user} is still alive and active on the Book Repository (delete_user.html). Endpoint: delete_user.")

    return redirect(url_for("home_page"))


@app.route("/admin_dashboard.html")
@app.route("/admin_dashboard.html/<int:page>")
@roles_required("Admin")
def admin_dashboard(page=1):
    user_details_query = User.objects().order_by("username").paginate(page=page, per_page=10)
    genre_list = Genre.objects()
    # app_db_log = Log.objects()
    return render_template("admin_dashboard.html", user_details_query=user_details_query, page_prev=(page - 1), page_next=(page + 1))


@app.route("/update_user.html/<user_id>", methods=["POST"])
@roles_required("Admin")
def update_user(user_id):
    # The "U" in CRUD, saving the changes made to the update user modal form fields.
    print(user_id)
    user = User.objects.get(id=user_id)
    user_form_name = user.username
    admin_user_form = {
        "active": request.form.get(f"active_{user_form_name}"),
        "email": request.form.get(f"email_{user_form_name}"),
        "first_name": request.form.get(f"first_name_{user_form_name}"),
        "last_name": request.form.get(f"last_name_{user_form_name}")
    }

    print("Active:", admin_user_form["active"])
    print("Email:", admin_user_form["email"])
    print("first_name:", admin_user_form["first_name"])
    print("last_name:", admin_user_form["last_name"])

    if user.username == "admin":
        admin_user_form["active"] = True
    elif admin_user_form["active"] == "on":
        admin_user_form["active"] = True
    else:
        admin_user_form["active"] = False

    print(user.username)
    print(admin_user_form["active"])
    print(admin_user_form)
    user.update(**admin_user_form)
    
    return redirect(url_for("admin_dashboard"))


@app.route("/admin_delete_user/<user_id>", methods=["GET"])
@roles_required("Admin")
def admin_delete_user(user_id):
    # The "D" in CRUD, deleting the user based on 'id' after delete modal
    # with NO confirmation.
    user = User.objects.get(id=user_id)
    user_books = Book.objects.filter(user=user.username)
    print(user_books.to_json())
    if user.username != "admin":
        deleted_username = user.username
        try:
            user_books.delete()
            user.delete()
            flash(f"The user {deleted_username} is deleted!", "success")
            app.logger.info(f"{current_user.username} deleted the user {deleted_username} (admin_dashboard.html). Endpoint: admin_delete_user.")
        except BaseException:
            flash(f"The user {deleted_username} was NOT deleted!", "danger")
            app.logger.warning(f"{current_user.username} did not delete the user {deleted_username} (admin_dashboard.html). Endpoint: admin_delete_user.")
    return redirect(url_for("admin_dashboard"))


@app.route("/load_genres")
@roles_required("Admin")
def load_genres():
    # Create the Genre Collection if it does not exist. Taken from
    # https://bookriot.com/guide-to-book-genres/
    if not Genre.objects():
        app.logger.info("Genre Collection is created by admin.")
        genre_array = [
            {"genre": "(F) Classic", "icon": "", "description": "A book or author that’s stood the test of time and has continued to inspire meaningful discussion and thought across generations. As gruesome as it sounds, I argue that the author needs to be dead for a book of theirs to be considered a classic."},
            {"genre": "(F) Literary", "icon": "", "description": "Books deemed as having artistic qualities. Often subtle in theme and contain some kind of social/political/personal commentary on what it means to be human. Can contain other genre elements, but the author uses those elements not to be parts of that community, but to highlight an important theme in their work."},
            {"genre": "(F) General", "icon": "", "description": "These books offer fun, engaging stories in a contemporary setting. They’re more approachable than Literary Fiction, and contain none of the genre elements in other categories."},
            {"genre": "(F) Historical", "icon": "",
                "description": "Books that take place at least 30 years before the time the author writes them. Subcategories are often broken up by time frames."},
            {"genre": "(F) Romance", "icon": "",
                "description": "A book where the primary plot involves falling in love (of the romantic variety) and has a happy or emotionally satisfying ending."},
            {"genre": "(F) Mystery", "icon": "",
                "description": "Novels where the plot revolves around solving why something has happened or will happen."},
            {"genre": "(F) Action", "icon": "",
                "description": "High-stake novels with frequent scene changes, where the protagonist is constantly being put at risk."},
            {"genre": "(F) Fantasy", "icon": "",
                "description": "Novels set in either a completely fictional world, or set in a version of this world that includes magic."},
            {"genre": "(F) Sci-Fi", "icon": "",
                "description": "Books that imagine a current possibility’s impact in the future."},
            {"genre": "(F) Horror", "icon": "",
                "description": "A novel where supernatural elements create fear and terror, both within the novel and for the reader."},
            {"genre": "(NF) History", "icon": "", "description": "Books which examine past true events. These can be broad surveys of a specific country, region, and/or time period, or they can focus on a specific event or set of events. They’re often heavily researched and can utilize academic language or be highly narrative."},
            {"genre": "(NF) Biography", "icon": "",
                "description": "Relates the story of a person’s life."},
            {"genre": "(NF) Fine Arts", "icon": "",
                "description": "Books where the information is primarily concerned with the aesthetic vs the factual."},
            {"genre": "(NF) Humour", "icon": "",
                "description": "Books meant to illicit laughter."},
            {"genre": "(NF) Religion", "icon": "",
                "description": "Books which examine a specific religion, the history of religions, and/or the practice of worshiping a deity/deities. Includes holy books."},
            {"genre": "(NF) Folklore", "icon": "",
                "description": "Collections and studies of fairytales, legends, storytelling, and folklore."},
            {"genre": "(NF) Philosophy", "icon": "",
                "description": "Study of the nature of knowledge, existence, and being from an academic perspective."},
            {"genre": "(NF) New Age", "icon": "",
                "description": "Books that examine nontraditional spirituality or non-mainstream belief practices."},
            {"genre": "(NF) Health", "icon": "", "description": "Books that describe ways of staying healthy: how to prevent or fight a specific medical issues; nutritional ideas; alternative medicine; nursing textbooks; sex, etc."},
            {"genre": "(NF) Science", "icon": "",
                "description": "Books which explain physical or natural science concepts, including mathematics, technology, chemistry, biology, physics, engineering and more."},
            {"genre": "(NF) Social", "icon": "",
                "description": "Books that analyze societies and social relationships."},
            {"genre": "(NF) Psychology", "icon": "",
                "description": "Books that examine mental and emotional functions and well-being."},
            {"genre": "(NF) Education", "icon": "", "description": "Books that look at the education system, including teaching how-to guides, curriculum guides, lesson plan collections, homeschool guides, special education, and test prep."},
            {"genre": "(NF) Reference", "icon": "",
                "description": "Books which provide basic, objective information, like dictionaries, encyclopedias, and books of quotations."},
            {"genre": "(NF) Business", "icon": "",
                "description": "Books about managing and creating businesses, job skills and career advice, personal and business finance, investing, and how money works."},
            {"genre": "(NF) Communicate.", "icon": "",
                "description": "Books about the ways communication occurs, communicating in other languages, the best ways to communicate, and the technical aspects of types of communication."},
            {"genre": "(NF) Home", "icon": "",
                "description": "Books about designing, organizing, taking care of, decorating, and otherwise loving homes and gardens."},
            {"genre": "(NF) Animals", "icon": "",
                "description": "Books about taking care of and loving animals."},
            {"genre": "(NF) Leisure", "icon": "",
                "description": "Books about activities and hobbies done or consumed primarily for enjoyment."},
            {"genre": "(NF) Cooking", "icon": "",
                "description": "Collections of recipes and the history of food."},
            {"genre": "(NF) Crime", "icon": "",
                "description": "Books that tell the story of a specific crime or criminal, collect stories of various criminals, or tell of a historical crime."},
            {"genre": "Other", "icon": "",
                "description": "Book's genre is not in the list."},
        ]
        genre_instances = [Genre(**data) for data in genre_array]
        Genre.objects.insert(genre_instances, load_bulk=False)
    return redirect(url_for("admin_dashboard"))


@app.route("/load_books")
@roles_required("Admin")
def load_books():
    if not Book.objects():
        book = Book(
            title="Fresh Spice",
            author="Arun Kapil",
            year=2014,
            ISBN=9781909108479,
            user=current_user.username,
            short_description="Vibrant recipes for bringing flavour, depth, and colour to home cooking.",
            comments="I love reading this book, dreaming of the recipes I can make. I made the Lamb Vindaloo and it was gorgeous. Good Samosas are hard to make.",
            rating=8,
            genre="(NF) Cooking",
            private_view="off",
            book_thumbnail="https://books.google.com/books/content?id=RZmKoAEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        ).save()

        book = Book(
            title="The Art of War",
            author="Sun Tzu",
            year=1991,
            ISBN=9780877735373,
            user=current_user.username,
            short_description="Thomas Cleary's translation and commentary of the 2000 year old piece on the Art of War.",
            comments="Nothing like a little management bullshit.",
            rating=4,
            genre="(NF) Philosophy",
            private_view="off",
            book_thumbnail="https://books.google.com/books/content?id=r7TuAAAAMAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        ).save()

        book = Book(
            title="Festa",
            author="Eileen Dunne Crescenzi",
            year=2015,
            ISBN=9780717164448,
            user=current_user.username,
            short_description="Recipes and recollections.",
            comments="A veritable feast of Italian dishes.",
            rating=7,
            genre="(NF) Cooking",
            private_view="off",
            book_thumbnail="https://books.google.com/books/content?id=C8djrgEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        ).save()

        book = Book(
            title="PERL by Example",
            author="Ellie Quigley",
            year=2008,
            ISBN=9780132381826,
            user=current_user.username,
            short_description="The World's easiest PERL tutorial.",
            comments="A bit dated, sadly.",
            rating=4,
            genre="(NF) Reference",
            private_view="off",
            book_thumbnail="https://books.google.com/books/content?id=Ja0gPwAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        ).save()

        book = Book(
            title="Knife",
            author="Tim Hayward",
            year=2016,
            ISBN=9781849498913,
            user=current_user.username,
            short_description="The culture, craft and cut of the cook's knife.",
            comments="",
            rating=7,
            genre="(NF) Cooking",
            private_view="off",
            book_thumbnail="https://books.google.com/books/content?id=ctyiDAEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        ).save()

        book = Book(
            title="Cracking the Coding Interview,  6th Edition",
            author="Gayle Laakmann McDowell",
            year=2016,
            ISBN=9780984782857,
            user=current_user.username,
            short_description="189 programming questions and solutions.",
            comments="",
            rating=7,
            genre="(NF) Reference",
            private_view="off",
            book_thumbnail="https://books.google.com/books/content?id=jD8iswEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        ).save()

        book = Book(
            title="Sapiens, a Brief History of Mankind",
            author="Yuval Noah Harari",
            year=2011,
            ISBN=9780099590088,
            user=current_user.username,
            short_description="This is the thrilling account of our extraordinary history - from insignificant apes to rulers of the World.",
            comments="",
            rating=7,
            genre="(F) History",
            private_view="off",
            book_thumbnail="https://books.google.com/books/content?id=uJ_CoAEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        ).save()

        book = Book(
            title="Talking with Psychopaths and Savages",
            author="Christopher Berry-Dee",
            year=2017,
            ISBN=9781786061225,
            user=current_user.username,
            short_description="A journey into the evil mind.",
            comments="",
            rating=7,
            genre="(NF) Psychology",
            private_view="off",
            book_thumbnail="https://books.google.com/books/content?id=J2PajwEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        ).save()

        book = Book(
            title="Curry Easy",
            author="Madhur Jaffrey",
            year=2010,
            ISBN=9780091923143,
            user=current_user.username,
            short_description="A journey into the evil mind.",
            comments="",
            rating=8,
            genre="(NF) Cooking",
            private_view="off",
            book_thumbnail="https://books.google.com/books/content?id=9aTPBQAAQBAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        ).save()

        book = Book(
            title="Six Thinking Hats",
            author="Edward de Bono",
            year=1999,
            ISBN=9780141033051,
            user=current_user.username,
            short_description="A journey into the evil mind.",
            comments="",
            rating=7,
            genre="(NF) Communicate.",
            private_view="off",
            book_thumbnail="https://books.google.com/books/content?id=gCBfPgAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        ).save()

        book = Book(
            title="Voices from the Grave",
            author="Ed Moloney",
            year=2010,
            ISBN=9780571251681,
            user=current_user.username,
            short_description="Two men's war in  Ireland.",
            comments="",
            rating=7,
            genre="(NF) History",
            private_view="off",
            book_thumbnail="/static/images/BR_logo_no_thumbnail.png"
        ).save()

        book = Book(
            title="Fresh",
            author="Donal Skehan",
            year=2015,
            ISBN=9781473621039,
            user=current_user.username,
            short_description="Fresh and vibrant cooking.",
            comments="",
            rating=7,
            genre="(NF) Cooking",
            private_view="off",
            book_thumbnail="https://books.google.com/books/content?id=AxprrgEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        ).save()

        book = Book(
            title="Stockholms Kustartilleriförsvar 1914-2000",
            author="Alexander Wahlund",
            year=2017,
            ISBN=9789163927065,
            user=current_user.username,
            short_description="En guide till det fasta sjöfrontsartilleriet i Stockholms skärgård.",
            comments="",
            rating=6,
            genre="(NF) Reference",
            private_view="off",
            book_thumbnail="/static/images/BR_logo_no_thumbnail.png"
        ).save()

        book = Book(
            title="An Introduction to Assembly Language Programming for the 8086 Family",
            author="Thomas P. Skinner",
            year=1985,
            ISBN=9780471808251,
            user=current_user.username,
            short_description="Assembly Language for the Intel 8086 Microprocessor.",
            comments="",
            rating=6,
            genre="(NF) Reference",
            private_view="off",
            book_thumbnail="https://books.google.com/books/content?id=6VYZAQAAIAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        ).save()

        book = Book(
            title="TED Talks: The official TED guide to public speaking",
            author="Chris Anderson",
            year=2018,
            ISBN=9781472228062,
            user=current_user.username,
            short_description="Professional Presentation and Communication Skills on TED and TEDx.",
            comments="",
            rating=7,
            genre="(NF) Communicate.",
            private_view="off",
            book_thumbnail="https://books.google.com/books/content?id=OBn9jwEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        ).save()

        book = Book(
            title="Wine Folly",
            author="Madeline Puckette and Justin Hammack",
            year=2018,
            ISBN=9780525533894,
            user=current_user.username,
            short_description="Explore undiscovered treasures. Enjoy great food and wine. Experience the wine lifestyle.",
            comments="",
            rating=8,
            genre="(NF) Reference",
            private_view="off",
            book_thumbnail="/static/images/BR_logo_no_thumbnail.png"
        ).save()
    return redirect(url_for("admin_dashboard"))


@app.errorhandler(404)
def not_found(error):
    excuse = "Apologies, we can't seem to find the Book Repository database or worse, we've lost access to the Internet. Please click on the pink pulsating buoy to go to the Home Page (registering or signing in) or Member's Page (signed in), or click on Sign Out below."
    return render_template("oops.html", error=error, excuse=excuse, error_type="Client: 404 - Bad Request")


@app.errorhandler(500)
def internal_error(error):
    excuse = "Apologies, something serious occurred and the Leprechauns are working on resolving the issue. It's most likely Google Mail (GMail) acting up...again. Please click on the pink pulsating buoy to go to the Home Page (registering or signing in) or Member's Page (signed in), or click on Sign Out below."
    return render_template("oops.html", error=error, excuse=excuse, error_type="Server: 500 - Internal Server Error")


# export PRODUCTION=ON | OFF in TEST
# PRODUCTION App -> Settings -> Reveal Config Vars -> KEY: PRODUCTION,
# VALUE: ON
if __name__ == "__main__":
    if not os.environ.get("MONGO_URI_BR"):
        raise ValueError(
            "MongoDB Uniform Resource Identifier is missing, which means that we can't access the database.")
    elif not os.environ.get("ADMIN_PASSWORD"):
        raise ValueError(
            "Admin Password is not set which means that the Admin user can not be created.")
    elif not os.environ.get("MAIL_SERVER"):
        raise ValueError(
            "Mail Server Configuration error: MAIL_SERVER is not defined.")
    elif not os.environ.get("MAIL_PORT"):
        raise ValueError(
            "Mail Server Configuration error: MAIL_PORT is not defined.")
    elif not os.environ.get("MAIL_USERNAME"):
        raise ValueError(
            "Mail Server Configuration error: MAIL_USERNAME is not defined.")
    elif not os.environ.get("MAIL_PASSWORD"):
        raise ValueError(
            "Mail Server Configuration error: MAIL_PASSWORD is not defined.")
    elif not os.environ.get("USER_EMAIL_SENDER_EMAIL"):
        raise ValueError(
            "Mail Server Configuration error: USER_EMAIL_SENDER_EMAIL is not defined.")
    elif os.environ.get("PRODUCTION") == "ON":
        app.run(host=os.environ.get("IP"),
                port=os.environ.get("PORT"), debug=False)
    else:
        app.run(host=os.environ.get("IP"),
                port=os.environ.get("PORT"), debug=True)
