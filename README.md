# Book Repository

![Initial Thoughts for the Book Repository](https://github.com/NaoiseGaffney/BookRepository/blob/development/documentation/Initial%20thoughts%20for%20Book%20Repository.jpg)

Milestone Project 3: Data-Centric Development with Python, Flask, JavaScript, CSS, HTML, and MongoDB. Using several Python frameworks and the Google Books API. The Book Repository is a virtual library for the personal storage and sharing of books, sharing of thoughts about books read, via comments and votes, and all through a secure website.

## Functions

* Authentication (Py) - optional feature
* Registration (Py) and (Js) {EmailJS} - optional feature
* Password Reset/Communication: (Js) {EmailJS}
* Delete User :-( --> Should all comments, votes and books be deleted too? No, though tag user as deleted in comments. Books?
* CRUD (Py) {[(MongoDB)]}
	* Create using Google Book API (better choice) and use [ISBN Search](https://isbnsearch.org/) as a backup (?) and `from difflib import get_close_matches`
	* Search for book, return list of books in DB, as well as Google Books API. Select relevant book. Use `get_close_matches` on existing books (Tery => Terry).
* Upload Image?
	* Profile?
	* Book, if not exist in ISBN Search?
* Dashboard/Stats (Py) {[(MongoDB)]} - optional feature
* Votes/Comments (Py) {[(MongoDB)]} - optional feature
	* Notification badge on comments?
* Affiliate Link to Amazon (Py) - optional feature
	* Webscraping `import requests` and `from bs4 import BeautifulSoup`
* Stats: # of Users, # of Books/User(s), # of. Users/Book, # of Comments/User, # of Comments/Book,  # of Comments/Site, # of Up or Down or "Meh" Votes/Book, Averages & Means & Min & Max
* Heroku Deployment using gunicorn instead of WSGI
* Documentation: README.md, User Experience and Design.md, Testing.md (Selenium IDE + ?), Code Walkthrough.md, User Journey Map
* Git Versioning: Dev/Test/Prod/Doc
* Layout, Structure, and Design: </> HTML 5, .css{} CSS 3, (Js), (Py)

## Colour Scheme

[Colour Scheme on Coolors] (<https://coolors.co/64ffda-26a69a-ff4081-eceff1-37474f>)

* Aquamarine #64FFDA => Materialize: teal accent-2
* Persian Green #26A69A => Materialize: teal lighten-1
* French Rose #FF4081 => Materialize: pink accent-2
* Cultured #ECEFF1 => Materialize: blue-grey lighten-5
* Charcoal #37474F => Materialize: blue-grey darken-3

## Features

* Open Book: Registration or Login or Password Reset.
* Left Page:
	* View list of own books (library).
	* Search for books, own, site, and Google Books.
* Right Page:
	* Book Details, front cover, title, authour, ISBN, description.
	* Comments and voting, read/not read yet (interested)
* Statistics Page Left: personal statistics.
* Statistics Page Right: site statistics.

## Use Cases

* Registration --> E-mail confirmation link --> Login --> CRUD --> Stats
* Login --> CRUD --> Stats
* Password Reset --> E-mail reset link --> Login --> CRUD --> Stats
* Delete User --> E-mail delete link for confirmation --> Delete :-(

## Technologies
* </> HTML, .css{} CSS, (Js), (Py), {[(MongoDB)]}
* {...} API's and Frameworks
	* (Js):
		* EmailJS -> Password Reset & Information
		* GeoLocation -> Country (City)
	* (Py):
		* numpy
		* pandas
		* bokeh
		* bs4
		* Google Books
		* OpenMap
		* gunicorn
		* Flask
		* ISBN Search (Webscraping)
	* .css{}
		* Materialize 1.0 (to materialize or not to materialize, that is the question...)

## Directory Structure (Virtual Environment)

* *.py
* README.md
* assets/
	* images/
		* ...
	* scripts/
		* sendmail.js
		* book.js
		* ...js
	* styles/
		* style.css
		* ...css
* documentation/
	* ...md
	* ...
* templates/
	* ...html
* DEV/...one folder per code snippet (in .gitignore)

## Database Structure
* Users
	* Name
	* Password (hashed)
	* E-Mail
	* Country (GeoLocation) -> Country
	* Comments {dict} -> Book Comments
	* Votes {dict} -> Book Votes

* Book
	* Title
	* Authour
	* Year
	* ISBN
	* Users -> Users
	* Comments -> Users
	* Votes -> Users

* Comments
	* Books
	* Users

* Votes
	* Books
	* Users


* Country
	* Country -> Users

* Stats
	* User(s)
	* Book(s)
	* Site
		* Users
		* Books
		* Countries
	* Country
	* Comments
	* Votes

	
MongoDB Atlas: Project -> Database(s) -> Collection(s) -> Document(s) -> Field(s)

## Deployment
1. Code Institute gitpod-full-template
2. BookRepository
3. VS Code: https://github.com/NaoiseGaffney/BookRepository on DropBox
4. bookrepository.py
5. .env --> GOOGLE_API_KEY (Google Books API), MONGO_URI, MONGO_URI_BR
6. .gitignore --> .env, .venv, /DEV
7. Directory Structure: for DEV and Test (promoted to Production)
8. Stage All Changes --> Commit All --> Push
9. Google API Keys: during development, IP addresses, in production HTTP referrer
10. Continuous Delivery: Development (DEV: local store only) --> Development (GitHub Pull) --> Staging (Test: GitHub --> Heroku) --> Production (Heroku)
11. Heroku - create new app: Dashboard --> New --> Create new app --> App Name: virtual-book-repository, Region: Europe --> Create app --> Deployment method: GitHub --> BookRepository, Enable Automatic Deploys, Deploy Branch --> Settings: Reveal Config Vars => IP = 0.0.0.0, PORT = 5000, PRODUCTION = ON (disables debug, debug=False) --> Restart All Dynos (config vars to take effect) --> Deploy: Create new pipeline - vbookrepo-pipe, staging --> Create pipeline --> Connect GitHub Repository to Pipeline: BookRepository --> Create new review apps for new pull requests automatically (When enabled, every new pull request opened will create a Review app automatically and pull requests that are closed will be deleted.), Choose region: Europe --> Enable Review Apps --> Reveal Config Vars => IP = 0.0.0.0, PORT = 5000, PRODUCTION = ON (disables debug, debug=False), GOOGLE_API_KEY = ..., MONGO_URI = ..., MONGO_URI_BR = ...
12. Create a new branch in VS Code: Shift-Command-P, Git: create branch. I can now switch between the two branches, 'master' (Staging) and 'review' (Development).

Code Institute gitpod-full-template: BookRepository => VS Code = development files, requirements.txt, .gitignore, Stage-Commit-Push => GitHub = BookRepository:master => Heroku = Create New App --> App Name: virtual-book-repository-stage, Choose a region: Europe, Create App --> Deploy - Deployment Method: GitHub (Connect to GitHub): NaoiseGaffney/BookRepository, Enable Automatic Deploys:master, Deploy Branch:master (no Vars set yet, will crash), Add this app to a pipeline: Create new pipeline, Choose a stage to add to this app:staging, Create pipeleine.

[Adding GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)

## Odds and Ends
Meta-tags in HTML to improve Google Searches. Add Favicon. Passwords and keys as environment variables. Colour-blindness: Sim Daltonism (using Orange and Blue).

```
python3 -m venv .venv
source .venv/bin/activate
.gitignore (.env .venv)
pip install pip --upgrade

pip3 install requests
pip3 install python-dotenv

pip3 install dnspython
pip3 install pymongo
pip3 install gunicorn
pip3 install flask

https://sites.google.com/a/chromium.org/chromedriver/downloads
cp /Users/gaff/Downloads/chromedriver /usr/local/bin/.
Run once and allow to run in Security Settings (System Preferences --> Security & Privacy --> Allow apps downloaded from:...)
pip3 install -U selenium

pip3 install bs4 <-- may not be required as I'm not doing any Webscraping

pip3 freeze --local > requirements.txt
echo web: gunicorn bookrepository:app > Procfile
```

### Google API
No HTTP Referrer as the GOOGLE_API_KEY is stored in the .env file. I need to look at some form of authentication though.


## Testing - Automated

[Selenium Tutorial](https://www.javatpoint.com/selenium-tutorial)

### Selenium IDE

[Selenium IDE: Login Test](https://www.javatpoint.com/selenium-ide-login-test)

### Selenium WebDriver

[Selenium WebDriver](https://www.javatpoint.com/selenium-webdriver)

[Selenium WebDriver and Python](https://www.javatpoint.com/selenium-python)
