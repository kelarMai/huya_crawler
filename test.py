import base64

test = MysqlManipulate()
sql_command = '''
select picture from staff where staff_id=1;
'''

pictureData = test.executeSqlCommand(sql_command)
picture = base64.b64decode(pictureData[0])
with open("new.jpg",'wb') as fb:
    fb.write(picture)