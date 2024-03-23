import requests

cookies = {
    'userinfo': '__a22f737f8259be708cfa^%^3B^%^7B^%^22username^%^22^%^3A^%^22peerelss^%^22^%^2C^%^22uniqueid^%^22^%^3A^%^22839412dc40a2ccc0deae2bb85be73d20^%^22^%^2C^%^22dvs9-1^%^22^%^3A1^%^2C^%^22ab^%^22^%^3A^%^22tao-uma-1-b-2^%^7Ctao-7fc-1-b-3^%^7Ctao-cou-1-a-1^%^7Ctao-sD8-1-b-9^%^7Ctao-73d-1-b-6^%^22^%^7D',
    'g_state': '{i_l:0}',
    'auth': '__e992d7acd9fe6e73a81d^%^3B^%^2255f83068c111e32a999887e7781eb8f9^%^22',
    'auth_secure': '__f982c16e20f7f0a01fac^%^3B^%^2296851dcdeb0a463b325beca13e578baf^%^22',
    'td': '0:2030^%^3B3:1140^%^3B6:1594x1541^%^3B7:2070^%^3B12:2150x1276^%^3B20:1745',
    'pxcts': '5040e153-0a9c-11ee-8569-566c58436565',
    'tw': '^%^7B^%^22userprofile-zone-2^%^22^%^3A1049^%^7D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.deviantart.com/kevinw59/gallery',
    'Connection': 'keep-alive',
    # 'Cookie': 'userinfo=__a22f737f8259be708cfa^%^3B^%^7B^%^22username^%^22^%^3A^%^22peerelss^%^22^%^2C^%^22uniqueid^%^22^%^3A^%^22839412dc40a2ccc0deae2bb85be73d20^%^22^%^2C^%^22dvs9-1^%^22^%^3A1^%^2C^%^22ab^%^22^%^3A^%^22tao-uma-1-b-2^%^7Ctao-7fc-1-b-3^%^7Ctao-cou-1-a-1^%^7Ctao-sD8-1-b-9^%^7Ctao-73d-1-b-6^%^22^%^7D; g_state={i_l:0}; auth=__e992d7acd9fe6e73a81d^%^3B^%^2255f83068c111e32a999887e7781eb8f9^%^22; auth_secure=__f982c16e20f7f0a01fac^%^3B^%^2296851dcdeb0a463b325beca13e578baf^%^22; td=0:2030^%^3B3:1140^%^3B6:1594x1541^%^3B7:2070^%^3B12:2150x1276^%^3B20:1745; pxcts=5040e153-0a9c-11ee-8569-566c58436565; tw=^%^7B^%^22userprofile-zone-2^%^22^%^3A1049^%^7D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'username': 'kevinw59',
    'type': 'gallery',
    'offset': '312',
    'limit': '24',
    'folderid': '47664817',
    'csrf_token': 'WCQXXyHDVVPpNR-r.s9uufl.aPYFchvIIsfha0lnPsubT4miywKB9nowJFiu0uLeSB4',
    'da_minor_version': '20230710',
}

response = requests.get(
    'https://www.deviantart.com/_puppy/dashared/gallection/contents',
    params=params,
    cookies=cookies,
    headers=headers,
)

json_re = response.json()
print(json_re)
