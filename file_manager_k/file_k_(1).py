from image.sdk_every_thing_http import search_file_by_key_world
from pathlib import Path
import os


# os.remove(file_with_copy)


def find_file_without_1(file_detail):
    copy_file = file_detail['file_path']
    print(copy_file)
    origin_file = copy_file.replace('(1)', '').replace(" (1)", "")
    if os.path.exists(origin_file) and os.path.getsize(origin_file) == os.path.getsize(copy_file):
        print(f"{origin_file}, exist")
        os.remove(copy_file)


def handle_file_name(key_world, file_detail):
    old_file_name = str(file_detail['file_path'])
    last_index = old_file_name.rfind(key_world)
    new_file_name = old_file_name[:last_index] + old_file_name[last_index + len(key_world):]
    print(new_file_name)
    if not os.path.exists(new_file_name):
        os.rename(old_file_name, new_file_name)
        print(f'已将 "{old_file_name}" 重命名为 "{new_file_name}"')
    else:
        old_file_size = os.path.getsize(old_file_name)
        new_file_size = os.path.getsize(new_file_name)
        if old_file_size > new_file_size:
            os.remove(new_file_name)
            os.rename(old_file_name, new_file_name)
        else:
            os.remove(old_file_name)


def find_all_file_contain_1(key_world):
    results = search_file_by_key_world(key_world)
    for re in results:
        if re['size'] > 100 * 1024 * 1024:
            print(re)
            handle_file_name(key_world, re)


# 找到所在的文件夹，寻找有没有同名且同大小的文件

# 删除文件名包含(1)


if __name__ == "__main__":
    find_all_file_contain_1('[Thz.la]')

