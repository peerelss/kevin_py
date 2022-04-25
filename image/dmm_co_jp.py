import requests
from bs4 import BeautifulSoup

params = {
    'dmmref': '51cmn00127',
    'i3_ref': 'detail',
    'i3_ord': '1',
    'i3_pst': 'info_maker',
}


def get_movie_from_url():
    response = requests.get('https://www.dmm.co.jp/digital/videoa/-/list/=/article=maker/id=40037/', params=params)
    soup = BeautifulSoup(response.content, "lxml")
    a_soup = soup.find_all('a', href=True)
    for a in a_soup:
        print(a)


if __name__ == '__main__':
    get_movie_from_url()
