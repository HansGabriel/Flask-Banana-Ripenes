from flask import Flask, render_template, request, jsonify
from algorithms.classify import classifyBanana

app = Flask(__name__)


@app.route('/')
def hello():
    # result = classifyBanana('static/images/banaa.png')
    return render_template('main.html')

@app.route('/uploadajax', methods=['POST'])
def upldfile():
    if request.method == 'POST':
        test = {"test": "test", "name": "name"}
        files = request.files['file']
        result = classifyBanana('static/images/banaa.png')
        return jsonify(test)
        # if files and allowed_file(files.filename):
        #     filename = secure_filename(files.filename)
        #     app.logger.info('FileName: ' + filename)
        #     updir = os.path.join(basedir, 'upload/')
        #     files.save(os.path.join(updir, filename))
        #     file_size = os.path.getsize(os.path.join(updir, filename))
        #     return jsonify(name=filename, size=file_size)