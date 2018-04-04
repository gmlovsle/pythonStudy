# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"


import re

line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print ("searchObj.group() : ", searchObj.groups())

else:
   print ("Nothing found!!")


