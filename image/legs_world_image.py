import requests
import unicodedata as ucd


def get_legs_world_jpg(url):
   print(url)


for i in reversed(range(1000,6381)):
    url = "https://legsworld.net/UpdatesNew/Previews-1212x1644/" + str(i) + '.jpg'
    get_legs_world_jpg(url)


