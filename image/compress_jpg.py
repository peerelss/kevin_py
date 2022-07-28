# -*- coding: utf-8 -*-
from PIL import Image
import os


def get_size(file):
    size = os.path.getsize(file)
    return size / 1024


dir_path = r'd:\jpg'
items = os.listdir(dir_path)

for item in items:
    # print(item)
    path = os.path.join(dir_path, item)
    print(item)


def compress_image(infile, outfile=None, mb=150, step=10, quality=80):
    """不改变图片尺寸压缩到指定大小
    :param infile: 压缩源文件
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """
    if outfile is None:
        outfile = infile
    o_size = get_size(infile)
    if o_size <= mb:
        im = Image.open(infile)
        im.save(outfile)

    while o_size > mb:
        im = Image.open(infile)
        im.save(outfile, quality=quality)
        if quality - step < 0:
            break
        quality -= step
        o_size = get_size(outfile)


def resize_image(infile, outfile='', x_s=800):
    """修改图片尺寸
    :param infile: 图片源文件
    :param outfile: 重设尺寸文件保存地址
    :param x_s: 设置的宽度
    :return:
    """
    im = Image.open(infile)
    x, y = im.size
    y_s = int(y * x_s / x)
    out = im.resize((x_s, y_s), Image.ANTIALIAS)

    out.save(outfile)


if __name__ == '__main__':
    # 源路径      # 压缩后路径
    compress_image(r"d:\jpg\20220616_094100.jpg", r"d:\jpg\2.JPG")
    resize_image(r"d:\jpg\2.JPG", r"d:\jpg\3.JPG")
