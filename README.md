# Book Repository
[Book Repository on Heroku](https://book-repository-virtual.herokuapp.com/)

"A safe virtual repository for books, a digital version of your library that is searchable, and where you can share your book notes and thoughts with like-minded readers." - Gaff

![Book Repository Logo](static/images/logo_bookstack_text_96_spacing.png)

The Book Repository is a digital or virtual library to store information about your books, such as title, author, year published, ISBN, genre, rating, description, and your reflection and comments.

The Book Repository provides a private and public search function too, using any combination of title, author, ISBN, genre, and rating.

An Admin Dashboard provides user management, loading of genres and books, as well as Book Repository statistics.

The Book Repository is inspired by my own love of books and reading, and my propensity to stack my books all over the house (makes it easy to see and read them), much to the annoyance of my wife. This way I have the means to store details of my books online, browse my digital stack and find the inspiration to read a book again, or better yet read a new book based on another reader's stack of books.

![Section Divider: Title and Business](documentation/section%20divider.png)

<details><summary>Please click to expand the ToC</summary>

- [Book Repository](#book-repository)
  * [Business](#business)
    + [External User's Goals](#external-user-s-goals)
    + [Site Owner's Goals](#site-owner-s-goals)
  * [User Experience](#user-experience)
    + [A Persona Summary of the Users/Readers of the Book Repository](#a-persona-summary-of-the-users-readers-of-the-book-repository)
    + [Strategy Trade-Off](#strategy-trade-off)
    + [User Stories, Use Cases, and Tasks Mapped to Information Architecture and Navigation](#user-stories--use-cases--and-tasks-mapped-to-information-architecture-and-navigation)
  * [Design Decisions](#design-decisions)
    + [Design Decisions Overview](#design-decisions-overview)
    + [Interface and Navigation Design](#interface-and-navigation-design)
    + [Design Details](#design-details)
      - [Typography](#typography)
      - [Colour Scheme](#colour-scheme)
      - [Buttons](#buttons)
      - [Navigation Bar](#navigation-bar)
      - [Fixed Footer](#fixed-footer)
      - [Background Image](#background-image)
      - [Flash Messages](#flash-messages)
      - [Tooltips](#tooltips)
      - [Breadcrumbs](#breadcrumbs)
      - [Pagination](#pagination)
      - [Logo](#logo)
      - [Favicon](#favicon)
      - [Book Stack](#book-stack)
      - [Tables](#tables)
  * [Features](#features)
    + [Existing Features](#existing-features)
      - [User Management:](#user-management-)
      - [Book Repository:](#book-repository-)
      - [Admin Dashboard:](#admin-dashboard-)
      - [Shared Features:](#shared-features-)
    + [Future Features](#future-features)
      - [User Management:](#user-management--1)
      - [Book Repository:](#book-repository--1)
      - [Admin Dashboard:](#admin-dashboard--1)
      - [Shared Features](#shared-features)
    + [Information and Visual Design](#information-and-visual-design)
    + [Features CRUD Table (Views)](#features-crud-table--views-)
    + [Application Logging and Flash Messaging Levels](#application-logging-and-flash-messaging-levels)
    + [Book Repository '.env' and Heroku Variables](#book-repository--env--and-heroku-variables)
    + [Flask-User and Book Repository Routes](#flask-user-and-book-repository-routes)
    + [Flask, Flask-User, and Book Repository Configuration Variables](#flask--flask-user--and-book-repository-configuration-variables)
  * [Technology](#technology)
    + [Technology Choices](#technology-choices)
    + [Code](#code)
    + [Development and Staging Platforms and Environments](#development-and-staging-platforms-and-environments)
    + [Documentation Tools](#documentation-tools)
    + [Acknowledgements and Attributions of Used Features and Functions](#acknowledgements-and-attributions-of-used-features-and-functions)
    + [General Knowledge and Hours of Reading](#general-knowledge-and-hours-of-reading)
  * [Testing and Validation](#testing-and-validation)
    + [Manual BDD](#manual-bdd)
    + [Automated BDD](#automated-bdd)
    + [Testing Notes](#testing-notes)
    + [Validation of HTML 5, CSS 3, JS and Python](#validation-of-html-5--css-3--js-and-python)
  * [Continuous Delivery and Deployment](#continuous-delivery-and-deployment)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
    + [Acknowledgements](#acknowledgements)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

</details>

![Section Divider: Title and Business](documentation/section%20divider.png)

## Business
The Business goals describe the expected user/reader and site owner goals, and drive the design, development, and deployment of the application which in this case is the Book Repository. The fulfillment of these goals detemine the success of the application.

### External User's Goals
Readers with libraries and/or stacks of books at home that they would like to catalogue online for easier access and overview, and share their ratings, thoughts and comments on their books with other Book Repository readers.

Seeking and finding inspiration on books to read as found by reading the book comments and ratings by the other readers.

### Site Owner's Goals
Inspire readers to find books they might not have heard of, and compel them to buy the books on Amazon or other book outlets, potentially providing comission to the site owner (this is not active as this is an educational project only).

Find new books to read, broadening my horizons, and enjoying the excitement of delving into the mind and perspective of the author.

![Section Divider: Business and User Experience](documentation/section%20divider.png)

## User Experience
User experience (UX) design is the design process used to create applications and websites that provide meaningful and relevant experiences to users.

### A Persona Summary of the Users/Readers of the Book Repository
![Persona Summary](documentation/Persona%20Summary.png)

The Book Repository is for readers of all ages (please see next paragraph), diverse demographics and interests, with a preference for real books as opposed to digital media like Kindle (digital media has online libraries and ways of sorting and sharing their books already), and who want to gain some measure of control over their growing stack or library of books through a Book Repository with the additional means to share their views and ratings on books, while also gaining insights and ideas from fellow readers.

The age limit of 18 exists as some books shared may not be suitable for children, and may not be marked as hidden by the user/reader from public searches. It's recommended that people under the age of 18 use the Book Repository under the supervision of a parent or other guardian.

Since the Book Repository aims to satisfy the requirements of a diverse demographic and age group, ease-of-use is key which is described in the section on Design Decisions and Technology Choices.

### Strategy Trade-Off
UX Design is driven by business goals and user needs, and features developed are aligned to these. However, each feature requires time and effort, and often time is constrained as is effort as the greater the effort the higher the cost. Therefore some features are prioritised or mandatory, while others are optional and developed pending time and ultimately cost.

The selected features are driven by the opportunity matrix, which helps us understand what is both more important and viable to create. In this case all features mentioned below are implemented as the features made sense to provide in this initial release. Additional and future features are documented under the Features section, and not documented here.

A Trello Board was used to list the Use Cases and Features, and grew over time as new ideas were added inspired by the project development. In other words, not all these ideas came about before the project development began. An Agile methodology was applied throughout this project.

<details><summary>Please click to expand: Opportunity Matrix - User Management - Table and Scatter Diagram</summary>

![Opportunity Matrix - User Management - Table](documentation/OppMatrixTable-UserMgmnt.png)

![Opportunity Matrix - User Management - Scatter](documentation/OppMatrixScatter-UserMgmnt.png)

</details>

<details><summary>Please click to expand: Opportunity Matrix - Book Repository - Table and Scatter Diagram</summary>

![Opportunity Matrix - Book Repository - Table](documentation/OppMatrixTable-BookRepository.png)

![Opportunity Matrix - Book Repository - Scatter](documentation/OppMatrixScatter-BookRepository.png)

</details>

<details><summary>Please click to expand: Opportunity Matrix - Admin Dashboard - Table and Scatter Diagram</summary>

![Opportunity Matrix - Admin Dashboard - Table](documentation/OppMatrixTable-AdminDashboard.png)

![Opportunity Matrix - Admin Dashboard - Scatter](documentation/OppMatrixScatter-AdminDashboard.png)

</details>

<details><summary>Please click to expand: Opportunity Matrix - Shared Functions - Table and Scatter Diagram</summary>

![Opportunity Matrix - Shared Functions - Table](documentation/OppMatrixTable-SharedFunctions.png)

![Opportunity Matrix - Shared Functions - Scatter](documentation/OppMatrixScatter-SharedFunctions.png)

</details>

[Initial thoughts and plans for the Book Repository](https://github.com/NaoiseGaffney/BookRepository/wiki/Initial-Project-Design-Thoughts---have-since-changed-with-new-knowledge-and-skills.) The initial plan (scribbled on an A4) is similar to the end result in terms of user outcomes and high-level functions, however, it changed as I wrote things down on the Trello Board and researched some of the technology choices and their capabilities, as technical, functional, and skill contstraints emerged.

### User Stories, Use Cases, and Tasks Mapped to Information Architecture and Navigation
The User Experience links the Business goals of the external user and site owner to a number of user stories. A user story captures a description of a software feature from an end-user perspective. A user story describes the type of user, what they want and why. A use case is a list of actions or event steps describing the interactions between a role and a system to achieve a goal.

A user story has one or more use cases with one or more tasks with steps associated with it, describing how the user story, and subsequent fulfillment of the external user's and site owner's business goals are realised: Business Goals -> User Story -> Use Case(s) -> Task(s).

Information Architecture is sequential with modals, leading the user/reader along at every stage. The navigation bar provides a different set of options depending on the role (user or Admin), and whether authenticated or not. The breadcrumbs provide the "trodden path", making it easy to get back to where the user/reader started while also clarifying where they are (please note, once signed in, the Landing/Home Page redirects to the Member's Page). On pages with many books (Member's Page, Search Results Page) and many users/readers (Admin Page) pagination navigation is provided at the top of the book stack/user table to either select a page directly or go through them using the < (previous page) and (next page) >.

---

![Information Architecture and Navigation - User Management](documentation/IA%20Nav%20-%20User%20Management.png)

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

---

*  **User Story 002 (User/Reader):** as a user/reader I want the ability to manage my user profile so that I can have the best possible user/reader exeperience.
	*  **Use Case 002-001 (U in User CRUD):** as a user/reader I want to update my user profile.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on the user profile (username) on the navigation bar [Edit User Profile](https://book-repository-virtual.herokuapp.com/user/edit_user_profile) -> add/edit your First and Last Name, click on the Update button -> success Flash message and [Member's Page](https://book-repository-virtual.herokuapp.com/members).
	*  **Use Case 002-002 (U in User CRUD):** as a user/reader I want to change my password.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on the user profile (username) on the navigation bar [Edit User Profile](https://book-repository-virtual.herokuapp.com/user/edit_user_profile) -> click on [Change Password](https://book-repository-virtual.herokuapp.com/user/change-password) -> enter your current/old password, your new password, retype your new password for confirmation, and click on the Change Password button -> success Flash message and [Member's Page](https://book-repository-virtual.herokuapp.com/members).
		*  **Tasks 2:** an email is sent to the user's/reader's email address, confirming the password change -> if the password change wasn't initiated by the user/reader they can click on the link in the email to change the password.
	*  **Use Case 002-003 (D in User CRUD):** as a user/reader I want to delete my account.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> click on the user profile (username) on the navigation bar [Edit User Profile](https://book-repository-virtual.herokuapp.com/user/edit_user_profile) -> click on [Delete User](https://book-repository-virtual.herokuapp.com/user/edit_user_profile#delete_user) -> click on yes to permanetly delete the user/reader and associated books from the Book Repository or no to close the delete user modal -> success Flash message [Landing/Home Page](https://book-repository-virtual.herokuapp.com/index.html).

---

![Information Architecture and Navigation - Book Repository](documentation/IA%20Nav%20-%20Book%20Repository.png)

*  **User Story 003 (User/Reader):** as a user/reader I want to search for books in the Book Repository so that I can find new books to read, inspired by reader comments, and possibly purchase on Amazon UK or from other vendors.
	*  **Use Case 003-001 (R in Book CRUD):** as a user/reader I want to search for a specific book in my Book Repository using the ISBN.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> via the drop-down menu click on Search Books -> [Search Books](https://book-repository-virtual.herokuapp.com/search_book) -> enter the ISBN (9780141185378) of the book I'm searching for, toggle the private switch on (private search), and click on the Search Books button -> [Search Results](https://book-repository-virtual.herokuapp.com/search_results) -> Burmese Days by George Orwell -> Book CRUD operations apply as this is my book.
	*  **Use Case 003-002 (R in Book CRUD):** as a user/reader I want to search for books in my Book Repository using any combination of title, author, and rating (not genre, nor ISBN).
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> via the drop-down menu click on Search Books -> [Search Books](https://book-repository-virtual.herokuapp.com/search_book) -> enter any combination of title (empty, partial, or full), author (empty, partial, or full) of the book I'm searching for, toggle the private switch on (private search), rating (from 1 to 10, value searched for is >= value entered), and click on the Search Books button -> [Search Results](https://book-repository-virtual.herokuapp.com/search_results) -> stack (list) of books found -> Book CRUD operations apply as these are my books.
	*  **Use Case 003-003 (R in Book CRUD):** as a user/reader I want to search for all my books in my Book Repository using an empty form search.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> via the drop-down menu click on Search Books -> [Search Books](https://book-repository-virtual.herokuapp.com/search_book) -> leave all form fields empty, toggle the private switch on (private search), and click on the Search Books button -> [Search Results](https://book-repository-virtual.herokuapp.com/search_results) -> stack (list) of books found (same result as my Book Stack in my Member's Page) -> Book CRUD operations apply as these are my books
	*  **Use Case 003-004 (R in Book CRUD):** as a user/reader I want to search for a specific book the Book Repository using the ISBN.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> via the drop-down menu click on Search Books -> [Search Books](https://book-repository-virtual.herokuapp.com/search_book) -> enter the ISBN (9780141185378) of the book I'm searching for, leave the toggle switch off (public search), and click on the Search Books button -> [Search Results](https://book-repository-virtual.herokuapp.com/search_results) -> Burmese Days by George Orwell (if the book isn't marked as private/hidden by users/readers) -> Book CRUD operations apply as this is my book, otherwise only R in Book CRUD as the book belongs to someone else.
	*  **Use Case 003-005 (R in Book CRUD):** as a user/reader I want to search for books in the Book Repository using any combination of title, author, and rating (not genre, nor ISBN).
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> via the drop-down menu click on Search Books -> [Search Books](https://book-repository-virtual.herokuapp.com/search_book) -> enter any combination of title (empty, partial, or full), author (empty, partial, or full) of the book I'm searching for, leave the toggle switch off (public search), rating (from 1 to 10, value searched for is >= value entered), and click on the Search Books button -> [Search Results](https://book-repository-virtual.herokuapp.com/search_results) -> stack (list) of books found that are not  marked as private/hidden by users/readers -> Book CRUD operations apply to my books, only R in Book CRUD for books belonging to other users/readers.
	*  **Use Case 003-006 (R in Book CRUD):** as a user/reader I want to search for all the books in the Book Repository using an empty form search.
		*  **Tasks 1:** [Member's Page](https://book-repository-virtual.herokuapp.com/members) -> via the drop-down menu click on Search Books -> [Search Books](https://book-repository-virtual.herokuapp.com/search_book) -> leave all form fields empty, leave the toggle switch off (public search), and click on the Search Books button -> [Search Results](https://book-repository-virtual.herokuapp.com/search_results) -> stack (list) of books found that are not  marked as private/hidden by users/readers -> Book CRUD operations apply to my books, only R in Book CRUD for books belonging to other users/readers.

---

![Information Architecture and Navigation - Admin Dashboard](documentation/IA%20Nav%20-%20Admin%20Dashboard.png)

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

![Section Divider: Title and Business](documentation/section%20divider.png)

## Design Decisions
The design decisions cover the look-and-feel, typography, colour scheme, forms, buttons, navigation elements, tooltips and more. They put "lipstick-on-the-pig", in other words make the Book Repository application appealing to and easy-to-use for a user/reader. They make the functions come alive and provide information and interaction with the user/reader.

### Design Decisions Overview
Flask-User uses Bootstrap-3 by defualt, a CSS Framework, I've opted for [Materialize 1.0.0](https://materializecss.com/) instead as it provides a clean, crisp look and is based on principles of Material Design. While there is a Flask extension called Flask-Materialize, it's based on a previous version of Materialize and doesn't offer the same stable features as a result, nor is it as flexible as using Materialize in this way. It also means that JavaScript is used to initialise the features, and doesn't rely on jQuery which improves performance, and jQuery doesn't need to be loaded.

[Material Icons](https://material.io/resources/icons/?style=baseline) are used too, for their clean, crisp look. They work well together with the CSS Framework Materialize 1.0.0.

The Forms and Fields follow the same look-and-feel consistenly across the Book Repository. The base is Materialize 1.0.0, the icons used are Material Icons, each field has a descriptive label that moves out-of-the-way when the field is selected, and each icon has a hover-tooltip to explain the field's purpose.

The colour scheme has changed over time to provide improved contrast and user feedback. As a general rule the main colours are blue darken-4 and white, used interchangeably to good effect. Teal lighten-1 is used for success messages and views, pink darken-1 is used for failure and delete, and charcoal is used for information.

The buttons are white text on blue darken-4 with icons to the right to provide a clear visual clue and reminder. In one instance the button is pink darken-1 with white text (Delete User in the Admin User Modal). The hamburger-menu for mobile devices has the icons on the left as it looks better than having them on the right of the text.

Flash Messages use the colour scheme to provide additional insights as to the success or failure of the attempted function. Teal lighten-1 for success, pink darken-1 for failure, and charcoal for information.

Text is either white (on blue darken-4), black, blue darken-4 (on white or background), or pink darken-1, depending on function. The text colour decisions were made over time based on the style of the surrounding components.

Error Handlers are displayed on the 'oops.html' page, the title is in pink darken-1, the text in black on a Materialize Card with a burning book image (following the Book Repository book theme).

### Interface and Navigation Design
* Information Architecture is sequential with modals, leading the user/reader along at every stage. The navigation bar provides a different set of options depending on the role (user or Admin), and whether authenticated or not.
* Breadcrumbs provide a clear view of where the user/reader is, and has been, with the option to click on any breadcrumb to go back to a previous page (please note, once signed in, the Landing/Home Page redirects to the Member's Page).
* Pagination is provided in the Member's Page and Search Results if 8 books or more exist. The pagination navigation is placed at the top of the book stack for ease-of-use. 
* The Book Repository emails for user/reader registration, password change, and password reset all provide ample explanations on what to do and why (click on the email link).
* Help tooltips (hover) and form field tooltips (hover) exist for every page and form, aiding the user/reader in understanding and using the Book Repository.
* Flash messages provide instant user/reader feedback on either the success or failure of a task (sign in, sign  out, register, update profile, change or reset password, add book, update book, delete book, and incorrect form field entries). The same Flash message feedback is used for the Admin Dashboard too, to aid an admin in using the existing features without having to read documentation or resort to trial-and-error.
* All from fields provide immediate user/reader feedback too, when selecting an empty field, when entering an incorrect entry, and when a required entry is needed (notable exception is the Admin Dashboard User Modal where some of the authentication is performed in 'app.py').
* All buttons (form buttons and navigation bar) combine text and icon consistently to aid in the function recognition and use. For all form fields the icon is to the left of the field. For all buttons the icon is on the right of the text. The navigation bar has the icons on the right of the text, except for the hamburger-menu where the icons are on the left of the text as it looks nicer from a layout perspective.
* Responsive Web Design: the Book Repository works across all devices and screen sizes. In fact, it looks somewhat better on mobile device than on the desktop if anything.
* The colour scheme has changed over the course of the project, aiming to provide a clear and clean user interface with a good contrast.
* The font used throughout the Book Repository is Raleway, provided by Google Fonts. It's an easy-to-read font on all device/screen sizes and is comfortable to read over long periods of time.
* The 4 error handlers handle the unfortunate incidents where a user/reader goes astray, or an internal issue has occured. The error handlers provide a means to get back to the Member's Page or Sign Out, as well as an apology for the incident and an explanation of what has occured and potentially why.
* The Book Repository logo is easily recognisable and simple in its design. It's a stack of books with the text, "Book Repository".

### Design Details
This section describes the visual components in detail, and with examples, to clarify their design and purpose.

#### Typography
![Book Repository Typgraphy: Raleway Font](documentation/Raleway%20Font.png)

[Google Fonts: Raleway](https://fonts.google.com/specimen/Raleway#standard-styles)

The font used throughout the Book Repository is Raleway, provided by Google Fonts. It's an easy-to-read font on all device/screen sizes and is comfortable to read over long periods of time.

#### Colour Scheme
![Book Repository Final Colour Scheme](documentation/Book%20Repository%20-%20Colour%20Scheme%20-%20README.png)

[Coolors Colour Scheme](https://coolors.co/0d47a1-26a69a-d81b60-ffffff-37474f)

The colour scheme has changed over the course of the project, aiming to provide a clear and clean user interface with a good contrast.

| Function                                 | Coolors                      | Materialize        | Sample                                 | Use                                                                                                                                                                                          |
|------------------------------------------|------------------------------|--------------------|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Logo                                     | Cobalt Blue #0D47A1          | blue darken-4      | ![Cobalt Blue](documentation/cobalt%20blue.png) | Logo.                                                                                                                                                                                        |
| Primary and  Background Colour (reverse) | Cobalt Blue #0D47A1          | blue darken-4      | ![Cobalt Blue](documentation/cobalt%20blue.png) | Together with white and black in some cases - button and navigation bar background, secondary button text over white background, active form field icons and labels, links, active elements. |
| Secondary and Font Colour (reverse)      | White #FFFFFF                | white              | ![Cobalt Blue](documentation/white.png) | Together with blue - button and navigation bar text and icons, secondary button background over blue background.                                                                             |
| Tertiary Colour                          | Dark Cornflower Blue #0C4091 | no equivalent      | ![Cobalt Blue](documentation/dark%20cornflower%20blue.png) | Toggle switch on, background colour.                                                                                                                                                         |
| Quaternary Colour                        | Black #000000                | black              | ![Cobalt Blue](documentation/black.png) | Most text is black, form field, book details, and table text.                                                                                                                                |
| Accent Colour 1                          | Ruby #D81B60                 | pink darken-1      | ![Cobalt Blue](documentation/ruby.png) | Flash message failure, delete book, delete user.                                                                                                                                             |
| Accent Colour 2                          | Persian Green #26A69A        | teal lighten-1     | ![Cobalt Blue](documentation/persian%20green.png) | Flash message success, view book.                                                                                                                                                            |
| Accent Colour 3                          | Charcoal #37474F             | blue-grey darken-3 | ![Cobalt Blue](documentation/charcoal.png) | Flash message info.                                                                                                                                                                          |

#### Buttons
The buttons are consistent in style and instantly recognisable with both text and icons making it easier for users/readers to understand and recognise their purpose. Text uses the Raleway font, and the icons are [Material Icons](https://material.io/resources/icons/?style=baseline).

![Buttons - Primary](documentation/Buttons%20-%20Primary.png)

All buttons are styled the same, with capitalised text on the left and an icon on the right. Primary buttons have a "blue darken-4" background with white text and icon, except for the Delete (Delete User) button in the Admin Dahsboard User Modal as it doesn't have a "Are you sure you wish to do this?" feature.

![Buttons - Secondary (drop-down)](documentation/Buttons%20-%20Secondary%20(drop-down).png)

The seceondary, drop-down menu buttons have a white background with "blue darken-4" text on the left and icon on the right.

#### Navigation Bar
The Navigation Bar is styled the same way as the primary buttons, with white text on the left and icon on the right on a "blue darken-4" background. The Navigation Bar is controlled by the Jinja template 'flask_user_layout.html' where if-else statements check whether the user/reader is authenticated or not, and whether the user is authenticated and has the role of Admin.

![Navigation Bar Unauthenticated](documentation/Unauthenticated%20-%20NavBar.png)

Navigation Bar when unauthenticated.

![Navigation Bar Authenticated User/Reader](documentation/User%20Authenticated%20-%20NavBar.png)

Navigation Bar when authenticated as a user/reader.

![Navigation Bar Authenticated Admin](documentation/Admin%20Authenticated%20-%20NavBar.png)

Navigation Bar when authenticated as an Admin.

The hamburger Bar is styled the same way as the primary buttons, however, the white text is on the right and icon on the left on a "blue darken-4" background as it looks nicer from a layout perspective. The Hamburger Bar is controlled by the Jinja template 'flask_user_layout.html' where if-else statements check whether the user/reader is authenticated or not, and whether the user is authenticated and has the role of Admin.

![Hamburger Bar Unauthenticated](documentation/Unauthenticated%20-%20HBar.png)

Hamburger Bar when unauthenticated.

![Hamburger Bar Authenticated User/Reader](documentation/Authenticated%20User%20-%20HBar.png)

Hamburger Bar when authenticated as a user/reader.

![Hamburger Bar Authenticated Admin](documentation/Authenticated%20Admin%20-%20HBar.png)

Hamburger Bar when authenticated as an Admin.

#### Fixed Footer
![Fixed Footer](documentation/Fixed%20Footer.png)
The fixed footer has grey text and a white icon on a blue darken-4 background. The text is provided by two Flask-User variables defined in 'config.py'.

![Fixed Footer - About Modal](documentation/About%20Modal.png)
The About Modal contains short descriptions on the purpose of the Book Repository, my "ego-page", and a code overview with a link to the GitHub Repository.

#### Background Image
![Stack of Books on the rigth-hand side by Sharon McCutcheon on Unsplash](static/images/sharon-mccutcheon-eMP4sYPJ9x0-unsplash.jpg)

[Sharon McCutcheon - Photographer](https://unsplash.com/@sharonmccutcheon?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)

The background image, a stack of books, photographed by Sharon McCutcheon on Unsplash is the perfect shade of blue-white with the books off-centre and to the right which means they are not interfering with the book stack and book details. It's also suitable as it has a stack of books, the Book Repository logo is a stack of books, and the user's/reader's stack of books are viewed on the Member's Page.

#### Flash Messages
Flash messages provide immediate user feedback on either the success or failure of a function (sign in, sign out, add book, and more). Teal lighten-1 for success, pink darken-1 for failure, and charcoal for information.

![Flash Message - Success](documentation/FlashMessageSuccess.png)

![Flash Message - Information](documentation/FlashMessageInfo.png)

![Flash Message - Failure](documentation/FlashMessageFailure.png)

#### Tooltips
Tooltip messages, on hover over the help (? icon) and icons, are white text on charcoal background (good contrast, easy to read).

![Tooltip Help](documentation/TooltipOnHoverHelp.png)

#### Breadcrumbs
Breadcrumbs provide a path for the user/reader to follow, letting them know where they've been, where they are, and an ability to get back to a previous page.

I had three options in creating the breadcrumbs. Programatically, using Flask-Breadcrumbs (additional overhead), Materialize 1.0.0 (styling), or create my own in HTML. I opted for the latter as it was the easiest choice, easiest to implement.

![Breadcrumbs](documentation/Breadcrumbs.png)

#### Pagination
Pagination allows for the browsing of pages when there are too many books (Member's Page and Search Results Page) or users (Admin Dashboard table) to display on a single page.

A user/reader/admin can navigate back and forth using the < and >, or by clicking on a page number. The current/active page number is in white text on a blue darken-4 square.

In the case of too many pages, and ellipsis is used which makes it suitable for smaller screens/devices.

The pagination function is a part of Flask-MongoEngine, and rendered in Jinja2 using a macro.

![Pagination](documentation/Pagination.png)

#### Logo
The Book Repository logo is easily recognisable and simple in its design. It's a stack of books with the text, "Book Repository".

The Book Repository logo is created in Microsoft PowerPoint, using a stock logo of stacked books with the text, "Book Repository". It matches the colour scheme, using the colour blue darken-4.

![Book Repository - Logo](static/images/logo_bookstack_text_96_spacing.png)

#### Favicon
The Favicon is the stack of books without the text from the Book Repository Logo.

![Favicon](static/images/android-chrome-192x192.png)

[Favicon.io Favicon Generator](https://favicon.io/) was used to create the Favicon.

#### Book Stack
The Member's Page and Search Results Page book stack displays virtual book spines. Once clicked on to view it pop-outs to display book details.

The book spine has 3 small icons, teal eye to view the book details, pink bin link to delete a book, and blue pen link to update the book details. The title links to Amazon UK using ISBN, the ISBN link liinks to ISBN Search using ISBN, and the front cover thumbnail uses ISBN to get it from the Google Books API.

![Book Stack](documentation/BookStack.png)

#### Tables
Tables are an effective way to display and work with large amounts of similar data. List Genres uses a table or the book genres and their descriptions, Admin Dashboard user table is good for when the site grows with many users, and the Statistics Modal uses a table to display the book genres used and their numbers.

![List Genres Table](documentation/ListGenresTable.png)

![Section Divider: User Experience and Features](documentation/section%20divider.png)

## Features
A feature is some action that can be performed by a user of an application, or is some internal function of an application. The features support the User Experience mentioned above and are implemented based on the business goals, user stories and use cases.

The features are divided into 4 main areas, User Management, Book Repository (the main book and library features), Admin Dashboard, and Shared Features.

![Book Repository - Context/Container C4 Diagram](out/documentation/book_repository_container/book_repository_container.png)

### Existing Features
Features currrently implemented as a part of the Book Repository.

#### User Management:

* Flask-User extension with:
	* User/reader registration with email confirmation (C is User CRUD).
	* User/reader sign in after registration (R in User CRUD).
	* User/reader password reset with email confirmation.
	* User/reader user profile update, with first and last name, and password change (U in User CRUD).
	* User/reader sign out.
* Added user/reader delete user/reader modal to Flask-User user profile update (D in User CRUD).

#### Book Repository:

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
	* The ability to search for books using a combinaition to title (partial or full) and author (partial or full), rating equal to or greater than, and genre (none or 1 of 32).
* Search Books Results with:
	* The ability to browse and view books matching the search criteria.
	* The ability to edit/update books belonging to the current user/reader (books belonging to other users/readers can't be edited/updated, nor deleted).

#### Admin Dashboard:

* Admin Page with:
	* User Management table, User, Full Name, Active, E-mail.
		* User modal to update user details, set user to active/inactive, and permanently deleter the user/reader and associated books (RUD in User CRUD).
		* Load Genres via the drop-down menu in case the genres collection wasn't created by the first access to the Landind Page or was accidentally deleted  (C in Book Genre CRUD).
		* Load Books via the drop-down menu to load a sample of 28 books to populate the Book Repository and use for testing purposes (C in Book CRUD).
		* List Genres, to view the 32 genres and their description. Future feature to add, update, and delete genres here (R in Book Genre CRUD).
		* Book Repository Statistics via the drop-down menu to vie the number of users, number of books, and number of books in each genre (R in Statistics CRUD).

#### Shared Features:

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

### Future Features
Future features are planned features that didn't make it into this first release due to time, effort, current knowledge and skills constraints (I know it can be done, I haven't yet figured out how).

#### User Management:

* Username update by user/reader under update user profile, with automatic update of books belonging to the user/reader.

#### Book Repository:

* Validate ISBN using Python extension isbnlib when books are added and updated.
* Support for ISBN with the check digit of 'X'.
* Get full Google Books API details when adding and updating books.
* Support for multiple languages using Flask-BabelEx (i18n/i10n).
* Shared book comments.
* User/reader messaging/message board.

#### Admin Dashboard:

* User 'admin' can activate/revoke Admin role in the Admin Dashboard User Modal to share the administrative responsibilities when the site grows.
* Number of books per user/reader and genre breakdown per user/reader.
* Username update with book updates of new username.
* Save and load several book JSON files.
* Undo delete of user/reader and books (within 5 days, placing all deleted items in a separate collection(s)).
* Create user/reader without the user/reader having to register via the register page.
* Update, add, delete genres in the genres collection.
* Application Log view in the Admin Dashboard, primarily to view rogue users/readers and to revoke their access to the Book Repository.

#### Shared Features
* Implement [Flask-Paranoid](https://flask-paranoid.readthedocs.io/en/latest/) to protect against stolen user session cookies (Flask-Login 'SESSION_PROTECTION = "strong"' when "Remember Me" is enabled isn't enough).

### Information and Visual Design

![Book Search 1: Book Search: private (user books) and ISBN ](documentation/Book%20Search%201.png)

![Book search 2: Book Search: private (user books) and title, and author, and gte rating, and not genre](documentation/Book%20Search%202.png)

![Book Search 3: Book Search: private (user books) and title, and author, and gte rating,  and genre](documentation/Book%20Search%203.png)

![Book Search 4: Book Search: public (all books, except hidden) and ISBN ](documentation/Book%20Search%204.png)

![Book Search 5: Book Search: public (all books, except hidden) and title, and author, and gte rating, and not genre](documentation/Book%20Search%205.png)

![Book Search 6: Book Search: public (all books, except hidden) and title, and author, and gte rating, and genre](documentation/Book%20Search%206.png)

#### Wireframes and Visuals
The initial wireframe diagram describes the first draft of the Book Repository. Further research and education formed the next release of the Book Repository, the wireframe diagrams below. The Book Reposiory changed over time, as increased knowledge and improved skills were gained, and as the development inspired further improvements.

Trying to come up with all the features up-front leads either to "Paralysis by analysis" or a  severly limited list of features not likely to satisfy any client requirements and needs. The backlog developed over time after each iteration inspired further items to be added to the backlog as the undersanding of the next feature or function to staisfy the overall requirements became clear.

##### Initial Wireframe Diagram of the Book Repository

<details><summary>Please click to expand: Landing / Home Page</summary>

![Wireframe: Initial Wireframe Diagram of the Book Repository](documentation/Initial%20thoughts%20for%20Book%20Repository.jpg)

</details>

##### Landing / Home Page

<details><summary>Please click to expand: Landing / Home Page</summary>

[Link: Landing / Home Page](https://book-repository-virtual.herokuapp.com/)

![Wireframe: Landing / Home Page](documentation/Book%20Repository/Landing%20Home%20Page.png)

![Visual: Landing / Home Page](documentation/Book%20Repository/V%20-%20Landing%20and%20Home%20Page.png)

</details>

##### Register Page

<details><summary>Please click to expand: Register Page</summary>

[Link: Register Page](https://book-repository-virtual.herokuapp.com/user/register)

![Wireframe: Register Page](documentation/Book%20Repository/Register.png)

![Visual: Register Page](documentation/Book%20Repository/V%20-%20Register%20Page.png)

</details>

##### Sign In

<details><summary>Please click to expand: Sign In Page</summary>

![Wireframe: Sign In](documentation/Book%20Repository/Sign%20In.png)

![Visual: Sign In](documentation/Book%20Repository/V%20-%20Sign%20In.png)

</details>

##### Member's Page

<details><summary>Please click to expand: Member's Page</summary>

![Wireframe: Member's Page](documentation/Book%20Repository/Member's%20Page.png)

![Visual: Member's Page](documentation/Book%20Repository/V%20-%20Members%20Page.png)

</details>

##### Admin Dashboard

<details><summary>Please click to expand: Admin Dashboard</summary>

![Wireframe: Admin Dashboard](documentation/Book%20Repository/Admin%20Page.png)

![Visual: Admin Dashboard](documentation/Book%20Repository/V%20-%20Admin%20Dashboard.png)

</details>

### Features CRUD Table (Views)
This table is an overview of the CRUD functions for each feature or role or MongoDB collection. It describes the implemented features, the future features, possible future features, and features that are not planned to be implemented. The notes describe where the feature is implemented in the Book Repository.

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

### Application Logging and Flash Messaging Levels
Application logging is key to gather application usage for statistics and planning, for security reasons to detect potential attempts at disrupting the site, for performance planning as the site grows (increased usage and conversion rates) to ensure the use of the Book Repository is always a pleasant exeperience, and for root-cause and impact-analysis in the event of critical issues disrupting the end-user experience.

Flash messaging keeps the users/readers informed (success, info, failure) through continuous feedback as they use the features of the Book Repository.

Python default logging is used, and additional information is attached to the log message to fulfil the above-mentioned application logging requirements. In future the Admin Dashboard will filter application log messages by user/reader, endpoint/function, and severity.

Local development uses a rotating file handler which makes the logs easier to read (colour-coded) and search as they are saved to files. Heroku places constraints on logging, prefering the use of the exisitng application log and paid for logging tools.

| Logger   | Flash   | Message       | Environments                                                 | Notes                                                                                                                                                    |
|----------|---------|---------------|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Notset   |         |               |                                                              |                                                                                                                                                          |
| Debug    |         |               | Local Development, Heroku Review Application, Heroku Staging | Local development = Flask Debug Toolbar. Heroku Review Application and Heroku Staging = Application Console.                                             |
| Info     | Success | Success, Info |                                                              | Application Log (rotating file logger and console) = Info. Flash Message = Success (teal). Book Repository Message in Application Log = Success or Info. |
| Warning  |         | Warning       |                                                              | Application Log (rotating file logger and console) = Warning. Book Repository Message in Application Log = Warning.                                      |
| Error    |         |               |                                                              |                                                                                                                                                          |
| Critical | Danger  | Failure       | Heroku Production                                            | Application Log (rotating file logger and console) = Critical. Flash Message = Danger (pink). Book Repository Message in Application Log = Failure.      |

### Book Repository '.env' and Heroku Variables
These variables are required for the Book Repository functions, such as register confirmation and password reset emails. Some are shared (the same) across all four environments, while some are unique to each environment (for example, the `MONGO_URI_BR` which is the MongoDB URI for each instance).

| Variables               | Local  | Heroku Review App | Heroku Staging | Heroku Production | Description                                                                                                                          |
|-------------------------|--------|-------------------|----------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| `ADMIN_PASSWORD`          | Unique | Unique            | Unique         | Unique            | User 'admin' password used when   creating the 'admin' user on first Home/Landing Page access.                                       |
| `GOOGLE_API_KEY`          | Shared | Shared            | Shared         | Shared            | Used for the Google Books API to   request the front cover thumbmnail for the book searched using ISBN.                              |
| `LOGGING_LEVEL`           | Unique | Unique            | Unique         | Unique            | Application log level, for   rotating file log handler and the application log to console.                                           |
| `MAIL_DEFAULT_SENDER`     | Shared | Shared            | Shared         | Shared            | Flask-User/Mail 'from' email   address for the registration and password reset confirmation emails.                                  |
| `MAIL_PASSWORD`           | Shared | Shared            | Shared         | Shared            | Flask-User/Mail password for the   registration and password reset confirmation emails.                                              |
| `MAIL_PORT`              | Shared | Shared            | Shared         | Shared            | Flask-User/Mail port for either   TLS or SSL (in this case TLS) for the registration and password reset   confirmation emails.       |
| `MAIL_SERVER`             | Shared | Shared            | Shared         | Shared            | Flask-User/Mail server name for   the registration and password reset confirmation emails.                                           |
| `MAIL_USERNAME`           | Shared | Shared            | Shared         | Shared            | Flask-User/Mail username for the   registration and password reset confirmation emails.                                              |
| `MONGO_URI_BR`            | Unique | Unique            | Unique         | Unique            | MongoDB URI for each Book   Repository instance (Dev, Rev, Staging, Production).                                                     |
| `SECRET_KEY`              | Unique | Unique            | Unique         | Unique            | Secret Key for Flask encryption.                                                                                                     |
| `USER_EMAIL_SENDER_EMAIL` | Shared | Shared            | Shared         | Shared            | Flask-User/Mail 'from' email   address for the registration and password reset confirmation emails.                                  |
| `PRODUCTION`              |        |                   |                | On                  | Heroku Production variable to   disable all debugging.                                                                               |
| `FDT`                     | Unique |                   |                |                   | Flask Debug Toolbar varibale to   ensure it only runs in local development environment as it contains   clear-text config variables. |

### Flask-User and Book Repository Routes
These routes are either a part of the Flask-User extension or created as a part of the Book Repository. The "y", "n", and "" under each heading (Flask User, Book Repo, User / Reader, Admin) denote the following: "y" = is either implemented by (Flask User or Book Repo) or used by (User/Reader or Admin), "n" = is either implemented by but not used (Flask User or Book Repo) nor used by (User/Reader or Admin), "" = is not implemented by (Flask User or Book Repo) nor used by (User/Reader or Admin).

For example, Flask-User implements user.invite_user, though isn't activated through 'config.py' configuration parameters which is why it's marked as "n".

| URL   route                     | Endpoint name                  | HTTP methods             | Flask User | Book Repo | User / Reader | Admin |
|---------------------------------|--------------------------------|--------------------------|------------|-----------------|-------------|-------|
| `/`                               | `home_page`                      | GET, HEAD, OPTIONS       |            | y               | y           | y     |
| `/add_book`                       | `add_book`                       | GET, HEAD, OPTIONS       |            | y               | y           | y     |
| `/admin_dashboard`                | `admin_dashboard`                | GET, HEAD, OPTIONS       |            | y               |             | y     |
| `/admin_dashboard/<int:page>`     | `admin_dashboard`                | GET, HEAD, OPTIONS       |            | y               |             | y     |
| `/admin_delete_user/<user_id>`    | `admin_delete_user`              | GET, HEAD, OPTIONS       |            | y               |             | y     |
| `/delete_book/<book_id>`          | `delete_book`                    | GET, HEAD, OPTIONS       |            | y               | y           | y     |
| `/delete_user`                    | `delete_user`                    | GET, HEAD, OPTIONS       |            | y               | y           | y     |
| `/edit_book/<book_id>`            | `edit_book`                      | GET, HEAD, OPTIONS       |            | y               | y           | y     |
| `/index`                          | `home_page`                      | GET, HEAD, OPTIONS       |            | y               | y           | y     |
| `/index.html`                     | `home_page`                      | GET, HEAD, OPTIONS       |            | y               | y           | y     |
| `/load_books`                     | `load_books`                     | GET, HEAD, OPTIONS       |            | y               |             | y     |
| `/load_genres`                    | `load_genres`                    | GET, HEAD, OPTIONS       |            | y               |             | y     |
| `/members`                        | `member_page`                    | GET, HEAD, OPTIONS       |            | y               | y           | y     |
| `/members/<int:page>`             | `member_page`                    | GET, HEAD, OPTIONS       |            | y               | y           | y     |
| `/save_book`                      | `save_book`                      | OPTIONS, POST            |            | y               | y           | y     |
| `/save_search`                    | `save_search`                    | GET, HEAD, OPTIONS, POST |            | y               | y           | y     |
| `/search_book`                    | `search_book`                    | GET, HEAD, OPTIONS       |            | y               | y           | y     |
| `/search_results`                 | `search_results`                 | GET, HEAD, OPTIONS, POST |            | y               | y           | y     |
| `/search_results/<int:page>`      | `search_results`                 | GET, HEAD, OPTIONS       |            | y               | y           | y     |
| `/static/<path:filename>`         | `static`                         | GET, HEAD, OPTIONS       | y          |                 | y           | y     |
| `/update_book/<book_id>`          | `update_book`                    | OPTIONS, POST            |            | y               | y           | y     |
| `/update_user/<user_id>`          | `update_user`                    | OPTIONS, POST            |            | y               | y           | y     |
| `/user/change-password`           | `user.change_password`           | GET, HEAD, OPTIONS, POST | y          |                 | y           | y     |
| `/user/change-username`           | `user.change_username`           | GET, HEAD, OPTIONS, POST | n          |                 | n           | n     |
| `/user/confirm-email/<token>`     | `user.confirm_email`             | GET, HEAD, OPTIONS       | y          |                 | y           | y     |
| `/user/edit_user_profile`         | `user.edit_user_profile`         | GET, HEAD, OPTIONS, POST | y          |                 | y           | y     |
| `/user/email/<id>/<action>`       | `user.email_action`              | GET, HEAD, OPTIONS       | y          |                 | y           | y     |
| `/user/forgot-password`           | `user.forgot_password`           | GET, HEAD, OPTIONS, POST | y          |                 | y           | y     |
| `/user/invite`                    | `user.invite_user`               | GET, HEAD, OPTIONS, POST | n          |                 |             |       |
| `/user/manage-emails`             | `user.manage_emails`             | GET, HEAD, OPTIONS, POST | n          |                 |             |       |
| `/user/register`                  | `user.register`                  | GET, HEAD, OPTIONS, POST | y          |                 | y           | y     |
| `/user/resend-email-confirmation` | `user.resend_email_confirmation` | GET, HEAD, OPTIONS, POST | y          |                 | y           | y     |
| `/user/reset-password/<token>`    | `user.reset_password`            | GET, HEAD, OPTIONS, POST | y          |                 | y           | y     |
| `/user/sign-in`                   | `user.login`                     | GET, HEAD, OPTIONS, POST | y          |                 | y           | y     |
| `/user/sign-out`                  | `user.logout`                    | GET, HEAD, OPTIONS, POST | y          |                 | y           | y     |

### Flask, Flask-User, and Book Repository Configuration Variables
| Key                           | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `APPLICATION_ROOT`              | '/'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `DEBUG`                         | TRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `DEBUG_TB_ENABLED`              | TRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `DEBUG_TB_HOSTS`                | ()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `DEBUG_TB_INTERCEPT_REDIRECTS`  | TRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `DEBUG_TB_PANELS`               | ('flask_debugtoolbar.panels.versions.VersionDebugPanel',   'flask_debugtoolbar.panels.timer.TimerDebugPanel',   'flask_debugtoolbar.panels.headers.HeaderDebugPanel',   'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',   'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',   'flask_debugtoolbar.panels.template.TemplateDebugPanel',   'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',   'flask_debugtoolbar.panels.logger.LoggingPanel',   'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',   'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel') |
| `ENV`                           | 'production'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `EXPLAIN_TEMPLATE_LOADING`      | FALSE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `JSON_AS_ASCII`                 | TRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `JSON_SORT_KEYS`                | TRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `JSONIFY_MIMETYPE`              | 'application/json'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `JSONIFY_PRETTYPRINT_REGULAR`   | FALSE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `MAIL_PASSWORD`                 | '**********************'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `MAIL_PORT`                     | '587'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `MAIL_SERVER`                   | 'smtp.gmail.com'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `MAIL_USE_SSL`                  | FALSE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `MAIL_USE_TLS`                  | TRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `MAIL_USERNAME`                 | '**********************'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `MAX_CONTENT_LENGTH`            | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `MAX_COOKIE_SIZE`               | 4093                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `MONGO_DB_URL`                  | 'mongodb+srv://mdb_c_root:**********************/BookRepositoryDev?retryWrites=true&w=majority'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `MONGODB_SETTINGS`              | {'host':   'mongodb+srv://mdb_c_root:**********************/BookRepositoryDev?retryWrites=true&w=majority'}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `PERMANENT_SESSION_LIFETIME`    | datetime.timedelta(seconds=3600)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `PREFERRED_URL_SCHEME`          | 'http'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `PRESERVE_CONTEXT_ON_EXCEPTION` | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `PROPAGATE_EXCEPTIONS`          | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `REMEMBER_COOKIE_DURATION`      | datetime.timedelta(seconds=3600)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `SECRET_KEY`                    | '**********************'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `SEND_FILE_MAX_AGE_DEFAULT`     | datetime.timedelta(seconds=43200)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `SERVER_NAME`                   | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `SESSION_COOKIE_DOMAIN`         | FALSE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `SESSION_COOKIE_HTTPONLY`       | TRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `SESSION_COOKIE_NAME`           | 'session'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `SESSION_COOKIE_PATH`           | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `SESSION_COOKIE_SAMESITE`       | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `SESSION_COOKIE_SECURE`         | TRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `SESSION_PROTECTION`            | 'strong'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `SESSION_REFRESH_EACH_REQUEST`  | TRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `TEMPLATES_AUTO_RELOAD`         | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `TESTING`                       | FALSE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `TRAP_BAD_REQUEST_ERRORS`       | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `TRAP_HTTP_EXCEPTIONS`          | FALSE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `USE_X_SENDFILE`                | FALSE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `USER_APP_NAME`                 | 'Book Repository'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `USER_COPYRIGHT_YEAR`           | 2020                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `USER_CORPORATION_NAME`         | 'GaffCo Consulting'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `USER_EMAIL_SENDER_EMAIL`       | '**********************'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `USER_ENABLE_CHANGE_USERNAME`   | FALSE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `USER_ENABLE_EMAIL`             | TRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `USER_ENABLE_USERNAME`          | TRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `USER_REQUIRE_RETYPE_PASSWORD`  | TRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `WTF_CSRF_CHECK_DEFAULT`        | TRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `WTF_CSRF_ENABLED`              | TRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `WTF_CSRF_FIELD_NAME`           | 'csrf_token'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `WTF_CSRF_HEADERS`              | ['X-CSRFToken',   'X-CSRF-Token']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `WTF_CSRF_METHODS`              | {'PUT', 'POST', 'DELETE',   'PATCH'}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `WTF_CSRF_SSL_STRICT`           | TRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `WTF_CSRF_TIME_LIMIT`           | 3600                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

![Section Divider: Features and Design Decisions and Technology Choices](documentation/section%20divider.png)

## Technology

### Technology Choices
Flask-User, application logging, CSRF, FDT, Flask-MongoEngine/MongoEngine, File Handling (JSON), Google Books API (thumbnail images), Session Cookies, Consent Cookie, 'config.py', .env and Heroku variables, CDD, DB Schema, JSON Schema...

### Code

Defensive Programming...

### Development and Staging Platforms and Environments

### Documentation Tools

### Acknowledgements and Attributions of Used Features and Functions

### General Knowledge and Hours of Reading

![Section Divider: Technology and, Testing and Validation](documentation/section%20divider.png)

## Testing and Validation
### Manual BDD

### Automated BDD

### Testing Notes

### Validation of HTML 5, CSS 3, JS and Python

![Section Divider: Testing and Validation, and Continuous Delivery and Deployment](documentation/section%20divider.png)

## Continuous Delivery and Deployment

![Section Divider: Continuous Delivery and Deployment, and Credits](documentation/section%20divider.png)

## Credits
![GaffCo Consulting Logo](documentation/GaffCo%20-%20Background.png)

GaffCo Consulting - [Naoise Gaffney: naoise.gaff.gaffney@gmail.com](mailto:naoise.gaff.gaffney@gmail.com)

![Code Institute Logo](documentation/CodeInstituteLogo.png)

Code Institute Mentor - [GitHub: 5pence - Spencer Barriball](https://github.com/5pence)

### Content

### Media

### Acknowledgements

The Diploma in Full Stack Development provides a great foundation of tools and technologies used to work as a professional developer. It's a case of being a Jack-of-All-Trades, and a Master of None (or Some). It's up to each developer to expand upon the knowledge and skills acquired during the course through additional self-study of elements covered as a part of the course as well as other frameworks, languages, tools, methodologies,  processes, and solutions.

Thank you Code Institute for allowing me on this journey in life!

Thank you Spencer Barriball for your unwavering support!

