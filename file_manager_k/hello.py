from flask import Flask, render_template
import json
from flask_cors import CORS
import os
from nanoid import generate
from tumblr_model import Tumblr_Model

STATIC_PATH = r"D:\games\angel_the_dreamgirl onlyfans leaked photos\\"
app = Flask(__name__, static_folder=STATIC_PATH)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/legsworld/<int:pageId>')
def show_legsworld_page(pageId=0):
    return ''


@app.route('/tumblr/<file_name>/<int:pageId>')
def show_tumblr_page(file_name, pageId=0):
    if os.path.exists(STATIC_PATH + file_name):
        a_file = open(STATIC_PATH + file_name, "r")
        list_of_lists = []
        temp = 0
        for line in a_file:
            temp = temp + 1
            if temp < pageId:
                continue
            if temp > pageId + 50:
                break
            stripped_line = line.strip()
            # print(stripped_line)
            if stripped_line:
                list_of_lists.append(Tumblr_Model(stripped_line, generate()).__dict__)

        return json.dumps(list_of_lists)
    else:
        return ''


@app.route('/tumblr/list')
def show_all_tumblr_list():
    if os.path.exists(STATIC_PATH) and os.path.isdir(STATIC_PATH):
        return json.dumps(reversed(sorted(os.listdir(STATIC_PATH))))
    return {'[]'}


@app.route('/user/<username>/<int:page>')
def show_user_profile(username, page):
    # show the user profile for that user
    return 'User %s Number %d' % (username, page)


@app.route('/tumblr/download/<tumblr_name>')
def download(tumblr_name):
    return 'success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
