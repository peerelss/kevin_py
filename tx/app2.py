import requests

cookies = {
    '_ga': 'GA1.2.906589744.1673320346',
    'ANTSENTRY-LNG': 'zhtw',
    'service_ticket': 'Ticket-6e020325a47671a6da0d172d237b60b20b7ace75b9f1c82663c81c93edfed917',
    '_gid': 'GA1.2.728198868.1680914113',
    'timezone': 'America/Los_Angeles',
    'ANTSENTRYID': 'YmZjZDg5NDktOGMyNS00N2VhLTk1ODYtY2RlZjQ5Y2MyNWRk',
    '_gat_gtag_UA_145823397_1': '1',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Ant-Token': '21AA32BFB1EF4ADBA0B5C7626EED217A',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga=GA1.2.906589744.1673320346; ANTSENTRY-LNG=zhtw; service_ticket=Ticket-6e020325a47671a6da0d172d237b60b20b7ace75b9f1c82663c81c93edfed917; _gid=GA1.2.728198868.1680914113; timezone=America/Los_Angeles; ANTSENTRYID=YmZjZDg5NDktOGMyNS00N2VhLTk1ODYtY2RlZjQ5Y2MyNWRk; _gat_gtag_UA_145823397_1=1',
    'Referer': 'https://cloud.minerplus.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.34',
    'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'isOnline': 'N',
    'minerFarmId': '433940698199284360',
    'queryType': '0',
    'queryKey': '',
    'page': '1',
    'pageSize': '500',
    'zoneId': '434291821984662228',
}

response = requests.get('https://cloud.minerplus.com/webapi/1/mn/miner/query', params=params, cookies=cookies,
                        headers=headers)
print(response.json()['data'])
