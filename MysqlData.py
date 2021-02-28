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
                    for table_configue in dir(MysqlConfigue):
                        if "TableConfig" in table_configue:
                            cursor.execute(getattr( MysqlConfigue,table_configue))
        pass

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
    
    def tempExecuteSqlCommand(self,command_type,command = "",*args):
        '''
        临时的数据库操作接口；这里得分割为多个命令形式
        :param command_type: 什么类型命令 select,insert,select,updata 等？
        :param command: 数据库操作命令，字符串
        :param *args:命令中的参数，元组形式
        '''
        if self.__db == None:
            self.connectDataBase()
        with self.__db:
            with self.__db.cursor() as cursor:
                cursor.execute(command.format(args))
            # self.__db.commit()
    
    def executeSqlCommand(self,commandObject):
        if commandObject.getSqlType == "":
            pass


        cursor = self.getCursor()
        cursor.execute(command)
        data = cursor.fetchone()
        return data

## test

a = MysqlManipulate()
a.connectDataBase()

