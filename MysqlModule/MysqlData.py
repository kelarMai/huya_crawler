import pymysql
import MysqlConfigue

class MysqlManipulate():
    __host = MysqlConfigue.host
    __port = MysqlConfigue.port
    __database = MysqlConfigue.database
    __username = MysqlConfigue.username
    __userpassword = MysqlConfigue.userpassword
    
    def __init__(self):
        self.__db = None
        self.__cursor = None
        pass

    def __del__(self):
        self.killCurosr()
        self.clossDataBase()        
            

    @staticmethod
    def changeUserInformation(newname = None,newpassword = None,port = None,database = None):
        '''
        需要使用其他用户来连接数据库时调用
        :param newname: 新用户的名称
        :param newpassword: 新用户的密码
        :param port：新端口，数字
        :param database：新数据库的名称
        '''
        if newname != None:
            MysqlManipulate.__username = newname
        if newpassword != None:
            MysqlManipulate.__userpassword = newpassword
        if port != None:
            MysqlManipulate.__port = port
        if database != None:
            MysqlManipulate.changeDataBaseName(database)
        
    
    @staticmethod
    def changeDataBaseName(new_database_name = None):
        '''
        更换数据库
        :param new_database_name：新数据库的名称
        '''
        if new_database_name != None:
            MysqlManipulate.__database = new_database_name

    def createTable(self,cursor):
        for table_configue in dir(MysqlConfigue):
            if "TableConfig" in table_configue:
                cursor.execute(getattr( MysqlConfigue,table_configue))

    def connectDataBase(self):
        self.__db = pymysql.connect(user=MysqlManipulate.__username , password = MysqlManipulate.__userpassword , host = MysqlManipulate.__host)
        with self.__db.cursor() as cursor:
            try:
                cursor.execute("use {0};".format(MysqlManipulate.__database))
            except Exception as e:
                # print(type(e.args))
                if e.args[0] == 1049:
                    ## 没有该数据库
                    create_database_sql = " create database if not exists {0}; ".format(MysqlManipulate.__database)
                    cursor.execute(create_database_sql)
                    cursor.execute("use {0};".format(MysqlManipulate.__database))
                    self.createTable(cursor)                    

    def clossDataBase(self):
        if self.__db != None:
            self.__db.close()
            self.__db = None

    def getCursor(self):
        if self.__db == None:
            self.connectDataBase()
        if self.__cursor == None:
            self.__cursor = self.__db.cursor()
        return self.__cursor
    
    def killCurosr(self):
        if self.__cursor != None:
            self.__cursor.close()
            self.__cursor = None
    
    def executeSqlCommand(self,command_type,command = "",sql_many = False,*args):
        '''
        param: command_type sql 类型，select insert update delete 等
        param: command sql语句
        :param *args:string 的 %s 类型字符串转换参数，
            参考 https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.Cursor.execute
        :param sql_many 是否一次执行多条 sql 命令
        '''
        cursor = self.getCursor()
        try:
            if command_type == "select":
                cursor.execute(command,args)
                return cursor.fetchall()
            else:
                ## execute 一次只能执行一条 sql 操作
                ## executemany 一次必须执行多条 sql 操作
                affect_rows_number = None
                if sql_many == True:
                    affect_rows_number = cursor.executemany(command,args)
                else:
                    affect_rows_number = cursor.execute(command,args)
                self.__db.commit()
                return affect_rows_number
        except Exception as e:
            if e.args[0] == 1062:
                ## 主键重复
                print("Error: {0}".format(e.args[1]))

    def tempExecuteSqlCommand(self,command_type,command = "",sql_many=False,*args):
        '''
        临时的数据库操作接口；
        :param command_type: 什么类型命令 select,insert,select,updata 等？
        :param command: 数据库操作命令，字符串
        :param *args:string 的 %s 类型字符串转换参数，
            参考 https://pymysql.readthedocs.io/en/latest/modules/cursors.html#pymysql.cursors.Cursor.execute
        :param sql_many 是否一次执行多条 sql 命令
        '''
        if self.__db == None:
            self.connectDataBase()
        with self.__db:
            with self.__db.cursor() as cursor:
                if command_type == "select":
                    cursor.execute(command,args)
                    return cursor.fetchall()
                else:
                    affect_rows_number = None
                    if sql_many == True:
                        affect_rows_number = cursor.executemany(command,args)
                    else:
                        affect_rows_number = cursor.execute(command,args)
                    self.__db.commit()
                    return affect_rows_number

    def insertManyDatas(self,tabel_name,data_tuples = None):
        '''
        :param table_name 表名
        :param data_tuples 二维元组数据
        '''
        datas_string = ""
        data_format = '(%d,"%s",%d,%s),'
        data_string = None
        for data_tuple in data_tuples:
            data_string = data_format % data_tuple
            datas_string += data_string
        datas_string = datas_string[:-1]
        insert_command = "insert into {0} values {1};".format(tabel_name,datas_string)
        print(insert_command)
        return self.executeSqlCommand('insert',insert_command)

