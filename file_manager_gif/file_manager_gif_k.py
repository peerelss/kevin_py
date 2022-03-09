# -*- coding: UTF8 -*-
import os

url_target: str = r'D:\images3\\'


def rename_gifv_to_gif(file_dir):
    if os.path.exists(file_dir) and os.path.isdir(file_dir):
        for i in os.listdir(file_dir):
            if str(i).endswith('gifv'):
                if os.path.exists(file_dir + '\\' + str(i).replace('gifv', 'gif')):
                    pass
                else:
                    os.rename(file_dir + '\\' + str(i), file_dir + '\\' + str(i).replace('gifv', 'gif'))


if __name__ == "__main__":
    if os.path.exists(url_target) and os.path.isdir(url_target):
        for i in os.listdir(url_target):
            if os.path.isdir(url_target + str(i)):
                print(str(i) + " is dir")
                rename_gifv_to_gif(url_target + str(i))
