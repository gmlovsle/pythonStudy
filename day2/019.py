#!/usr/bin/env puthon
# -*- coding:utf-8 -*-
# Author:Genming Zhang
data = {
    '成都市':{
        "双流区":{
            "东升镇":["东立国际花城","景茂名都","优品时代"],
            "华阳镇":["锦江花园","南湖国际社区"]
        },
        "新都区":{
            "三河镇":["花园小区","锦绣前城"],
            "泰新镇":{"汉邦成都"},
            "龙虎镇":{"龙虎小区","梁家老院子"},
        },
        "龙泉驿区":{
            "茶店镇":["龙湖御景"],
            "大面镇":{"洪河城市花园","百悦城","炜岸城","龙城1号"},
            "同安镇":{"明星花苑","东方虹花苑"},
        },
    },
    '眉山市':{
        "仁寿县":{
            "文林镇":["景观名都","景观贵都","景观兴城"],
            "满井镇":{"城南名苑","城南"},
        },
        "东坡区":{
            "止戈镇":["止戈1号院","止戈2号院","止戈3号院","止戈4号院"],
            "中保镇":{"中保1号院","中保2号院"},
        },
         "彭山区":{
            "止戈镇":["止戈1号院","止戈2号院","止戈3号院","止戈4号院"],
            "中保镇":{"中保1号院","中保2号院"},
        },
        "洪雅县":{
            "止戈镇":["止戈1号院","止戈2号院","止戈3号院","止戈4号院"],
            "中保镇":{"中保1号院","中保2号院"},
        },
        "丹棱县":{
            "止戈镇":["止戈1号院","止戈2号院","止戈3号院","止戈4号院"],
            "中保镇":{"中保1号院","中保2号院"},
        },
        "青神县":{
            "止戈镇":["止戈1号院","止戈2号院","止戈3号院","止戈4号院"],
            "中保镇":{"中保1号院","中保2号院"},
        },
    },
    '乐山市':{
        "犍为县":{
            "玉津镇":["玉津1号","玉津2号"],
            "清溪镇":{"清溪1号","清溪2号"},
            "罗城镇":{"罗城1号","罗城2号"},
        },
        "井研县":{
            "研城镇":["研城1号","研城2号"],
            "马踏镇":{"马踏1号","马踏2号"},
            "研经镇":{"研经1号","研经2号"},
        },
        "沐川县":{
            "沐溪镇":["沐溪1号","沐溪2号"],
            "永福镇":{"永福1号","永福2号"},
            "大楠镇":{"大楠1号","大楠2号"},
        },
    },
}
def menu(data,number):
    flag = 1
    while flag==1:
        for i in data:
            a = "\t" + i
            print(a)
        choice = input("选择进入%s>>:" %number)
        if choice in data:
            menu(data[choice],number+1)
        if choice == "b":
            break
        elif choice == "q":
            flag = 0
menu(data,1)