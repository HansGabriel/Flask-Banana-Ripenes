from flask import Flask, render_template, request, jsonify
from algorithms.classify import classifyBanana

from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

def getFileExtension(file):
    return file.filename.split('.')[1]


@app.route('/')
def hello():
    return render_template('main.html')

@app.route('/uploadajax', methods=['POST'])
def upldfile():
    if request.method == 'POST':
        files = request.files['file']
        filename = secure_filename(files.filename)
        updir = os.path.join(basedir, 'static/images/')
        files.save(os.path.join(updir, filename))
        file_dir = f'upload/{filename}'
        print(file_dir)
        result = classifyBanana(file_dir)
        return jsonify(name=filename, classType = result)