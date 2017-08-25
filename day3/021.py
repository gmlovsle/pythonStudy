#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
#!/usr/bin/env python
#_*_conding:utf-8_*_

import sys

f=open('015.txt','r',encoding='utf-8')
f_new=open('lyrics_new','w+',encoding='utf-8')
find_str=sys.argv[1]
replace_str=sys.argv[2]
for line in f:
    if find_str in line:
        line=line.replace(find_str,replace_str)
    f_new.write(line)
f.close()
f_new.close()