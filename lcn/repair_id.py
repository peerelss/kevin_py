# -*- coding: utf-8 -*-
import os

file_aaa = r'C:\lcn\aaa.txt'
file_all = r'C:\lcn\all.txt'
file_baofei = r'C:\lcn\baofei.txt'

line_aaa = []
line_all = []
line_baofei = []

with open(file_aaa, 'r') as file_aa:
    for line in file_aa.readlines():
        line = line.strip('\n')
        line_aaa.append(line)

with open(file_all, 'r') as file_al:
    for line in file_al.readlines():
        line = line.strip('\n')
        line_all.append(line)

with open(file_baofei, 'r') as file_bao:
    for line in file_bao.readlines():
        line = line.strip('\n')
        line_baofei.append(line)
'''for i in line_all:
    if i in line_baofei:
        pass
    elif i in line_aaa:
        pass
    else:
        print(i)'''

if '5120305501035' in line_aaa:
    print('aaa')

if '5120305501035' in line_baofei:
    print('baofei')


