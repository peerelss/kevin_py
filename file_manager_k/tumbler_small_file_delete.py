# 删除文件以 tumblr 开头 100.jpg 结尾的小文件
import os.path

dir = r'M:\after\image'
file_dir_list = [
    r'F:\after\image', r'G:\after\image', r'H:\after\image', r'I:\after\images', r'J:\after\image', r'L:\after\image',
    r'M:\after\image'
]


def tumblr_small_file_delete(dir_path):
    i = 0
    if os.path.isdir(dir_path):
        file_list = os.listdir(dir_path)
        for f in file_list:
            file_path = os.path.join(dir_path, f)
            if os.path.isfile(file_path):
                file_path = os.path.join(dir_path, f)
                if file_path.endswith('.jpg') or file_path.endswith('.gif') or file_path.endswith(
                        '.png') or file_path.endswith('.gifv'):
                    file_size = (os.path.getsize(file_path)) / 1000
                    if file_size < 25:
                        print(' delete ' + file_path)
                        print(str(file_size) + " kb ")
                        i = i + 1
                        os.remove(file_path)
            elif os.path.isdir(file_path):
                tumblr_small_file_delete(file_path)
    print(str(dir_path) + ' delete ' + str(i) + ' files')


if __name__ == '__main__':
    for d in file_dir_list:
        tumblr_small_file_delete(d)
