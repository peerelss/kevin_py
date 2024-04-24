import os
from image.sdk_every_thing_http import search_file_by_key_world


def search_file_by_dir(file_path):
    if os.path.isdir(file_path):
        for file in os.listdir(file_path):
            print(file)


if __name__ == "__main__":
    # getallfile(rootdir)
    search_file_by_dir(r'f:\after\set\TranniesInTrouble1.com')
