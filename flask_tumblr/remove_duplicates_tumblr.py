import os
import redis
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
file_dir_list = [
    r'F:\after\image', r'G:\after\image', r'H:\after\image', r'I:\after\images', r'J:\after\image', r'L:\after\image',
    r'M:\after\image'
]


def remove_duplicates(folder_paths):
    for folder in folder_paths:
        for root, dirs, files in os.walk(folder):
            for file in files:
                # 检查文件是否为图片
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', 'gifv')) and file.startswith(
                        "tumblr"):
                    if r.exists(file):
                        # 获取同名文件位置
                        file_pre = r.get(file)
                        # 如果同名文件存在
                        if os.path.exists(file_pre):
                            file_path = os.path.join(root, file)
                            # 如果两个是同一个文件
                            if file_pre == file_path:
                                print(f"same one : {file_pre}, ")
                            else:
                                print(f"duplicates File found pre file: {file_pre}, now file: {file_path}")
                    else:
                        file_path = os.path.join(root, file)
                        r.set(file, file_path)
                        print(f"File saved: {file}, Path: {file_path}")


def delete_empty_directories(path):
    if os.path.exists(path) and os.path.isdir(path):
        # 获取目录下的所有子目录和文件
        children = os.listdir(path)

        # 递归调用每个子目录
        for child in children:
            child_path = os.path.join(path, child)
            if os.path.isdir(child_path):
                delete_empty_directories(child_path)

        # 再次检查当前目录是否为空（可能由于子目录删除变为空）
        if not os.listdir(path):
            # 如果目录现在为空，删除它
            os.rmdir(path)
            print(f"Deleted empty directory: {path}")
        else:
            pass
    #     print(f"Directory is not empty: {path}")
    else:
        print(f"Path is not a directory or does not exist: {path}")


directory_path = r'F:\after\image\jpg\tumblr\tumblr-utils-master'


def build_directory_tree(root_dir):
    """构建一个目录树结构的JSON表示。"""
    tree = {"name": os.path.basename(root_dir), "children": []}

    try:
        for entry in os.listdir(root_dir):
            path = os.path.join(root_dir, entry)
            if os.path.isdir(path):
                if path in directory_path:
                    tree["children"].append(build_directory_tree(path))
                else:
                    tree["children"].append({"name": entry, 'children': []})
    except PermissionError:
        # 权限错误时跳过
        pass

    return tree


def get_test():
    import requests

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Connection': 'keep-alive',
        'Origin': 'http://localhost:3000',
        'Referer': 'http://localhost:3000/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(
        'http://localhost:5000/list-path-details?path=M:\\after\\image\\A5579%E6%91%84%E5%BD%B1%E5%B8%88%E5%A4%A7%E7%A5%9E%E6%9C%80%E6%96%B0%E7%BA%A6%E6%8B%8D%E6%A8%A1%E7%89%B9%20%E9%97%BA%E8%9C%9C%20%E7%91%B6%E7%91%B6%20%E6%96%87%E6%96%87%20%E4%BE%9D%E4%BE%9D17%E5%A5%97[1076P+9V]',
        headers=headers,
    )
    print(response.json())


# 示例使用

if __name__ == '__main__':
    # delete_empty_directories(r'f:\after\image')
    get_test()
