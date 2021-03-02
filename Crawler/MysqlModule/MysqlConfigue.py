
host = '127.0.0.1'
port = 3306
username = 'kelar'
userpassword = '123456'
database = 'HuyaCrawler'

TableConfig0 = r"""
create table if not exists huya_anchor_info
(
anchor_id mediumint unsigned primary key,
anchor_name char(25) not null,
subscriber_number int default 0,
clan_name char(20) default '',
live_firse_class char(10) default '',
live_second_class char(10) default ''
);
"""
TableConfig1 = r"""
create table if not exists huya_anchor_weekly_income
(
anchor_id_with_date char(25) primary key,
anchor_id mediumint unsigned ,
weekly_income1 mediumint unsigned default 0,
weekly_income2 mediumint unsigned default 0,
weekly_income3 mediumint unsigned default 0,
weekly_income4 mediumint unsigned default 0,
weekly_income5 mediumint unsigned default 0,
weekly_income6 mediumint unsigned default 0,
weekly_income7 mediumint unsigned default 0,
weekly_income8 mediumint unsigned default 0,
weekly_income9 mediumint unsigned default 0,
weekly_income10 mediumint unsigned default 0,
weekly_income11 mediumint unsigned default 0,
weekly_income12 mediumint unsigned default 0,
weekly_income13 mediumint unsigned default 0,
weekly_income14 mediumint unsigned default 0,
weekly_income15 mediumint unsigned default 0,
weekly_income16 mediumint unsigned default 0,
weekly_income17 mediumint unsigned default 0,
weekly_income18 mediumint unsigned default 0,
weekly_income19 mediumint unsigned default 0,
weekly_income20 mediumint unsigned default 0,
weekly_income21 mediumint unsigned default 0,
weekly_income22 mediumint unsigned default 0,
weekly_income23 mediumint unsigned default 0,
weekly_income24 mediumint unsigned default 0,
weekly_income25 mediumint unsigned default 0,
weekly_income26 mediumint unsigned default 0,
weekly_income27 mediumint unsigned default 0,
weekly_income28 mediumint unsigned default 0,
weekly_income29 mediumint unsigned default 0,
weekly_income30 mediumint unsigned default 0,
weekly_income31 mediumint unsigned default 0,
weekly_income32 mediumint unsigned default 0,
weekly_income33 mediumint unsigned default 0,
weekly_income34 mediumint unsigned default 0,
weekly_income35 mediumint unsigned default 0,
weekly_income36 mediumint unsigned default 0,
weekly_income37 mediumint unsigned default 0,
weekly_income38 mediumint unsigned default 0,
weekly_income39 mediumint unsigned default 0,
weekly_income40 mediumint unsigned default 0,
weekly_income41 mediumint unsigned default 0,
weekly_income42 mediumint unsigned default 0,
weekly_income43 mediumint unsigned default 0,
weekly_income44 mediumint unsigned default 0,
weekly_income45 mediumint unsigned default 0,
weekly_income46 mediumint unsigned default 0,
weekly_income47 mediumint unsigned default 0,
weekly_income48 mediumint unsigned default 0,
weekly_income49 mediumint unsigned default 0,
weekly_income50 mediumint unsigned default 0,
constraint foreign key(anchor_id) references huya_anchor_info(anchor_id)
) ;
"""

class EnumCommand():
    def __init__(self):
        self.__sql_type = None                    # sql_type 为 string 类型，可以为 select,insert,select,update 等，更多功能组件完善
        self.__sql_command = None                 # sql 命令
    
    def setSqlType(self,sql_type = ""):
        self.__sql_type = sql_type

    def getSqlType(self):
        return self.__sql_type

    def setSqlCommand(self,sql_command = ""):
        self.__sql_command = sql_command
    
    def getSqlCommand(self):
        return self.__sql_command


## test

# a = EnumCommand()
# a.setSqlType("123")
# b = a.getSqlType()
# b = 1456
# print(a.getSqlType())
