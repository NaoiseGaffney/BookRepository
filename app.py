import logging
import os
from flask import Flask, render_template_string, render_template, redirect, url_for, request, flash
from flask_mongoengine import MongoEngine, MongoEngineSession, MongoEngineSessionInterface
from flask_user import login_required, UserManager, UserMixin, current_user, roles_required
# from wtforms.validators import DataRequired
# from mongoengine.errors import NotUniqueError
import datetime
from flask_debugtoolbar import DebugToolbarExtension

# generates WTForms from MongoEngine models
# from flask_mongoengine.wtf import model_form


from config import ConfigClass

from dotenv import load_dotenv
from pathlib import Path
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

# Enable logging of application events (info, warning, error)

""" Flask application factory """

# Setup Flask and load app.config
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_object(__name__+".ConfigClass")
app.debug = True

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

    # Relationships
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
    private_view = db.StringField(default="")

    # def calc_votes(self):
    # self.rating = mean(n for n in self.votes if n is not None)

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


# Create admin user as first/default user, if admin does not exist. Password is set using an environment variable.
if not User.objects.filter(User.username == "admin").first():
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


# Create the Genre Collection if it does not exist. Taken from https://bookriot.com/guide-to-book-genres/
if not Genre.objects:
    print("No Genre Objects exist.")
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
            "description": "Book's genre is not in the list."},
        {"genre": "Other", "icon": "", "description": "Books that tell the story of a specific crime or criminal, collect stories of various criminals, or tell of a historical crime."},
    ]
    genre_instances = [Genre(**data) for data in genre_array]
    Genre.objects.insert(genre_instances, load_bulk=False)


# The Home page is accessible to anyone


@app.route("/")
def home_page():
    if current_user.is_authenticated:
        return redirect(url_for("member_page"))
    return render_template("index.html")


# The Members page is only accessible to authenticated users via the @login_required decorator


@app.route("/members")
@app.route("/members/<int:page>")
@login_required
def member_page(page=1):
    # The "R" in CRUD

    """ book = Book(
        title="Fresh Spice",
        author="Arun Kapil",
        year=2014,
        ISBN=9781909108479,
        user=current_user.username,
        short_description="Vibrant recipes for bringing flavour, depth, and colour to home cooking.",
        comments="I love reading this book, dreaming of the recipes I can make. I made the Lamb Vindaloo and it was gorgeous. Good Samosas are hard to make.",
        rating=8,
        genre="(NF) Cooking",
        private_view=""
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
        private_view=""
    ).save()

    book = Book(
        title="Festa",
        author="Eileen Dunne Crescenzi",
        year=2015,
        ISBN=9780717164448,
        user=current_user.username,
        short_description="Recipes and recollections.",
        comments="An veritable feast of Italian dishes.",
        rating=7,
        genre="(NF) Cooking",
        private_view=""
    ).save() """

    app.logger.info(f"Member Page Accessed by {current_user.username}.")

    books_pagination = Book.objects.filter(user=current_user.username).paginate(page=page, per_page=7)
    return render_template("members.html", books_pagination=books_pagination, page_prev=(page-1), page_next=(page+1))


@app.route("/add_book")
@login_required
def add_book():
    # Preparing for the "C" in CRUD
    genre = Genre.objects()
    app.logger.info(f"{current_user.username} is about to add a book.")
    return render_template("add_book.html", genre=genre)


@app.route("/save_book", methods=["POST"])
@login_required
def save_book():
    # The "C" in CRUD
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

    try:
        book.save()
        flash(f"The book {book.title} was saved!", "success")
        app.logger.info(
            f"{book.title} with id {book.id} created by {current_user.username}.")
    except:
        app.logger.error(
            f"{book.title} with id {book.id} not created by {current_user.username}.")
        flash(f"The book {book.title} was NOT saved!", "danger")
    return redirect(url_for("member_page"))


@app.route("/edit_book/<book_id>")
@login_required
def edit_book(book_id):
    # Preparing for the "U" in CRUD
    book = Book.objects.get(id=book_id)
    genre = Genre.objects()
    app.logger.info(
        f"{book.title} with id {book.id} to be edited by {current_user.username}.")
    return render_template("edit_book.html", book=book, genre=genre)


@app.route("/update_book/<book_id>", methods=["POST"])
@login_required
def update_book(book_id):
    # The "U" in CRUD
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
    try:
        book.update(**fields)
        flash(f"The book {book.title} is updated!", "success")
        app.logger.info(
            f"{book.title} with id {book.id} edited by {current_user.username}.")
    except:
        app.logger.error(
            f"{book.title} with id {book.id} edited by {current_user.username}.")
        flash(f"The book {book.title} was NOT updated!", "danger")
    return redirect(url_for("member_page"))


@app.route("/delete_book/<book_id>")
@login_required
def delete_book(book_id):
    # The "D" in CRUD
    book = Book.objects.get(id=book_id)
    try:
        book.delete()
        flash(f"The book {book.title} is deleted!", "success")
        app.logger.info(
            f"{book.title} with id {book.id} deleted by {current_user.username}.")
    except:
        app.logger.error(
            f"{book.title} with id {book.id} NOT deleted by {current_user.username}.")
        flash(f"The book {book.title} was NOT deleted!", "danger")
    return redirect(url_for("member_page"))


@app.route("/search_book")
@login_required
def search_book():
    genre = Genre.objects()
    return render_template("search_book.html", genre=genre)


@app.route("/search_results", methods=["POST"])
# @app.route("/search_results/<int:page>")
@login_required
def search_results():
    # Get search form data
    form_title = request.form.get("title")
    form_author = request.form.get("author")
    try:
        form_isbn = int(request.form.get("isbn"))
    except ValueError:
        form_isbn = 0

    try:
        form_rating = int(request.form.get("rating"))
    except ValueError:
        form_rating = 1

    form_genre = request.form.get("genre")
    form_private_view = request.form.get("private_view")

    print(form_title, form_author, form_isbn, form_rating, form_genre)

    # Query Book Repository based on the search form data
    if form_private_view == "on":
        if form_isbn:
            books_pagination = Book.objects.filter(user=current_user.username, ISBN=form_isbn)
            return render_template("test.html", books_pagination=books_pagination)
        elif form_genre == None:
            books_pagination = Book.objects.filter(user=current_user.username, title__icontains=form_title, author__icontains=form_author, rating__gte=form_rating).order_by("+title", "+author", "-rating")
            return render_template("test.html", books_pagination=books_pagination)
        else:
            books_pagination = Book.objects.filter(user=current_user.username, title__icontains=form_title, author__icontains=form_author, rating__gte=form_rating, genre=form_genre).order_by("+title", "+author", "-rating")
            return render_template("test.html", books_pagination=books_pagination)
    else:
        if form_isbn:
            books_pagination = Book.objects.filter(ISBN=form_isbn)
            return render_template("test.html", books_pagination=books_pagination)
        elif form_genre == None:
            books_pagination = Book.objects.filter(title__icontains=form_title, author__icontains=form_author, rating__gte=form_rating).order_by("+title", "+author", "-rating")
            return render_template("test.html", books_pagination=books_pagination)
        else:
            books_pagination = Book.objects.filter(title__icontains=form_title, author__icontains=form_author, rating__gte=form_rating, genre=form_genre).order_by("+title", "+author", "-rating")
            return render_template("test.html", books_pagination=books_pagination)

    # book_query_results = Book.objects.filter(user=current_user.username, title__icontains=form_title, author__icontains=form_author, ISBN=form_isbn, rating__lte=form_rating, genre=form_genre).order_by("+title", "+author", "-rating").paginate(page=page, per_page=7)


# export PRODUCTION=ON | OFF in TEST
# PRODUCTION App -> Settings -> Reveal Config Vars -> KEY: PRODUCTION, VALUE: ON
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
