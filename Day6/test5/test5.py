#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

class school(object):
    members = 0
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self,stu_obj):
        print("%s学员注册手续"%stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        print("雇佣新员工%s"%staff_obj.name)
        self.staffs.append(staff_obj)

class school_member(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass

class teacher(school_member):
    def __init__(self,name,age,sex,salary,course):
        super(teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
           -----Info of Teacher:%s -----
            Name:%s
            Age:%s
            Sex:%s
            Salary:%s
            Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))
    def teach(self):
        print("%s is teaching course [%s]"%(self.name,self.course))

class student(school_member):
    def __init__(self,name,age,sex,stu_id,grade):
        super(student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
           -----Info of Student:%s -----
            Name:%s
            Age:%s
            Sex:%s
            Stu_id:%s
            Grade:%s
        '''%(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))

    def pay_tution(self,amount):
        print("%s has paid tution for $%s"%(self.name,amount))

s = school("城北小学","仁寿")

t1 = teacher("杨",23,"女",5000,"数学")
t2 = teacher("张",24,"男",5000,"物理")
s1 = student("李强",11,"男",45,"数学")
s2 = student("刘佳",12,"男",44,"物理")

s.hire(t1)
s.enroll(s1)
s.enroll(s2)

print(s.students)
print(s.staffs)
s.staffs[0].teach()
for stu in s.students:
     stu.pay_tution(5000)