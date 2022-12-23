from flask import Flask
import json
from flask_cors import CORS
import pymongo
from bson.json_util import dumps, loads
from flask import Flask, render_template, request, Response

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


@app.route('/jav/star/<name>')
def get_jpg_by_name(name):
    myquery = {"av_star": name}
    result_x = mycol.find(myquery, {'av_id': 1, 'av_jpg': 1, "_id": 0}).limit(10).skip(1)
    return dumps(list(result_x)[0]['av_jpg'])


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
        t = {'products': list(result_x)}
        return json.dumps(t)
    else:
        result_x = mycol_en.find(myquery,
                                 {'av_id': 1, 'av_jpg': 1, 'av_title': 1, 'av_star': 1, "av_maker": 1, "_id": 0}).limit(
            page_size).skip(skip)
        return json.dumps(list(result_x))


@app.route('/jav_en/<maker_name>/<int:page_size>/<int:page_no>')
def show_maker_en(maker_name, page_size=0, page_no=0):
    print('page_size : ' + " page_no : ")
    skip = page_size * (page_no - 1)
    myquery = {"av_maker": maker_name}
    result_x = mycol.find(myquery, {'av_id': 1, 'av_jpg': 1, 'av_title': 1, "_id": 0}).limit(page_size).skip(skip)
    return dumps(list(result_x))


@app.route('/avid/<av_id>')
def show_av_detail_by_id(av_id):
    myquery = {"av_id": av_id.upper()}
    result_x = mycol.find(myquery).sort('_id', -1)
    t = {'detail': result_x[0]}
    return dumps(t)


# 入参
@app.route('/series/<series_id>/<int:page_no>')
def show_movies_by_series(series_id, page_no):
    myquery = {"av_series": series_id}
    result_x = mycol.find(myquery, {'av_id': 1, 'av_jpg': 1, 'av_title': 1, '_id': 0}).limit(20).skip(
        20 * (page_no - 1))
    result_count = mycol.count_documents(myquery)
    # count = result_x.count()

    re = {'count': result_count, 'lists': list(result_x)}
    return dumps(re)


@app.route('/jav_en/<maker_name>/count')
def show_maker_count(maker_name):
    myquery = {"av_maker": maker_name}
    myquery1 = {'av_star': maker_name}
    result_x = mycol.count_documents(myquery)
    if result_x > 0:
        return dumps(result_x)
    else:
        return dumps(mycol_en.count_documents(myquery1))


# 搜索结果，首先搜索片名-如果为空择搜索番号，如果为空择搜索女优名
@app.route('/search/<search_name>')
def show_search_result(search_name):
    myquery = {'av_title': {'$regex': search_name}}
    result_x = mycol.find(myquery, {'av_id': 1, 'av_jpg': 1, 'av_title': 1, '_id': 0}).limit(30)

    return dumps({'lists': list(result_x)})


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


# 获取所有的女优名，以及作品数量（聚合搜索）
@app.route('/stars')
def show_all_stars():
    pipeline = [{'$group': {'_id': "$av_star", 'num_maker': {'$sum': 1}}},
                {'$sort': {'num_maker': -1}},
                {'$match': {'num_maker': {'$gt': 2}}},
                {'$limit': 50}
                ]
    result_x = mycol.aggregate(pipeline)
    return dumps({'stars': result_x})


# 获取所有的厂家，以及作品数量
@app.route('/makers')
def show_all_maker():
    pipeline = [{'$group': {'_id': "$av_maker", 'num_maker': {'$sum': 1}}},
                {'$sort': {'num_maker': -1}},
                {'$match': {'num_maker': {'$gt': 2}}},
                {'$limit': 30}
                ]
    result_x = mycol.aggregate(pipeline)
    return dumps({'makers': result_x})


# 获取所有的系列，已经数量，按数量排列
@app.route('/series')
def show_all_series():
    pipeline = [{'$group': {'_id': "$av_series", 'num_maker': {'$sum': 1}}},
                {'$sort': {'num_maker': -1}},
                {'$match': {'num_maker': {'$gt': 2}}},
                {'$limit': 30}
                ]
    result_x = mycol.aggregate(pipeline)

    return dumps({'series': result_x})


@app.route('/get_all_offline', methods=['POST', 'GET'])
def result():
    print(request.is_json)
    print(request.json)
    return 'success'


# 获取所有的tag，按数量排列
@app.route('/tags')
def show_all_tags():
    pipeline = [{'$group': {'_id': "$av_tags", 'num_maker': {'$sum': 1}}},
                {'$sort': {'num_maker': -1}},
                {'$match': {'num_maker': {'$gt': 2}}},
                {'$limit': 30}
                ]
    result_x = mycol.aggregate(pipeline)
    return dumps({'tags': result_x})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
