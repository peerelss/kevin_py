from flask import Flask
import json
from flask_cors import CORS

STATIC_PATH = r"/media/kevin/Backup/tumblr_txt_all3/"
app = Flask(__name__, static_folder=STATIC_PATH)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/tumblr/<file_name>')
def show_tumblr_page(file_name):
    a_file = open(STATIC_PATH + file_name, "r")
    list_of_lists = []
    temp_count = 0
    for line in a_file:
        temp_count = temp_count + 1
        if temp_count > 1000:
            break
        stripped_line = line.strip()
        # print(stripped_line)
        if stripped_line:
            list_of_lists.append(stripped_line)

    return json.dumps(list_of_lists)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
