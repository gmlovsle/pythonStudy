#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang


name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input(("Salary:"))

info = """
-----info of %s-----
 Name:%s
 Age:%d
 Job:%s
 Salary:%s
""" % (name,name,age,job,salary)

info2 = """
-----info of {_name}-----
 Name:{_name}
 Age:{_age}
 Job:{_job}
 Salary:{_salary}
""" .format(_name=name,_age=age,_job=job,_salary=salary)

info3 = """
-----info of {0}-----
 Name:{0}
 Age:{1}
 Job:{2}
 Salary:{3}
""" .format(name,age,job,salary)

print(type(age),type(str(age)))
print (info)
print (info2)
print (info3)

#优选info2