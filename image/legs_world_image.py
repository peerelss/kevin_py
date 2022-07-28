import requests
import unicodedata as ucd


def get_legs_world_jpg(url):
   print(url)


for i in reversed(range(6736,6800)):
    url = "https://legsworld.net/UpdatesNew/Previews-1212x1644/" + str(i) + '.jpg'
    get_legs_world_jpg(url)


