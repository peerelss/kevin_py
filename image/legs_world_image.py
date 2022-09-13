import requests
import unicodedata as ucd


def get_legs_world_jpg(url):
    print(url)


for i in reversed(range(6766, 6812)):
    url = "https://legsworld.net/UpdatesNew/Previews-1212x1644/" + str(i) + '.jpg'
    get_legs_world_jpg(url)
