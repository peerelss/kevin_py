url = r'http://127.0.0.1:258/?search='
url_end = r'&sort=size&ascending=0'
import json
import ctypes
import datetime
import struct
import os

# defines
EVERYTHING_REQUEST_FILE_NAME = 0x00000001
EVERYTHING_REQUEST_PATH = 0x00000002
EVERYTHING_REQUEST_FULL_PATH_AND_FILE_NAME = 0x00000004
EVERYTHING_REQUEST_EXTENSION = 0x00000008
EVERYTHING_REQUEST_SIZE = 0x00000010
EVERYTHING_REQUEST_DATE_CREATED = 0x00000020
EVERYTHING_REQUEST_DATE_MODIFIED = 0x00000040
EVERYTHING_REQUEST_DATE_ACCESSED = 0x00000080
EVERYTHING_REQUEST_ATTRIBUTES = 0x00000100
EVERYTHING_REQUEST_FILE_LIST_FILE_NAME = 0x00000200
EVERYTHING_REQUEST_RUN_COUNT = 0x00000400
EVERYTHING_REQUEST_DATE_RUN = 0x00000800
EVERYTHING_REQUEST_DATE_RECENTLY_CHANGED = 0x00001000
EVERYTHING_REQUEST_HIGHLIGHTED_FILE_NAME = 0x00002000
EVERYTHING_REQUEST_HIGHLIGHTED_PATH = 0x00004000
EVERYTHING_REQUEST_HIGHLIGHTED_FULL_PATH_AND_FILE_NAME = 0x00008000

# dll imports
everything_dll = ctypes.WinDLL(r"C:\Users\MSI\PycharmProjects\kevin_py\image\Everything64.dll")
everything_dll.Everything_GetResultDateModified.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_ulonglong)]
everything_dll.Everything_GetResultSize.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_ulonglong)]
everything_dll.Everything_GetResultFileNameW.argtypes = [ctypes.c_int]
everything_dll.Everything_GetResultFileNameW.restype = ctypes.c_wchar_p

# convert a windows FILETIME to a python datetime
# https://stackoverflow.com/questions/39481221/convert-datetime-back-to-windows-64-bit-filetime
WINDOWS_TICKS = int(1 / 10 ** -7)  # 10,000,000 (100 nanoseconds or .1 microseconds)
WINDOWS_EPOCH = datetime.datetime.strptime('1601-01-01 00:00:00',
                                           '%Y-%m-%d %H:%M:%S')
POSIX_EPOCH = datetime.datetime.strptime('1970-01-01 00:00:00',
                                         '%Y-%m-%d %H:%M:%S')
EPOCH_DIFF = (POSIX_EPOCH - WINDOWS_EPOCH).total_seconds()  # 11644473600.0
WINDOWS_TICKS_TO_POSIX_EPOCH = EPOCH_DIFF * WINDOWS_TICKS  # 116444736000000000.0


def get_time(filetime):
    """Convert windows filetime winticks to python datetime.datetime."""
    winticks = struct.unpack('<Q', filetime)[0]
    microsecs = (winticks - WINDOWS_TICKS_TO_POSIX_EPOCH) / WINDOWS_TICKS
    return datetime.datetime.fromtimestamp(microsecs)


# create buffers
filename = ctypes.create_unicode_buffer(260)
date_modified_filetime = ctypes.c_ulonglong(1)
file_size = ctypes.c_ulonglong(1)


def if_file_exist(av_id):
    everything_dll.Everything_SetSearchW(av_id)
    everything_dll.Everything_SetSort(6)
    everything_dll.Everything_SetRequestFlags(
        EVERYTHING_REQUEST_FILE_NAME | EVERYTHING_REQUEST_PATH | EVERYTHING_REQUEST_SIZE | EVERYTHING_REQUEST_DATE_MODIFIED)

    # execute the query
    everything_dll.Everything_QueryW(1)

    # get the number of results
    num_results = everything_dll.Everything_GetNumResults()

    # show the number of results
    for i in range(num_results):
        everything_dll.Everything_GetResultSize(i, file_size)
        if file_size.value > 1024 * 1024 * 400:
            return True
    return False


def if_file_exist_with_size(av_id, size):
    everything_dll.Everything_SetSearchW(av_id)
    everything_dll.Everything_SetSort(6)
    everything_dll.Everything_SetRequestFlags(
        EVERYTHING_REQUEST_FILE_NAME | EVERYTHING_REQUEST_PATH | EVERYTHING_REQUEST_SIZE | EVERYTHING_REQUEST_DATE_MODIFIED)

    # execute the query
    everything_dll.Everything_QueryW(1)

    # get the number of results
    num_results = everything_dll.Everything_GetNumResults()

    # show the number of results
    for i in range(num_results):
        everything_dll.Everything_GetResultSize(i, file_size)
        if file_size.value > 1024 * 1024 * size:
            return True
    return False


def search_file_by_key_world(fileName):
    keyword = str(fileName).replace('_', " ").replace('-', " ")
    everything_dll.Everything_SetSearchW(keyword)
    everything_dll.Everything_SetSort(6)
    everything_dll.Everything_SetRequestFlags(
        EVERYTHING_REQUEST_FILE_NAME | EVERYTHING_REQUEST_PATH | EVERYTHING_REQUEST_SIZE | EVERYTHING_REQUEST_DATE_MODIFIED)

    # execute the query
    everything_dll.Everything_QueryW(1)

    # get the number of results
    num_results = everything_dll.Everything_GetNumResults()
    result_list = []
    for i in range(num_results):
        everything_dll.Everything_GetResultFullPathNameW(i, filename, 260)
        everything_dll.Everything_GetResultDateModified(i, date_modified_filetime)
        everything_dll.Everything_GetResultSize(i, file_size)
        file_p = ctypes.wstring_at(filename)
        if os.path.exists(file_p) and os.path.isfile(file_p):
            #  print(ctypes.wstring_at(filename))
            #  print(file_size.value)
            file_name = os.path.basename(file_p)
            result_list.append({'file_path': file_p, 'size': file_size.value, 'filename': file_name})
    return result_list


import requests


def search_web_sdk(key_world):
    params = {
        's': key_world,
        'json': '1',
        'sort': 'size',
        'ascending': '0',
        'path_column': '1',
        'size_column': '1'
    }

    # 发送GET请求
    response = requests.get('http://localhost:80', params=params)
    return (response.json()['results'])


def search_file_by_name_sdk(full_name):
    everything_dll.Everything_SetSearchW(full_name)
    everything_dll.Everything_SetSort(6)
    everything_dll.Everything_SetRequestFlags(
        EVERYTHING_REQUEST_FILE_NAME | EVERYTHING_REQUEST_PATH | EVERYTHING_REQUEST_SIZE | EVERYTHING_REQUEST_DATE_MODIFIED)

    # execute the query
    everything_dll.Everything_QueryW(1)

    # get the number of results
    num_results = everything_dll.Everything_GetNumResults()
    result_list = []
    for i in range(num_results):
        everything_dll.Everything_GetResultFullPathNameW(i, filename, 260)
        everything_dll.Everything_GetResultDateModified(i, date_modified_filetime)
        everything_dll.Everything_GetResultSize(i, file_size)
        file_p = ctypes.wstring_at(filename)
        if os.path.exists(file_p) and os.path.isfile(file_p):
            file_name = os.path.basename(file_p)
            result_list.append({'file_path': file_p, 'size': file_size.value, 'filename': file_name})
    return result_list


if __name__ == '__main__':
    # js = search_web_sdk('011614_738')
    results = if_file_exist_with_size('sdsi-020', 100)
    print(results)
