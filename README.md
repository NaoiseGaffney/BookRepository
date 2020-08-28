# Book Repository
[Book Repository on Heroku](https://book-repository-virtual.herokuapp.com/)

"A safe virtual repository for books, a digital version of your library that is searchable, and where you can share your book notes and thoughts with like-minded readers." - Gaff

![Book Repository Logo](https://github.com/NaoiseGaffney/BookRepository/blob/development/static/images/logo_bookstack_text_96_spacing.png)

The Book Repository is a digital or virtual library to store information about your books, such as title, author, year published, ISBN, genre, rating, description, and your reflection and comments.

The Book Repository provides a private and public search function too, using any combination of title, author, ISBN, genre, and rating.

An Admin Dashboard provides user management, loading of genres and books, as well as Book Repository statistics.

The Book Repository is inspired by my own love of books and reading, and my propensity to stack my books all over the house (makes it easy to see and read them), much to the annoyance of my wife. This way I have the means to store details of my books online, browse my digital stack and find the inspiration to read a book again, or better yet read a new book based on another reader's stack of books.

## Business
The Business goals describe the expected user/reader and site owner goals, and drive the design, development, and deployment of the application which in this case is the Book Repository. The fulfillment of these goals detemine the success of the application.

### External User's Goals
Readers with libraries and/or stacks of books at home that they would like to catalogue online for easier access and overview, and share their ratings, thoughts and comments on their books with other Book Repository readers.

Seeking and finding inspiration on books to read as suggested by other readers.

### Site Owner's Goals
Inspire readers to find books they might not have heard of, and compel them to buy the books on Amazon or other book outlets, potentially providing comission to the site owner (this is not active as this is an educational project only).

Find new books to read, broadening my horizons, and enjoying the excitement of delving into the mind and perspective of the author.

## User Experience

User experience (UX) design is the design process used to create applications and websites that provide meaningful and relevant experiences to users. The User Experience links the Business goals of the external user and site owner to a number of user stories. A user story captures a description of a software feature from an end-user perspective. A user story describes the type of user, what they want and why. A use case is a list of actions or event steps describing the interactions between a role and a system to achieve a goal.

A user story has one or more use cases with one or more tasks with steps associated with it, describing how the user story, and subsequent fulfillment of the external user's and site owner's business goals are realised: Business Goals -> User Story -> Use Case(s) -> Task(s) -> Steps.

* **User Story 001 (User/Reader):** as a new user/reader I want to join the Book Repository to store details about my books so that I can share them with a wider audience.
	* **Use Case 001-001 (C in User CRUD):** as a new user/reader I want to register an account with the Book Repository.
		*  **Tasks 1:** [Book Repository Home/Landing Page](https://book-repository-virtual.herokuapp.com/) -> read and accept the Consent Cookie (optional) -> click on Register in the naviagtion bar or the hamburger-menu followed by Register [Register](https://book-repository-virtual.herokuapp.com/user/register) -> fill in the form: username, email address, password, password confirmation, and click on the Register button -> if successful: a success Flash message, otherwise a danger Flash message.
		*  **Tasks 2:** a confirmation email with a link is sent to the email address specified during registration -> click on the link -> you're accepted and signed in at the same time -> Member's Page -> two success Flash messages, one for registration and one for sign in.
	*  **Use Case 001-002:** as a user/reader I want to Sign In to the Book Repository to access my stack of books.
		*  **Tasks 1:** [Book Repository Home/Landing Page](https://book-repository-virtual.herokuapp.com/) -> read and accept the Consent Cookie (optional) -> click on Sign In in the navigation bar or the hamburger-menu followed by Sign In [Sign In](https://book-repository-virtual.herokuapp.com/user/sign-in) -> enter your username and password (the same credentials used when registering), click on the Remember Me box (optional), and click on the Sign In button -> success Flash message and [Member's Page](https://book-repository-virtual.herokuapp.com/members).
	*  **Use Case 001-003:** as a user/reader I want to reset my password as I have forgotten it.
		*  **Tasks 1:** [Book Repository Home/Landing Page](https://book-repository-virtual.herokuapp.com/) -> read and accept the Consent Cookie (optional) -> click on Sign In in the navigation bar or the hamburger-menu followed by Sign In [Sign In](https://book-repository-virtual.herokuapp.com/user/sign-in) -> click on [Forgot Your Password?](https://book-repository-virtual.herokuapp.com/user/forgot-password) -> enter your email address, the same one you used o register your acccount and click on the Send Reset Password Email button -> success Flash message.
		*  **Tasks 2:** a password reset email is sent to the provided email address, provided it exists in the Book Repository -> click on the password link to reset your password or ignore if you don't need to reset your password -> [Reset Password](https://book-repository-virtual.herokuapp.com/user/reset-password/...) -> enter your new password, retype your new password to confirm, and click on the Change Password button -> success Flash message and [Member's Page](https://book-repository-virtual.herokuapp.com/members).
		*  **Tasks 3:** an email confirming your password change is sent to the email address you provided -> if you initiated the password change, do nothing, otherwise click on the "click here to reset it" link.
	*  **Use Case 001-004 (C in Book CRUD):** as a user/reader I want to add a book to my virtual library/stack of books.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on the Add Book button on the page if you have no books, or hover over the drop-down menu (open book) and click on Add Book -> [Add Book](https://book-repository-virtual.herokuapp.com/add_book) fill in the form: title, author, year published, ISBN (used for book front cover, link to book on Amazon UK, and link to ISBN Search), book description (optional), book comments (optional), book rating (from 1 to 10, where 10 is spectacular), genre, and toggle the private switch if you want your book to remain hidden from other users/readers, and click on the Add Book button -> success Flash message and [Member's Page](https://book-repository-virtual.herokuapp.com/members)
	*  **Use Case 001-005 (R in Book CRUD):** as a user/reader I want to view a book in my virtual library/stack of books.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on the "book spine" and it will pop-out displaying the collapsible-content with book details -> click on the title link to view the book in a separate tab on Amazon UK (uses the ISBN as a reference, for example: https://www.amazon.co.uk/s?k=9780141185378 for Burmese Days) -> click on ISBN link to view the book in a separate tab on ISBN Search (uses the ISBN as a reference, for example: https://isbnsearch.org/isbn/9780141185378 for Burmese Days).
	*  **Use Case 001-006 (U in Book CRUD):** as a user/reader I want to update/edit an existing book in my Book Repository stack.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on the dark blue pencil link on the book spine of the book you want to update -> [Edit Book - Burmese Days](https://book-repository-virtual.herokuapp.com/edit_book/5f480c6727f905184bcf1a51) -> make the necessary changes to title, author, year published, ISBN (to update the front cover thumbnail, Amazon UK and ISBN Search links), book description, book comments (add new, update or delete existing comments), rating, genre, and whether the book is hidden (private) from public searches, and click on the Add Book button -> success Flash message and [Member's Page](https://book-repository-virtual.herokuapp.com/members).
	*  **Use Case 001-007 (D in Book CRUD):** as a user/reader I want to delete an existing book in my Book Repository stack.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on the pink dustbin/rubbish bin link on the book spine of the book you want to delete the book -> [Delete Book - Burmese Days](https://book-repository-virtual.herokuapp.com/members#delete_book_5f480c6727f905184bcf1a51) -> the delete book modal provides a yes (permanently delete book: [Delete Book - Yes](https://book-repository-virtual.herokuapp.com/delete_book/5f480c6727f905184bcf1a51)) button and a no (close modal: [Delete Book - No](https://book-repository-virtual.herokuapp.com/members#!)) button -> success Flash message and [Member's Page](https://book-repository-virtual.herokuapp.com/members).

*  **User Story 002 (User/Reader):** as a user/reader I want to search for books in the Book Repository so that I can find new books to read, inspired by reader comments, and possibly purchase on Amazon UK or from other vendors.
	*  **Use Case 002-001 (R in Book CRUD):** as a user/reader I want to search for a specific book in my Book Repository using the ISBN.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> via the drop-down menu click on Search Books -> [Search Books](https://book-repository-virtual.herokuapp.com/search_book) -> enter the ISBN (9780141185378) of the book I'm searching for, toggle the private switch on (private search), and click on the Search Books button -> [Search Results](https://book-repository-virtual.herokuapp.com/search_results) -> Burmese Days by George Orwell -> Book CRUD operations apply as this is my book.
	*  **Use Case 002-002 (R in Book CRUD):** as a user/reader I want to search for books in my Book Repository using any combination of title, author, and rating (not genre, nor ISBN).
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> via the drop-down menu click on Search Books -> [Search Books](https://book-repository-virtual.herokuapp.com/search_book) -> enter any combination of title (empty, partial, or full), author (empty, partial, or full) of the book I'm searching for, toggle the private switch on (private search), rating (from 1 to 10, value searched for is >= value entered), and click on the Search Books button -> [Search Results](https://book-repository-virtual.herokuapp.com/search_results) -> stack (list) of books found -> Book CRUD operations apply as these are my books.
	*  **Use Case 002-003 (R in Book CRUD):** as a user/reader I want to search for all my books in my Book Repository using an empty form search.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> via the drop-down menu click on Search Books -> [Search Books](https://book-repository-virtual.herokuapp.com/search_book) -> leave all form fields empty, toggle the private switch on (private search), and click on the Search Books button -> [Search Results](https://book-repository-virtual.herokuapp.com/search_results) -> stack (list) of books found (same result as my Book Stack in my Member's Page) -> Book CRUD operations apply as these are my books
	*  **Use Case 002-004 (R in Book CRUD):** as a user/reader I want to search for a specific book the Book Repository using the ISBN.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> via the drop-down menu click on Search Books -> [Search Books](https://book-repository-virtual.herokuapp.com/search_book) -> enter the ISBN (9780141185378) of the book I'm searching for, leave the toggle switch off (public search), and click on the Search Books button -> [Search Results](https://book-repository-virtual.herokuapp.com/search_results) -> Burmese Days by George Orwell (if the book isn't marked as private/hidden by users/readers) -> Book CRUD operations apply as this is my book, otherwise only R in Book CRUD as the book belongs to someone else.
	*  **Use Case 002-005 (R in Book CRUD):** as a user/reader I want to search for books in the Book Repository using any combination of title, author, and rating (not genre, nor ISBN).
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> via the drop-down menu click on Search Books -> [Search Books](https://book-repository-virtual.herokuapp.com/search_book) -> enter any combination of title (empty, partial, or full), author (empty, partial, or full) of the book I'm searching for, leave the toggle switch off (public search), rating (from 1 to 10, value searched for is >= value entered), and click on the Search Books button -> [Search Results](https://book-repository-virtual.herokuapp.com/search_results) -> stack (list) of books found that are not  marked as private/hidden by users/readers -> Book CRUD operations apply to my books, only R in Book CRUD for books belonging to other users/readers.
	*  **Use Case 002-006 (R in Book CRUD):** as a user/reader I want to search for all the books in the Book Repository using an empty form search.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> via the drop-down menu click on Search Books -> [Search Books](https://book-repository-virtual.herokuapp.com/search_book) -> leave all form fields empty, leave the toggle switch off (public search), and click on the Search Books button -> [Search Results](https://book-repository-virtual.herokuapp.com/search_results) -> stack (list) of books found that are not  marked as private/hidden by users/readers -> Book CRUD operations apply to my books, only R in Book CRUD for books belonging to other users/readers.

*  **User Story 003 (User/Reader):** as a user/reader I want the ability to manage my user profile so that I can have the best possible user/reader exeperience.
	*  **Use Case 003-001 (U in User CRUD):** as a user/reader I want to update my user profile.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on the user profile (username) on the navigation bar [Edit User Profile](https://book-repository-virtual.herokuapp.com/user/edit_user_profile) -> add/edit your First and Last Name, click on the Update button -> success Flash message and [Member's Page](https://book-repository-virtual.herokuapp.com/members).
	*  **Use Case 003-002 (U in User CRUD):** as a user/reader I want to change my password.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on the user profile (username) on the navigation bar [Edit User Profile](https://book-repository-virtual.herokuapp.com/user/edit_user_profile) -> click on [Change Password](https://book-repository-virtual.herokuapp.com/user/change-password) -> enter your current/old password, your new password, retype your new password for confirmation, and click on the Change Password button -> success Flash message and [Member's Page](https://book-repository-virtual.herokuapp.com/members).
		*  **Tasks 2:** an email is sent to the user's/reader's email address, confirming the password change -> if the password change wasn't initiated by the user/reader they can click on the link in the email to change the password.
	*  **Use Case 003-003 (D in User CRUD):** as a user/reader I want to delete my account.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on the user profile (username) on the navigation bar [Edit User Profile](https://book-repository-virtual.herokuapp.com/user/edit_user_profile) -> click on [Delete User](https://book-repository-virtual.herokuapp.com/user/edit_user_profile#delete_user) -> click on yes to permanetly delete the user/reader and associated books from the Book Repository or no to close the delete user modal -> success Flash message [Landing/Home Page](https://book-repository-virtual.herokuapp.com/index.html).

*  **User Story 004 (User 'admin' and user/reader with Admin Role):** as an admin or user/reader with the Admin Role I want to manage the users, genres, books, and statistics so that I can provide the best possible Book Repository experince for the users/readers.
	*  **Use Case 004-001 (R in Admin User CRUD):** as an admin I want to view the users/readers in the Book Repository.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on [Admin Page](https://book-repository-virtual.herokuapp.com/admin_dashboard) -> view the paginated table (10 users per page) and navigate between the pages using the < > and the page numbers -> click on a user/reader link -> view: active/inactive status, first and last name, password (hidden and hashed), and email address, and click on the Cancel button to get back to [Admin Page](https://book-repository-virtual.herokuapp.com/admin_dashboard).
	*  **Use Case 004-002 (U in Admin User CRUD):** as an admin I want to update the user/readers details in the Book Repository.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on [Admin Page](https://book-repository-virtual.herokuapp.com/admin_dashboard) -> view the paginated table (10 users per page) and navigate between the pages using the < > and the page numbers -> click on a user/reader link -> view: active/inactive status, first and last name, password (hidden and hashed), and email address -> update the form fields: activate/deactivate (inactive) user/reader (inactive = user/reader can't sign in), first and last name, password and retype password (once submitted the new password is hashed), and email address, and click on the Update button when done or Cancel button if no updates are required -> sucess Flash message and [Admin Page](https://book-repository-virtual.herokuapp.com/admin_dashboard).
	*  **Use Case 004-003 (D in Admin User CRUD):** as an admin I want to delete the user/reader and associated books permanently.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on [Admin Page](https://book-repository-virtual.herokuapp.com/admin_dashboard) -> view the paginated table (10 users per page) and navigate between the pages using the < > and the page numbers -> click on a user/reader link -> view: active/inactive status, first and last name, password (hidden and hashed), and email address -> click on the Delete button (there is no "Are you sure?" modal) or Cancel button if no deletion is required -> success Flash message and [Admin Page](https://book-repository-virtual.herokuapp.com/admin_dashboard).
	*  **Use Case 004-004 (C in Genre CRUD):** as an admin I want to load the 'genre.json' file (book genres) to the Genre Collection so that they can be used by the users/readers when adding, updating, and viewing books.
		*  **Tasks 1:** (optional) update the 'genre.json' file to suit your Book Repository requirements: genre and description.
		*  **Tasks 2:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on [Admin Page](https://book-repository-virtual.herokuapp.com/admin_dashboard) -> hover over the drop-down (category icon) menu and click on the Load Genres button -> if the Genre Collection already exists a Flash message will say so, otherwise a Flash message will say successful creation and [Admin Page](https://book-repository-virtual.herokuapp.com/admin_dashboard).
	*  **Use Case 004-005 (R in Genre CRUD):** as an admin I want view the list of genres.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on [Admin Page](https://book-repository-virtual.herokuapp.com/admin_dashboard) -> hover over the drop-down (category icon) menu and click on the List Genres button -> scroll through the list of genres and their descriptions in the modal, click on the Done button to close -> [Admin Page](https://book-repository-virtual.herokuapp.com/admin_dashboard).
	*  **Use Case 004-006 (C in Book CRUD):** as an admin I want to load a sample book file, 'book.json', to the Book Collection so that I can start off the Book Repository with some books and also use for BDD testing purposes.
		*  **Tasks 1:** (optional) update the 'book.json' file to suit your Book Repository requirements.
		*  **Tasks 2:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on [Admin Page](https://book-repository-virtual.herokuapp.com/admin_dashboard) -> hover over the drop-down (category icon) menu and click on the Load Books button -> if the Book Collection already exists a Flash message will say so, otherwise a Flash message will say successful creation and [Admin Page](https://book-repository-virtual.herokuapp.com/admin_dashboard).
	*  **Use Case 004-007 (R in Statistics CRUD):** as an admin I want to view the number of users, number of books, and the most popular genres in the Book Repository.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on [Admin Page](https://book-repository-virtual.herokuapp.com/admin_dashboard) -> hover over the drop-down (category icon) menu and click on the Statistics button -> scroll through the statitics and click on the Done button to close the modal -> [Admin Page](https://book-repository-virtual.herokuapp.com/admin_dashboard).

## Features
A feature is some action that can be performed by a user of an application, or is some internal function of an application. The features support the User Experience mentioned above and are implemented based on the business goals, user stories and use cases.

The features are divided into 4 main areas, User Management, Book Repository (the main book and library features), Admin Dashboard, and Shared Features.

### User Management:

* Flask-User extension with:
	* User/reader registration with email confirmation (C is User CRUD).
	* User/reader sign in after registration (R in User CRUD).
	* User/reader password reset with email confirmation.
	* User/reader user profile update, with first and last name, and password change (U in User CRUD).
	* User/reader sign out.
* Added user/reader delete user/reader modal to Flask-User user profile update (D in User CRUD).

### Book Repository:

* Member's Page with:
	* The user's/reader's virtual stack of books to ilicit the same feeling as walking into a library at home, or a public library.
	* The ability to view the stack, the book details, edit/update a book, and delete a book (RUD in Book CRUD).
	* The ability to add a new book via the drop-down menu (C in Book CRUD).
	* The ability to search for books via the drop-down menu (R in Book CRUD).
	* The ability to view the list of book genres and their descriptions (R in Book CRUD).
	* The ability to view a book on Amazon UK if it exists (using ISBN) via the title link.
	* The ability to view a book on ISBN Search if it exists (using ISBN) via the ISBN link.
* Add Book with (C in Book CRUD):
	* The ability to add books with title, author, year published, ISBN (used for book front cover, link to book on Amazon UK, and link to ISBN Search), book description, book comments (personal thoughts and comments shared with other readers), book rating (1 to 10, where 10 is spectacular), genre (1 of 32 genres), and whether to hide the book from other readers during public book searches.
	* List genres via the drop-down menu to aid in selecting the most appropriate genre for the book.
* Search Books with (R in Book CRUD):
	* The ability to search for public (all books except those marked private/hidden) or private (own books).
	* The ability to search for books using ISBN.
	* Theability to search for books using a combinaition to title (partial or full) and author (partial or full), rating equal to or greater than, and genre (none or 1 of 32).
* Search Books Results with:
	* The ability to browse and view books matching the search criteria.
	* The ability to edit/update books belonging to the current user/reader (books belonging to other users/readers can't be edited/updated, nor deleted).

### Admin Dashboard:

* Admin Page with:
	* User Management table, User, Full Name, Active, E-mail.
		* User modal to update user details, set user to active/inactive, and permanently deleter the user/reader and associated books (RUD in User CRUD).
		* Load Genres via the drop-down menu in case the genres collection wasn't created by the first access to the Landind Page or was accidentally deleted  (C in Book Genre CRUD).
		* Load Books via the drop-down menu to load a sample of 28 books to populate the Book Repository and use for testing purposes (C in Book CRUD).
		* List Genres, to view the 32 genres and their description. Future feature to add, update, and delete genres here (R in Book Genre CRUD).
		* Book Repository Statistics via the drop-down menu to vie the number of users, number of books, and number of books in each genre (R in Statistics CRUD).

### Shared Features:

* Added:
	* Help tooltips (? icon).
	* Breadcrumbs for navigation.
	* Pagination for Member's Page, Search Results Page, and Admin Page (user table).
	* Icons with text for fields and buttons for a better user experience and design.
	* Icon tooltips to guide the user/reader when filling in forms.
	* Drop-Down Menu.
* Fixed Navigation Bar (Hamburger-Menu) with:
	* User/reader:
		* Unauthenticated - Home, Sign In, Register.
		* Authenticated - Member's Page, User Profile Update (username), Sign Out.
	* Admin Role:
		* Unauthenticated - Home, Sign In, Register.
		* Authenticated - Admin Page, Member's Page, User Profile Update (username), Sign Out.
* Fixed Footer About Modal with:
	* Book Repository explanation.
	* Short "ego-page".
	* Code stack description and link to the project on GitHub.
* Styling and Layout using Materialize CSS 1.0.0 for a clean crisp interface that's easy to view and use.
* Osano Consent Cookie.

## Future Features
Future features are planned features that didn't make it into this first release due to time, effort, current knowledge and skills constraints (I know it can be done, I haven't yet figured out how).

### User Management:

* Username update by user/reader under update user profile, with automatic update of books belonging to the user/reader.

### Book Repository:

* Validate ISBN using Python extension isbnlib when books are added and updated.
* Get full Google Books API details when adding and updating books.
* Support for multiple languages using Flask-BabelEx (i18n/i10n).
* Shared book comments.
* User/reader messaging/message board.

### Admin Dashboard:

* User 'admin' can activate/revoke Admin role in the Admin Dashboard User Modal to share the administrative responsibilities when the site grows.
* Number of books per user/reader and genre breakdown per user/reader.
* Username update with book updates of new username.
* Save and load several book JSON files.
* Undo delete of user/reader and books (within 5 days, placing all deleted items in a separate collection(s)).
* Create user/reader without the user/reader having to register via the register page.
* Update, add, delete genres in the genres collection.
* Application Log view in the Admin Dashboard, primarily to view rogue users/readers and to revoke their access to the Book Repository.

### Shared Features
* Implement [Flask-Paranoid](https://flask-paranoid.readthedocs.io/en/latest/) to protect against stolen user session cookies (Flask-Login 'SESSION_PROTECTION = "strong"' isn't enough).

## Features CRUD Table (Views)
'X' = CRUD feature implemented

'f' = future CRUD implementation

'?' = unplanned/undecided future CRUD implementation

'' = not planning to implement CRUD feature

| Collection or Role or Feature | C | R | U | D | Notes                                                                                                                                                                                                                                                      |
|-------------------------------|---|---|---|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| User                          | X | X | X | X | User/Reader has full CRUD control of their accounts. Creation = Registration. Read = User Profile. Update = Edit User Profile. Delete = Edit User Profile -> Delete User (associated books).                                                               |
| Book                          | X | X | X | X | User/Reader has full CRUD control of their books. Create = Add Book. Read = Member's Page and Search Results Page. Update = Update/Edit Book. Delete = Delete Book.                                                                                        |
| Genre                         | X | X | f | f | User 'admin' or Admin Role has partial control, however the Genre Collection is created at "first touch" on the Landing/Home Page. The User/Reader has Read access to the Genre list when viewing, adding, or updating books.                              |
| Admin User                    | ? | X | X | X | Admin Role can view, update user profile details (except username), set user/reader account to inactive, and permanently delete the user/reader and associated books.                                                                                      |
| Admin Statistics              |   | X |   |   | Statistics provided are: number of users/readers, number of books, table of current genres used and number of each in descending order. Future feature includes the number of books and genre per user.                                                    |
| Application Logs              | X | f |   | X | Application logs provide application endpoint/function information related to each user/reader. In future, viewing these logs, and filtering them per user/reader and severity is useful to identify issues. Rotating logs are deleted after 10 instances. |

## Application Logging and Flash Messaging Levels
| Logger   | Flash   | Message       | Environments                                                 | Notes                                                                                                                                                    |
|----------|---------|---------------|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Notset   |         |               |                                                              |                                                                                                                                                          |
| Debug    |         |               | Local Development, Heroku Review Application, Heroku Staging | Local development = Flask Debug Toolbar. Heroku Review Application and Heroku Staging = Application Console.                                             |
| Info     | Success | Success, Info |                                                              | Application Log (rotating file logger and console) = Info. Flash Message = Success (teal). Book Repository Message in Application Log = Success or Info. |
| Warning  |         | Warning       |                                                              | Application Log (rotating file logger and console) = Warning. Book Repository Message in Application Log = Warning.                                      |
| Error    |         |               |                                                              |                                                                                                                                                          |
| Critical | Danger  | Failure       | Heroku Production                                            | Application Log (rotating file logger and console) = Critical. Flash Message = Danger (pink). Book Repository Message in Application Log = Failure.      |

## Design

## Technology
### Code

### Development and Staging Platforms and Environments

### Documentation Tools

### Acknowledgements and Attributions of Used Features and Functions

### General Knowledge and Hours of Reading

## Testing and Validation
### Manual BDD

### Automated BDD

### Testing Notes

### Validation of HTML 5, CSS 3, JS and Python

## Continuous Delivery and Deployment

## Credits
![GaffCo Consulting Logo](https://github.com/NaoiseGaffney/Professional-Training-Development/blob/master/docs/GaffCo%20-%20Background.png)

GaffCo Consulting - [Naoise Gaffney: naoise.gaff.gaffney@gmail.com](mailto:naoise.gaff.gaffney@gmail.com)

![Code Institute Logo](https://github.com/NaoiseGaffney/Professional-Training-Development/blob/master/docs/CodeInstituteLogo.png)

Code Institute Mentor - [GitHub: 5pence - Spencer Barriball](https://github.com/5pence)

### Content

### Media

### Acknowledgements

The Diploma in Full Stack Development provides a great foundation of tools and technologies used to work as a professional developer. It's a case of being a Jack-of-All-Trades, and a Master of None (or Some). It's up to each developer to expand upon the knowledge and skills acquired during the course through additional self-study of elements covered as a part of the course as well as other frameworks, languages, tools, methodologies,  processes, and solutions.

Thank you Code Institute for allowing me on this journey in life!

Thank you Spencer Barriball for your unwavering support!

