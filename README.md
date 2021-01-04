# [Banana Ripeness Flask]()

A web app, built using flask, that identifies the ripeness of a banana.

* **Front:** The frontend was built using HTML, CSS and Jquery.
* **Backend:** The backend was built using flask, a minimalist framework built in python, used for simple serving simple applications.
* **Libraries:** Libraries used in this project include opencv-python, numpy, and Pillow. All of which were used for the banana ripeness classification. 


## Installation

Installation requires anaconda or conda installed. Having python only may result to errors in opencv.

First clone and cd into the repository

```
git clone https://github.com/HansGabriel/Flask-Banana-Ripeness.git
cd Flask-Banana-Ripeness
```

Install virtualenv (if not yet installed)

```
pip install virtualenv
```

Create a virtual environment and activate it

```
virtualenv venv
source venv/scripts/activate
```

Install the dependencies

```
pip install -r requirements.txt
```

Run the app with flask

```
python app.py
```

Now you can visit it on the browser at http://localhost:5000/


