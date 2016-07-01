#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
实现：
输入用户密码
认证成功后显示登录信息
错误三次锁定
'''
import sys
retry_limit = 3
retry_count = 0
account_file = 'accounts.txt'
lock_file = 'account_lock.txt'

while retry_count < retry_limit:
    username = raw_input('Username:')
    lock_check = file(lock_file)#打开文件lock_file
    for line in lock_check.readlines():
        line = line.split()
        if username == line[0]:
            sys.exit('User %s is locked!' %username)
    password = raw_input('Password:')
    f = file(account_file,'rb')#打开账户文件
    match_flag = False
    for line in f.readlines():
        user,passwd = line.strip('\n').split()#去掉每行多余的\n并把这一行按空格分成两列，
        #分别赋值user,passwd两个变量
        if username == user and password ==passwd:
            print 'Match!',username
            match_flag = True#相等就把循环外的match_flag变量改为True
            break #直接跳出本循环
    f.close()
    if match_flag == False:
        print "User unmatched!"
        retry_count += 1
    else:
        print "Welcome login jqlinux system!"
else:
    print 'Your account is locked!'
    f = file(lock_file,'ab')
    f.write(username+'\n')
