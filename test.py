## 字符测试
# a = "123"
# a += "456"
# print(a[0:-1])
a = "%d,%s,%s,%s"%(1,"","2","d")
print(a)


## 列表测试
# a = [1,2,3]
# a += a
# print(a)

# a.append(a)
# print(a[6][2])


##元组测试
# a = tuple([1,2,3])
# a += (4,5,6)
# print(a)


## format 只能用在 "{}".format 的形式
# a = "ssndlf {0},{1}".format(2,3)
# b = "{0},{1}"
# b.format(4,5)
# print(a,b)



## 路径相关
# import os
# hall_page_file_package = os.getcwd()
# hall_page_file_package += '\\HuyaHallPage'
# for root,dirts,files in os.walk(hall_page_file_package):
#     print(root,type(root))
#     print(dirts,type(dirts))
#     print(files,type(files))



# ## 字典测试
# a = {}
# a['b'] = None
# a['a'] = 0
# print(a)


## readlines() 函数测试
# file_test = './huya_anchor_live_links.txt'
# list_temp = None
# with open(file_test,'r') as f:
#     list_temp = [line.replace('\n','') for line in f.readlines()]
# with open(file_test,'w') as f:
#     for name in list_temp:
#         f.write(name)
#         f.write('\n')


## 获取当前时间
# import time
# print(str(int(time.time())))



## 文件函数测试
# import Crawler.MysqlModule.TestMysqlData

# import CrawlerModule.AnchorInform