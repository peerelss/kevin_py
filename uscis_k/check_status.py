import requests

cookies = {
    'TS0152f920': '01ff0b08602b4a78756df78a5bd5a3399c5e1ee36c31641aa5012c82b8b20c9711034d2a4964ac7af7a5fe3cce614bd5a3fd69d63b',
    'NIT_UiState': 'DISP^%^3Dclosed^%^26AgentLaunchType^%^3Dembedded^%^26ProactiveOffer^%^3Dfalse',
    'NIT_SessionState': 'User^%^3D4cca50fe-8655-4db2-b2a4-1149ef5b1ccd^%^26SessionID^%^3D94210981-4c79-4858-bd18-8a5809be53c3^%^26SoundEnabled^%^3Dfalse^%^26PlayPrvOnNav^%^3Dfalse^%^26LastPrvUrl^%^3D^%^26TTSInstance^%^3D^%^26TTSMimeTypes^%^3D^%^26CurLang^%^3D^%^26LastMin^%^3D0^%^26LastRev^%^3D0^%^26InlineSurveyState^%^3D0^%^26ChatState^%^3DDisconnected^%^26Unread^%^3D0^%^26ChatPos^%^3D0',
    'TS014337b4': '01e4295156e42cf93778f0ff56c1247026712a9dbe39320d5f120320a82e3e863b914ef3d02d2490643aca9d7f420fe625c4c440e1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://egov.uscis.gov/',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJVSV9VU0VSIiwiaWF0IjoxNjk2MDkxNjI3LCJleHAiOjE2OTYxNzgwMjd9.2FQK66PxEVASq1IrPVB0Uoa3fob_U8UwE1ZWsE6Itz8',
    'Connection': 'keep-alive',
    # 'Cookie': 'TS0152f920=01ff0b08602b4a78756df78a5bd5a3399c5e1ee36c31641aa5012c82b8b20c9711034d2a4964ac7af7a5fe3cce614bd5a3fd69d63b; NIT_UiState=DISP^%^3Dclosed^%^26AgentLaunchType^%^3Dembedded^%^26ProactiveOffer^%^3Dfalse; NIT_SessionState=User^%^3D4cca50fe-8655-4db2-b2a4-1149ef5b1ccd^%^26SessionID^%^3D94210981-4c79-4858-bd18-8a5809be53c3^%^26SoundEnabled^%^3Dfalse^%^26PlayPrvOnNav^%^3Dfalse^%^26LastPrvUrl^%^3D^%^26TTSInstance^%^3D^%^26TTSMimeTypes^%^3D^%^26CurLang^%^3D^%^26LastMin^%^3D0^%^26LastRev^%^3D0^%^26InlineSurveyState^%^3D0^%^26ChatState^%^3DDisconnected^%^26Unread^%^3D0^%^26ChatPos^%^3D0; TS014337b4=01e4295156e42cf93778f0ff56c1247026712a9dbe39320d5f120320a82e3e863b914ef3d02d2490643aca9d7f420fe625c4c440e1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

response = requests.get('https://egov.uscis.gov/csol-api/case-statuses/LIN2390217318', cookies=cookies, headers=headers)

print(response.json()['CaseStatusResponse']['detailsEs'])
