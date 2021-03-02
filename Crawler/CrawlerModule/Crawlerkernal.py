import os

from .AnchorInform import AnchorInform 
from ..CrawlerModule import AuxiliaryPageAnalyze as AuxiliaryPageAnalyze

def getAllAnchorInform(hall_first_page_url = None,hall_page_file_package = None):
    '''
    获取所有直播间的信息，返回 AnchorInform 的 list
    '''
    ## 获取所有大厅界面信息
    files_path_list = None
    if hall_first_page_url != None:
        ## 如果学会了怎么获取下一页的大厅信息，再编写这一部分
        pass
    
    def getFilePath(file_package):
        return [os.path.join(root,file_name) for root,dirts,files in os.walk(file_package) for file_name in files ]
        

    if  hall_page_file_package != None:
        ## 已经下载好的所有所有大厅网页代码的文件夹
        files_path_list = getFilePath(hall_page_file_package)


    ## 写入所有直播间的 id 信息到文件中
    livehouse_id_file = os.getcwd() + r'\Crawler\CrawlerModule\huya_anchor_live_links.txt'
    for file_path in files_path_list:
        AuxiliaryPageAnalyze.getUrlFromEachHallPage(file_path,livehouse_id_file)

    ## 从直播间见面中获取主播的信息
    anchor_inform_list = None
    anchor_inform_list = AuxiliaryPageAnalyze.fromUrlsGetAnchorInform(livehouse_id_file)

    return anchor_inform_list