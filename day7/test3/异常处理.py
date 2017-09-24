# -*- coding:utf-8 -*-
#__author__ = "Genming Zhang"

names = ["zhanggenming","yangshenglan"]
data = {}

try:
    open("dd","f")
    names[3]
    data["name"]

except KeyError as f:#抓住单个错误
    print("Don't have the key",f)
except IndexError as I:
    print("IndexError",I)
except Exception as U:#其他错误
    print("Unknown error",U)

else:#不出错
    print("Everything is okay.")

finally:#不管出错不出错
    print("Whatever yes or no,do it.")
# except (KeyError,IndexError) as f:#抓住多个错误
#     print("Don't have the key",f)

# except Exception as b:#抓住所有的错误
#     print("Error",b)