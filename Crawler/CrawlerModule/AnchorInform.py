
class AnchorInform():
    def __init__(self):
        ## 整数
        self.anchor_id = 0      
        self.anchor_name = ""
        ## 整数
        self.subscriber_number = 0
        self.clan = ""
        ## 一级分类
        self.live_first_class = "" 
        self.live_second_clsss = ""
        ## 整数列表
        self.anchor_weekly_income = None

    def showAllInform(self):
        # 测试用，查看数据
        with open('./anchor_information.txt','a',encoding='utf-8') as f:
            f.write(str(self.anchor_id) + '  '+self.anchor_name+ '  '+str(self.subscriber_number)+ '  '+self.clan+ '  '+self.live_first_class+ '  '+self.live_second_clsss+  ' \n')
        print(self.anchor_id,self.anchor_name,self.subscriber_number,self.clan,self.live_first_class,self.live_second_clsss,self.anchor_weekly_income)
    
    def saveInform(self):
        
        pass
