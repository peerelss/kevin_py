import requests

cookies = {
    'next-auth.callback-url': 'http%3A%2F%2Flocalhost%3A3000%2Fprofile',
    'next-auth.csrf-token': '25aab816be1d793bdc4292af9860cc73bc6d488a171f6e7452ff7489d8c08d94%7C827c8db4fcd4b4a5e1ae5183da90c8aa2c9fbb4ab381dd4fac5933689ab243ae',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'next-auth.callback-url=http%3A%2F%2Flocalhost%3A3000%2Fprofile; next-auth.csrf-token=25aab816be1d793bdc4292af9860cc73bc6d488a171f6e7452ff7489d8c08d94%7C827c8db4fcd4b4a5e1ae5183da90c8aa2c9fbb4ab381dd4fac5933689ab243ae',
    'Origin': 'http://localhost:3000',
    'Referer': 'http://localhost:3000/register',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57',
    'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'route': 'register',
    'email': 'p2@gmail.com',
    'password': 'p1',
}

response = requests.post('http://localhost:3000/api/user_manager', cookies=cookies, headers=headers, json=json_data)
print(response.json())
# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"route":"register","email":"peerelss@gmail.com","password":"gg"}'
#response = requests.post('http://localhost:3000/api/user_manager', cookies=cookies, headers=headers, data=data)