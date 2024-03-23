import urllib

import werkzeug
from flask import Flask, send_from_directory, safe_join, abort, jsonify, send_file, request
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def get_image_list(directory):
    image_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_path = os.path.join(root, file)
                image_list.append(image_path)
    return image_list


@app.route('/image/<path:filename>')
def custom_static(filename):
    directory = r'M:\after\image\图片任务组_hobble_o'  # 自定义图片存储目录
    try:
        # 安全地拼接目录和文件名
        filename = werkzeug.utils.safe_join(directory, filename)
        if not os.path.isfile(filename):
            # 文件不存在时返回404
            abort(404)
        return send_from_directory(directory, os.path.basename(filename))
    except FileNotFoundError:
        abort(404)


@app.route('/show-image', methods=['GET'])
def show_image():
    # 获取图片的绝对路径
    image_path = request.args.get('path')

    # 检查图片路径是否存在且确实是文件
    if not image_path or not os.path.isfile(image_path):
        abort(404)  # 如果路径无效或文件不存在，返回404错误

    return send_file(image_path)


@app.route('/images')
def images():
    directory = r'M:\after\image\图片任务组_hobble_o'  # 替换为你的图片所在目录
    image_list = get_image_list(directory)
    return jsonify(image_list)


@app.route('/files')
def list_files():
    directory = r'M:\after\image\图片任务组_hobble_o'  # 替换为实际目录路径
    files = os.listdir(directory)
    files_list = '<br>'.join(files)  # 创建一个简单的HTML字符串来显示文件列表
    return files_list


@app.route('/get-images', methods=['GET'])
def get_images():
    folder_o = request.args.get('folder')
    folder = urllib.parse.unquote(folder_o)
    print(folder)

    # 确保安全地获取文件夹路径
    if not folder or '..' in folder or '~' in folder:
        abort(400, 'Invalid folder path')

    full_folder_path = os.path.abspath(folder)

    # 检查路径是否存在且为目录
    if not os.path.isdir(full_folder_path):
        abort(404, 'Folder not found')

    # 获取文件夹内的图片文件
    images = [f for f in os.listdir(full_folder_path)
              if os.path.isfile(os.path.join(full_folder_path, f))
              and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # 构造JSON数据
    images_info = [{"filename": image, "path": os.path.join(full_folder_path, image)} for image in images]

    return jsonify(images_info)


# 删除图片
@app.route('/delete-image', methods=['GET'])
def delete_image():
    image_path = request.args.get('image_path')

    # 检查图片路径是否提供
    if not image_path:
        return jsonify({"status": "failed", "message": "No image path provided"}), 400

    # 检查文件是否存在
    if not os.path.exists(image_path):
        return jsonify({"status": "failed", "message": "Image not found"}), 404

    # 尝试删除图片
    try:
        print(image_path)
        os.remove(image_path)
        print('删除成功')
        return jsonify({"status": "success", "message": "Image deleted successfully"})
    except Exception as e:
        print('删除失败')
        return jsonify({"status": "failed", "message": str(e)}), 500


@app.route('/list-path-details', methods=['GET'])
def list_path_details():
    path = request.args.get('path')
    if not path or not os.path.exists(path) or not os.path.isdir(path):
        return jsonify({"error": "Invalid or non-existent directory path provided."}), 400

    contents = {'files': [], 'directories': []}
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            contents['files'].append({'filename': item, 'path': item_path})
        elif os.path.isdir(item_path):
            contents['directories'].append({'filename': item, 'path': item_path})

    return jsonify(contents)


if __name__ == "__main__":
    app.run(debug=True)
