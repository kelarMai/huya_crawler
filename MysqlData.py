import pymysql

host = 'localhost'
port = 3306
username = 'kelar'
userpassword = '123456'
database = 'huya_crawler'



create_data_base = '''

'''

class MysqlManipulate():
    __host = host
    __port = port
    __database = database
    __username = username
    __userpassword = userpassword
    
    def __init__(self):
        self.db = None

        pass

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
        db = pymysql.connect(user=MysqlManipulate.__username , password = MysqlManipulate.__userpassword , port = MysqlManipulate.__port , database = MysqlManipulate.__database)

        pass

