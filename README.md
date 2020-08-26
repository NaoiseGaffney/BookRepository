# Book Repository
[Book Repository on Heroku](https://book-repository-virtual.herokuapp.com/)

"A safe virtual repository for books, a digital version of your library that is searchable, and where you can share your book notes and thoughts with like-minded readers." - Gaff

The Book Repository is a digital or virtual library to store information about your books, such as title, author, year published, ISBN, genre, rating, description, and your reflection and comments.

The Book Repository provides a private and public search function too, using any combination of title, author, ISBN, genre, and rating.

An Admin Dashboard provides user management, loading of genres and books, as well as Book Repository statistics.

**Book Repository - Member's Page**

![Book Repository - Member's Page](https://github.com/NaoiseGaffney/BookRepository/blob/development/documentation/Book%20Repository%20-%20Member%20Page.png)

**Book Repository - Landing Page - Mobile**

![Book Repository - Landing Page - Mobile](https://github.com/NaoiseGaffney/BookRepository/blob/development/documentation/Book%20Repository%20-%20Landing%20Page%20-%20Mobile.jpg)
![Book Repository - Landing Page - Mobile Menu](https://github.com/NaoiseGaffney/BookRepository/blob/development/documentation/Book%20Repository%20-%20Landing%20Page%20Menu%20-%20Mobile.jpg)

## Business
### External User's Goals
Readers with libraries and/or stacks of books at home that they would like to catalogue online for easier access and overview, and share their ratings, thoughts and comments on their books with other Book Repository readers.

Seeking and finding inspiration on books to read as suggested by other readers.

### Site Owner's Goals
Inspire readers to find books they might not have heard of, and compel them to buy the books on Amazon or other book outlets, potentially providing comission to the site owner (this is not active as this is an educational project only).

### Features
The features are divided into 3 main areas, User Management, Book Repository (the main book and library features), and Admin Dashboard.

User Management:

* Flask-User extension with:
	* User/reader registration with email confirmation.
	* User/reader sign in after registration.
	* User/reader password reset with email confirmation.
	* User/reader user profile update, with first and last name, and password change.
	* User/reader sign out.
* Added user/reader delete user/reader modal to Flask-User user profile update.
* Added:
	* Help tooltips (? icon)
	* Breadcrumbs for navigation
	* Icons with text for fields and buttons for a better user experience and design.
	* Icon tooltips to guide the user/reader when filling in forms.
* Styling and Layout using Materialize CSS 1.0.0 for a clean crisp interface that's easy to view and use.

Book Repository:

* Member's Page with:
	* The user's/reader's virtual stack of books to ilicit the same feeling as walking into a library at home, or a public library.
	* The ability to view the stack, the book details, edit/update a book, and delete a book.
	* The ability to add a new book via the drop-down menu.
	* The ability to search for books via the drop-down menu.
	* The ability to view the list of book genres and their descriptions.
	* The ability to view a book on Amazon UK if it exists (using ISBN) via the title link.
	* The ability to view a book on ISBN Search if it exists (using ISBN) via the ISBN link.
* Add Book with:
	* The ability to add books with title, author, year published, ISBN (user for book front cover, link to book on Amazon UK, and link to ISBN Search), book description, book comments (personal thoughts and comments shared with other readers), book rating (1 to 10, where 10 is spectacular), genre (1 of 32 genres), and whether to hide the book from other readers during public book searches.
	* List genres via the drop-down menu to aid in selecting the most appropriate genre for the book.
* Search Books with:
	* The ability to search for public (all books except those marked private/hidden) or private (own books).
	* The ability to search for books using ISBN.
	* Theability to search for books using a combinaition to title (partial or full) and author (partial or full), rating equal to or greater than, and genre (none or 1 of 32).
* Search Books Results with:
	* The ability to browse and view books matching the search criteria.
	* The abilityto 
* Fixed Footer About Modal with:
	* Book Repository explanation.
	* Short "ego-page".
	* Code stack description and link to the project on GitHub.

Admin Dashboard:

#### Future Features
User Management:

* Username update by user/reader under update user profile, with automatic update of books belonging to the user/reader.

Book Repository:

* Validate ISBN using Python extension isbnlib when books are added and updated.
* Get full Google Books API details when adding and updating books.
* Support for multiple languages using Flask-BabelEx (i18n/i10n).

Admin Dashboard:

* User 'admin' can activate/revoke Admin role in the Admin Dashboard User Modal to share the administrative responsibilities when the site grows.
* Number of books per user/reader and genre breakdown per user/reader.
* Username update with book updates of new username.
* Save and load several book JSON files.
* Undo delete of user/reader and books (within 5 days, placing all deleted items in a separate collection).
* Create user/reader without the user/reader having to register via the register page.
* Update, add, delete genres in the genres collection.

## Processess

### User Experience
User Stories -> Use Cases -> Tasks -> Tests

## Solution
### Features
### Future Features

### Design Decisions

### Code

## Technology
### Code

### Development and Staging Platforms and Environments

### Documentation Tools

### Acknowledgements and Attributions of Used Features and Functions

### General Knowledge and Hours of Reading

## Testing

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

