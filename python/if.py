#/usr/bin/env python
#-*- coding:utf-8 -*-
name = raw_input('请输入你的名字：')
age = int(raw_input("age:"))
job = raw_input('job:')
salary = raw_input('salary:')


if age >30:
    msg ='\033[32; You are too old!\033[0m'
else:
    msg ='You are still quite young,go hook up some girls or boys.'

print '''
Personal information of %s:
    Name: %s
    Age: %d
    Job: %s
    Salary: %s    
    msg: %s
----------------------------    
''' % (name,name,age,job,salary,msg)