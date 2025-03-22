To run the source code in your local system then follow the steps below : 


1) Download all the files from git

2) Download Python 3.9.1 from https://www.python.org/downloads/release/python-390/

3) Run the file, check the Add to variables before installation

4) Go to Environmental Vatiables from start
Double click on path of User variables and add two new paths(Here this is the path in my machine) :
C:\Users\R i t w i k a\AppData\Local\Programs\Python\Python39\Scripts\
C:\Users\R i t w i k a\AppData\Local\Programs\Python\Python39

Again with System variables add paths :
C:\Users\R i t w i k a\AppData\Local\Programs\Python\Python39

5) Open command prompt from start, and run the command python --version to check if it is properly installed.

6) Then run the following commands

7) cd <path copied earlier from step 1>
Eg : cd C:\Users\R i t w i k a\Desktop\WebApp\website

8) To create virtual environment run: python -m venv venv
9) To activate venv run: venv\Scripts\activate
10) Install requirements: pip install -r requirements.txt
11) Setup flask :
set FLASK_APP=app.py
flask run

8) Go to http://127.0.0.1:5000/
