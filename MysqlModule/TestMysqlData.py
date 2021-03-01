import MysqlData

testObject = MysqlData.MysqlManipulate()
testObject.connectDataBase()

## 命令执行测试
# try:
#     ## 测试一个 sql 包含多条命令
#     testObject.executeSqlCommand('insert','insert into huya_anchor_info value (1,"li","ming","tian"); insert into huya_anchor_info value (2,"wang","yang","ming");',True)

#     ## 测试 args 使用
#     affect_rows_number = testObject.executeSqlCommand('insert','insert into huya_anchor_info values %s;',False,(6,"4056",123,"ghfd"))
#     print(affect_rows_number)
# except Exception as e:
#     print(e)    


## insert datas
try:
    ## 一次插入多条数据
    affect_rows_number = testObject.insertManyDatas('huya_anchor_info',((1,'4',2,'5'),(3,"5",5,"46")))
    print(affect_rows_number)
except Exception as e:
    print(e)




## select datas


## update datas


## delete datas
# try:
#     # 删除所有行数据
#     testObject.executeSqlCommand('delete','delete from huya_anchor_info;')
# except Exception as e:
#     print(e)
