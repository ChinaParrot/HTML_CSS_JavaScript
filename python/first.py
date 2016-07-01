#/usr/bin/env python
#-*- coding:utf-8 -*-
x=2
y=3
print id(x)
print id(y)
x=y
print id(x)
print id(y)

name = raw_input('请输入你的名字：')
age = int(raw_input("age:"))
job = raw_input('job:')
salary = raw_input('salary:')

print '''
Personal information of %s:
    Name: %s
    Age: %d
    Job: %s
    Salary: %s    
----------------------------    
''' % (name,name,age,job,salary)




