import requests


def get_legs_world_jpg(url):
    html = requests.get(url)
    if html.history:
        print('not exist')
    else:
        print(url)


for i in range(6621, 7000):
    url = "https://legsworld.net/UpdatesNew/Previews-1212x1644/" + str(i) + '.jpg'
    get_legs_world_jpg(url)
