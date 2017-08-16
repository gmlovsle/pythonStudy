#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
age_of_oldboy = 56
count = 0
while count < 3:
    guess_age = int(input("guess age:"))

    if guess_age == age_of_oldboy:
        print("You got it!")
        break
    elif guess_age < age_of_oldboy:
        print("Think bigger!")
    else:
        print("Think smaller!")
    count+=1

    if count == 3:
        countine_confirm=input("Do you want to keep guessing? Y or N")
        if countine_confirm == "n" or countine_confirm == "N":
            print("Goodbye")
            break
        if countine_confirm == "y" or countine_confirm == "Y":
            count = 0
else:
    print("You have tried too many times..")
