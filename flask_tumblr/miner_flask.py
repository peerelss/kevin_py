from flask import Flask, render_template, request
import json
from flask_cors import CORS
import pymongo
from bson.json_util import dumps, loads

STATIC_PATH = r"/media/kevin/Backup/tumblr_txt_all3/"
app = Flask(__name__, static_folder=STATIC_PATH)


@app.route('/')
def hello_world():
    return render_template('hello.html')


@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result1 = request.form
        print(result1['ip地址'])
        return render_template("result.html", result=result1)


@app.route('/testnode')
def test_node():
    return json.dumps({'name': "kevin"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
