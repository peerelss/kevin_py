import os
from image.sdk_every_thing_http import search_file_by_name_sdk
import time
from bt4g.juanzi import print_progress_bar
def search_file_by_name(file_path, file_name):
    file_o = os.path.join(file_path, file_name)
    results = search_file_by_name_sdk(file_name)
    result_big = list(filter(lambda x: x['size'] > 1024 * 1024 * 2 and x['filename'] == file_name , results))
    for re in result_big:
        if os.path.samefile(file_o, re['file_path']):
            pass
        else:
            os.remove(re['file_path'])
            print('remove duplicate file ' + re['file_path'])
    time.sleep(0.1)


def display_file_by_dir(file_path):
    if os.path.isdir(file_path):
        file_list = os.listdir(file_path)
        for file in file_list:
            if not str(file).endswith('.jpg') and not str(file).endswith('.gif'):
                search_file_by_name(file_path, file)
                print_progress_bar(file_list.index(file) + 1, len(file_list), prefix='Progress:',
                                   suffix='Complete ',
                                   length=100)


if __name__ == "__main__":
    # getallfile(rootdir)
    display_file_by_dir(r'f:\after\eu')
    # search_file_by_name(r'F:\after\set\TranniesInTrouble1.com', 'star_nine_domme01_lrg.wmv')
