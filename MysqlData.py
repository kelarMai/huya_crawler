import pymysql
import MysqlConstantImformation

class MysqlManipulate():
    __host = MysqlConstantImformation.host
    __port = MysqlConstantImformation.port
    __database = MysqlConstantImformation.database
    __username = MysqlConstantImformation.username
    __userpassword = MysqlConstantImformation.userpassword
    
    def __init__(self):
        self.db = None
        self.cursor = None
        pass

    def __delattr__(self):
        if self.db != None:
            self.db.close()
            self.db = None

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
        self.db = pymysql.connect(user=MysqlManipulate.__username , password = MysqlManipulate.__userpassword , host = MysqlManipulate.__host,database = MysqlManipulate.__database)
        # , port = MysqlManipulate.__port
        pass

    def getCursor(self):
        if self.db == None:
            self.connectDataBase()
        if self.cursor == None:
            self.cursor = self.db.cursor()
        return self.cursor
    
    def killCurosr(self):
        self.cursor.close()
        self.cursor = None
    
    # def tempExecuteSqlCommand(self,command_type,command = "",*args = ()):
    #     '''
    #     临时的数据库操作接口；这里得分割为多个命令形式
    #     :param command_type: 什么类型命令 select,insert,select,updata等？
    #     :param command: 数据库操作命令，字符串
    #     :param *args:命令中的参数，元组形式
    #     '''
    #     if self.db == None:
    #         self.connectDataBase()
    #     with self.db:
    #         with self.db.cursor() as cursor:
    #             cursor.execute(command.format(args))
    #         # self.db.commit()
    
    def executeSqlCommand(self,command = ""):
        cursor = self.getCursor()
        cursor.execute(command)
        data = cursor.fetchone()
        return data




