import sys
import requests

cookies = {
    '_ga': 'GA1.2.906589744.1673320346',
    'timezone': 'America/Los_Angeles',
    'ANTSENTRY-LNG': 'zhtw',
    '_gid': 'GA1.2.1725814232.1674800620',
    'ANTSENTRYID': 'ZTQ5MjkwMGEtYTI2Zi00YzFjLWFkNDEtN2E2NDJiNzI2ZGEz',
    'service_ticket': 'Ticket-5c25ecdb4742268e346fc2974be9de92e2196197a4310b200145b7299d34b21d',
    '_gat_gtag_UA_145823397_1': '1',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Ant-Token': '98CF8297997E4140A5991F51D56EA962',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga=GA1.2.906589744.1673320346; timezone=America/Los_Angeles; ANTSENTRY-LNG=zhtw; _gid=GA1.2.1725814232.1674800620; ANTSENTRYID=ZTQ5MjkwMGEtYTI2Zi00YzFjLWFkNDEtN2E2NDJiNzI2ZGEz; service_ticket=Ticket-5c25ecdb4742268e346fc2974be9de92e2196197a4310b200145b7299d34b21d; _gat_gtag_UA_145823397_1=1',
    'Referer': 'https://cloud.minerplus.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'isOnline': 'Y',
    'minerFarmId': '433940698199284360',
    'queryType': '0',
    'queryKey': '',
    'page': '1',
    'pageSize': '10',
}

response = requests.get('https://cloud.minerplus.com/webapi/1/mn/miner/query', params=params, cookies=cookies,
                        headers=headers)

if __name__ == '__main__':
    for i in range(6812, 6950):
        print('https://legsworld.net/UpdatesNew/Previews-1212x1644/' + str(i) + '.jpg')
