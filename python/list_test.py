#!/usr/bin/env python
#-*- coding:utf-8 -*-

name = ['a','b',2,'c','d',2,'s','ssss',1,3,5,2,20]

first_pos = 0
for i in range(name.count(2)):
    new_list = name[first_pos:]
    next_pos = new_list.index(2) + 1
    print 'Find postion:',first_pos + new_list.index(2)
    first_pos += next_pos

pos = 0
for y in range(name.count(2)):
    if pos == 0:
        pos = name.index(2)
    else:
        pos = name.index(2,pos + 1)
    print pos
