## Application

This is a Flask web application that uses the MobileNetV2 model for classification of images of skin lesions. It has a 83.4% accuracy. 
<br> I have added the Jupyter notebook which was used to train the model.
<br> The dataset was taken from International Skin Imaging Collaboration(ISIC).


## To run the source code in your local system then follow the steps below(Windows) : 

1) Download all the files from git

2) Download and install Python 3.9.1 from https://www.python.org/downloads/release/python-390/

3) Open command prompt from start, and run the command python --version to check if it is properly installed.

4) Then run the following commands

5) Go to the main directory where app.py is present, run:  `cd <path>`
6) To create virtual environment run: `python -m venv venv`
7) To activate venv run: `venv\Scripts\activate`
8) Install requirements: `pip install -r requirements.txt`
9) Setup flask, run:`set FLASK_APP=app.py`
10) Deploy the app on your local, run: `flask run`
11) Go to `http://127.0.0.1:5000/`
