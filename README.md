## NEIGHBOURHOOD WATCH.
This is an Independent project for Moringa Core Django module, june 17 2022.

 ## Description
Neighbourhood application will help in the viewing of what is going on in the neighbourhood .Update your profile and credantials incase of any opportunity or any news you are up to date

 ## Features
- The home page allows users to sign up if they have no account or login if they have one 
- User can see all a page to update their profile
- Users can now see all the bussiness,and news

- view site in here: https://tina-hood.herokuapp.com/

## Technologies Used
- Python 3.9
- Django MVC framework
- HTML, CSS and Bootstrap for a beautiful design,and styling
- JavaScript to make the application interactive
- Postgressql for database
- Heroku for deployment
- django restframework to help with the api
 ## Specifications
To view the user directories or BDD check the specs file.

## Prerequisite
The Neighbourhood project requires a prerequisite understanding of the following:

- Django Framework
- Python3.9
- Postgres
- Python virtualenv
- Setup and installation
- Clone the Repo
- Activate virtual environment
- Activate virtual environment using python3.9 as default handler virtualenv -p /usr/bin/python3.9 venv && -  source venv/bin/activate

## Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt

Create the Database
- psql
- CREATE DATABASE neighbourhood;
.env file
* Create .env file and paste paste the following filling where appropriate:

- SECRET_KEY = '<Secret_key>'
- DBNAME = 'neighbourhood'
- USER = '<Username>'
- PASSWORD = '<password>'
- DEBUG = True
- Run initial Migration
- python3.9 manage.py makemigrations  
- python3.9 manage.py migrate
     * Run the app
- python3.9 manage.py runserver
- Open terminal on localhost:8000
 ## Known bugs
No known bugs so far. If found drop me an email.

 ##  Contributors
- Christine Nkatha
## Contact Information
nkathachristine456@gmail.com || christine.nkatha@student.moringaschool.com



## LICENCE
MIT License

Copyright (c) 2022 @Christine Nkatha

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.