#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
age_of_oldboy = 56
count = 0
for count in range(0,3):
    guess_age = int(input("guess age:"))

    if guess_age == age_of_oldboy:
        print("You got it!")
    elif guess_age < age_of_oldboy:
        print("Think bigger!")
    else:
        print("Think smaller!")

count = 0
while count <3:
    guess_age = int(input("guess age:"))

    if guess_age == age_of_oldboy:
        print("You got it!")
        break
    elif guess_age < age_of_oldboy:
        print("Think bigger!")
    else:
        print("Think smaller!")
    count+=1

else:
    print("You have tried too many times..")