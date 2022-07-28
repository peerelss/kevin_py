from flask import Flask
import json
from flask_cors import CORS
import pymongo
from bson.json_util import dumps, loads

STATIC_PATH = r"/media/kevin/Backup/tumblr_txt_all3/"
app = Flask(__name__, static_folder=STATIC_PATH)
CORS(app, supports_credentials=True)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["av_db"]
mycol = mydb['av_items_thumb']
mycol2 = mydb['av_items_thumb_jav_bus']
mycol3 = mydb['av_items_thumb_jav_luxu']
mycol_en = mydb['av_items_thumb_en']


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


@app.route('/luxu/<int:page_size>/<int:page_no>')
def show_luxu_no(page_size=0, page_no=0):
    # print('page_size : ' + page_size + " page_no : " + page_no)
    skip = page_size * (page_no - 1)
    myquery = {"av_id": {"$regex": "^259LUXU"}}
    result_x = mycol3.find(myquery, {'av_id': 1, 'av_jpg': 1, "_id": 0}).limit(page_size).skip(skip)
    return dumps(list(result_x))


@app.route('/javbus/<star_name>/<int:page_size>/<int:page_no>')
def show_star_name_no(star_name, page_size=0, page_no=0):
    # print('page_size : ' + page_size + " page_no : " + page_no)
    skip = page_size * (page_no - 1)
    myquery = {"av_star": star_name}
    result_x = mycol.find(myquery, {'av_id': 1, 'av_jpg': 1, "_id": 0}).limit(page_size).skip(skip)
    return dumps(list(result_x))


@app.route('/jav/<name>/<int:page_size>/<int:page_no>')
def show_maker_or_star(name, page_size=0, page_no=0):
    skip = page_size * (page_no - 1)
    myquery = {"av_maker": name}
    myquery1 = {"av_star": name}
    if mycol.count_documents(myquery) > 0:
        result_x = mycol.find(myquery,
                              {'av_id': 1, 'av_jpg': 1, 'av_title': 1, 'av_star': 1, "av_maker": 1, "_id": 0}).limit(
            page_size).skip(skip)
        return dumps(list(result_x))
    elif mycol.count_documents(myquery1) > 0:
        result_x = mycol.find(myquery1,
                              {'av_id': 1, 'av_jpg': 1, 'av_title': 1, 'av_star': 1, "av_maker": 1, "_id": 0}).limit(
            page_size).skip(skip)
        return dumps(list(result_x))
    else:
        result_x = mycol_en.find(myquery,
                                 {'av_id': 1, 'av_jpg': 1, 'av_title': 1, 'av_star': 1, "av_maker": 1, "_id": 0}).limit(
            page_size).skip(skip)
        return dumps(list(result_x))


@app.route('/jav_en/<maker_name>/<int:page_size>/<int:page_no>')
def show_maker_en(maker_name, page_size=0, page_no=0):
    print('page_size : ' + " page_no : ")
    skip = page_size * (page_no - 1)
    myquery = {"av_maker": maker_name}
    result_x = mycol.find(myquery, {'av_id': 1, 'av_jpg': 1, 'av_title': 1, "_id": 0}).limit(page_size).skip(skip)
    return dumps(list(result_x))


@app.route('/jav_en/<maker_name>/count')
def show_maker_count(maker_name):
    myquery = {"av_maker": maker_name}
    myquery1 = {'av_star': maker_name}
    result_x = mycol.count_documents(myquery)
    if result_x > 0:
        return dumps(result_x)
    else:
        return dumps(mycol_en.count_documents(myquery1))


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
