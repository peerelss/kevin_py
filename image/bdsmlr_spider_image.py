# -*- coding: utf-8 -*-
import sys
import requests
import os
from bs4 import BeautifulSoup
import time
import requests

import requests

cookies = {
    'XSRF-TOKEN': 'eyJpdiI6ImorNlpaekZOTUJIQ3pPVnR0bGZzeXc9PSIsInZhbHVlIjoiTnVpYTRZWURKUCsrNkNGcmdiU3ZwcjB1MlNwS2ZUaDFLMmdtd2NyMERPVTF4bzRGZWpOTW5yTjhFdkxiV1FkTHV5SjBrb05DZ0V4dnNJXC9HaEt6T09pcnV2ZXhTUzFrWGFQbUk5WmZUZGl4K2pzTWpvU3RsQlVsUCs4MjJTSStYIiwibWFjIjoiZDFlOGVkMjM1Y2U2NjRhNjIxMmNhNWJlYzhkNzg4NzMxNWZjNDA4YzFmNDA5YWQxMDNjN2ViNDc5MTUyNjE4MiJ9',
    'bdsmlr7_session': 'eyJpdiI6IllwaFpDaVZVN2pLcmY2eG84bmdZTGc9PSIsInZhbHVlIjoiZkdGWnRlcWtaVTNSM3dSejkzUlA5XC9YRFkyNFJhSEI3RGZ1ZjlaZEFCcmdhU05zbVFDVzJZSm9DUXgyc1c1ZTBaRmJuNWRRZVwvclNmS20yVnFmQ3hcL25QcU8yNnFBdXJOTDAyaGtcL21ob2N3Yk5meEVrTFVUXC93cDJ0UENLU2RuTCIsIm1hYyI6ImZlYTkwNjIxNDVhMTMzY2M0ZTVkYWMyNGQ1ZWFkYzVjZDhlYTEwZTBkZjJlZDQxYWQ0YjI0MGIxMDkwNWRlNzQifQ%3D%3D',
    'icGpviI0IreQKMGTOvl4q57ktHGtneaEKhcQEP6y': 'eyJpdiI6Im4zR0pPOUlReW9BZG12UTg4QWNCOHc9PSIsInZhbHVlIjoiMFR0YnNWZ2JmV2pkbWdaR1NidUREZXgxTkpEbWY1SncyaTNYWkhWaWI5WjFNakdoOTBaemxacE9jbEJVY0Mwd29ic3BWd1wvQnRuQzVDWnc3RHVnMkIwOFo4eFI0MEZsRDM3dzhGZU9qT2EzZWFlZ05GT0V6d0V1SUFodHlReVBpbFpxUDJtZDlZNkN1SDkrQzBtNFA3NWU1R2RxdHgwOXJoXC9Mb1NxYlA4QnBHNlFzZGFEQmxtWkM1bG1EbHFqOW1YY2dUa0tMU095VmJtM2tCSVZrdFd5bVR6YnJhRGpmMTBKSWh5OWs4d2tPNVp5ZVM5a2xSUTQ2VTdOV2FVTmlZcU1QNmx6REE0NEdHd1YxRTZ1RmRqblJvdzJzVytYWjV5VnMwZFVlaG90aU9HUUhHXC90UktSMFFLSEtrbGZwVWFVMmtBMldaZ2dIT3FwdUJyYmplRnJHeitBdnJWY1FCU0JoXC96Y1Nmbmp1dVlhNlRsWWhDeUlaSk5KTTc0OExpXC94Z2Z1ZTVsdmMxUk1mV1BRRFVUSGtCQ1E1T3NGaVpPWFd2a0lCS2RiZjk5WWxOS29pcWd0aVJRZGkwTW9QdmFGZWZhYTBCVzJPTWFRMVwvbXVnT1Y0eFh4VDdva3pnNUNreTJxZUZJTktjVzNBN0NcL1VJalV6NkpiSk82VHZ3TzBoUWpxS053eXI1dVBLd0JVRkxxVnhyOUFMQm5udWszaFBnM0V5RzBIY0d4MmdlS2NROHN4XC9vM3VXNGhYZHJzc2F5YklQSFNZRm9wb0NHTXFmTis0NXkxTmdUejluXC9WcVVBUUdWSUNOOGZ3eXhJYjJMbVwvS3JUY2NqaDlGdHpvbHhJTmg4SG5WVDA4cWk0c0doV0pVRE9nMzZXd214WXJHaVErQ2lodmtqY0NHRXBjcW90SUY2U0FRV1FTZUR2TXBoOGJFZU5jMVVYMHFlcG8xNkRnOFdhSlpHVFwvNUd0UWxSV2pIT2pJQlhlR3ROZ0VWb2hlbndCOVYzMTJHSUthQktpRnBHZlFOSlFmeXdtQmNTc05tTThNOG9UM3BXV2l0YjBWVDl2bk9DUkdSRk1Tc0FIRlZ5UU9PbCtUa2FjUU1WZnVEOWpBMitzd0xhMjZPeHMySDRPQTlzZ0ZFeG14R2NGUlFKcFBWQjJlMitiQTdwWitLYUxcL0kwTEZSREQ2MDNOaGI3Z1RUMHdUT1M1QVc0NTg5YndxMmNiNHlacGtwK3hyVUUyQVZ0dHFHSGJnUmlLbkVOekt1amF2bitIcU5xVGxsazRPOTFLMzJXcjhVSkFHSWdiRmxsc3Z6dEVpbnBlOGM0Nm53YVNJVDNzUGpWSlVadE1ic2h0Zm1DQ1o3dHE4TnR2dkJYQWhvTjdjZjJmMnR5NTVWSkdrcjQxTGdFY2tSTUNYNlpJS3d6cFhFbzZRcnJPUHAxOVc4WFZzSkJSeDlYU2FRQUMyNmZzeDRpQzAweXFzUGpjUU9PUTlsaDVnM0lQS3dSeWJuSGFrWXhuUUh2dFhsaVhjVTNQRVRKaUdwSGx4Tm10SVlFSlVOdzRoemQ5RXJNdXNTaWI2WnFlNWY3VSsrVFk4WUJyclh3N2lBdEl5Q0F5cFljXC94RU50QllnY1hBbTFIbzJ0cGxucTQwMTdBUGxOV1JQeThpYlJXVE05dnNYQW5Tb05zM1prZitsTTlFdkY0b3dWYmp5dlc2WWpOXC9Pa3hEdDUycFlkUlBYVDJcL1hwOUJJY3NjbHY5d3EzY1lOMndJPSIsIm1hYyI6IjIwNDdlYjMyYzY0M2EwZGE1ZjYxMzIwZDk1ODY3NGFkNTc3YTUxZjkyZTM3MGMyZTdjZGZhMjI4YTNhMWY5NDMifQ%3D%3D',
    '_ga': 'GA1.2.1468065637.1646427807',
    'countVisitsFrontint': '0',
    'countVisits': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-CSRF-TOKEN': '1XwxS6Lk4qlUiLXfwbZWYjS8k34OWM36ILB7PKCT',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://happybondageclub.bdsmlr.com',
    'Connection': 'keep-alive',
    'Referer': 'https://happybondageclub.bdsmlr.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Cache-Control': 'max-age=0',
}

data1 = {
    'scroll': '20',
    'timenow': '2022-03-05 22:16:51',
    'last': '475716261'
}


def get_pic_url_from_url(data):
    print(data['last'] + "   " + data['scroll'])
    response = requests.post('https://happybondageclub.bdsmlr.com/infinitepb2/happybondageclub', headers=headers,
                             cookies=cookies,
                             data=data)
    soup_jpg = BeautifulSoup(response.content, 'lxml').find_all('img')
    f = open('/media/kevin/Backup/bdsmlr/' + 'happybondageclub_bdsmlr.txt', 'a')
    for s in soup_jpg:
        f.write(s['src'] + '\n')
        print(s['src'])
    f.close()
    soup = BeautifulSoup(response.content, 'lxml').find_all("div", {"class": "countinf"})

    data['scroll'] = int(data['scroll']) + 20
    data['last'] = soup[-1]['data-id']
    data['timenow'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if len(soup_jpg) < 1:
        return False
    else:
        return True


def get_next_page_from_url():
    pass


if __name__ == "__main__":
    while get_pic_url_from_url(data1):
        pass
