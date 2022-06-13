import sys
import requests
import os

dir=r'C:\Users\kevin\legsworld\\'

for i in reversed(range(1350,6766)):
    if os.path.exists(dir+str(i)+'.jpg'):
        pass
    else:
        print("https://legsworld.net/UpdatesNew/Previews-1212x1644/" + str(i) + '.jpg')
