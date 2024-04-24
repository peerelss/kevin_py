import pymongo
import redis
import requests
from bs4 import BeautifulSoup
import re
import pymongo
from image.sdk_every_thing_http import search_file_by_key_world

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["t66y_av_rm"]
mycol = mydb['t66y_av_rm']

import sys
import time


def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    sys.stdout.flush()
    # Print New Line on Complete
    if iteration == total:
        print()


# magnet:?xt=urn:btih:3c233f700f4339e4ab703c27d47efd0306f6d23d&dn=MDYD-797-U&tr=http://sukebei.tracker.wf:8888/announce&tr=udp://tracker.archlinux.org.theoks.net:6969/announce&tr=udp://tracker.openbittorrent.com:6969&tr=http://tracker.tasvideos.org:6969/announce&tr=udp://tracker.leech.ie:1337/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://tracker.coppersurfer.tk:6969/announce&tr=udp://tracker.internetwarriors.net:1337&tr=udp://tracker.internetwarriors.net:1337/announce&tr=udp://open.stealth.si:80/announce&tr=udp://9.rarbg.me:2710/announce&tr=udp://9.rarbg.me:2710&tr=http://anidex.moe:6969/announce&tr=http://freerainbowtables.com:6969/announce&tr=http://www.freerainbowtables.com:6969/announce&tr=udp://9.rarbg.com:2830/announce&tr=http://tracker2.itzmx.com:6961/announce&tr=http://tracker.etree.org:6969/announce&tr=http://www.thetradersden.org/forums/tracker:80/announce.php&tr=udp://udp-tracker.shittyurl.org:6969/announce&tr=https://tracker.shittyurl.org/announce&tr=http://tracker.shittyurl.org/announce&tr=udp://bt.firebit.org:2710/announce&tr=http://bt.firebit.org:2710/announce&tr=udp://exodus.desync.com:6969/announce&tr=udp://tracker.torrent.eu.org:451/announce&tr=http://sukebei.tracker.wf:8888/announce
if __name__ == '__main__':
    results = search_file_by_key_world('011614_738')
    print(results)
