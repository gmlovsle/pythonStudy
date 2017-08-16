#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang


age_of_oldboy = 56

guess_age = int(input("guess age:"))

if guess_age == age_of_oldboy:
    print("You got it!")
elif guess_age < age_of_oldboy:
    print("Think bigger!")
else:
    print("Think smaller!")