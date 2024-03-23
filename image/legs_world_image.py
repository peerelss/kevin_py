import requests
import unicodedata as ucd
import os.path


def get_legs_world_jpg(s_url):
    dir_ = 'C:\\Users\kevin\Downloads\legsworld\cover\\'
    print(s_url)
    try:
        response = requests.get(s_url)
        with open(dir_ + s_url[s_url.rfind('/'): s_url.index('jpg') + 3], "wb") as file:
            file.write(response.content)
    except:
        print('null')


for i in reversed(range(606, 7314)):
    index = str(i)
    if i < 1000:
        index = '0' + str(i)
    url = "https://legsworld.net/UpdatesNew/Previews-1212x1644/" + str(i) + '.jpg'
    get_legs_world_jpg(url)
