import os
import time

import Crawler.MysqlModule.MysqlData as MysqlData
import Crawler.CrawlerModule.Crawlerkernal as Crawlerkernal

if __name__ == "__main__":
    mysql_object = MysqlData.MysqlManipulate()

    ## 从大厅界面获取所有主播的信息
    hall_page_file_package = os.getcwd()
    hall_page_file_package += '\\HuyaHallPage'
    # print(hall_page_file_package)
    anchor_inform_list = Crawlerkernal.getAllAnchorInform(hall_page_file_package=hall_page_file_package)
    print("main: anchor_inform_list:")
    print(len(anchor_inform_list))

    ## 测试用，查看数据
    # for anchor in anchor_inform_list:
    #     anchor.showAllInform()
    

    ## 把主播的对象数据处理一下，存储到 mysql 中
    huya_anchor_info_table_format = '(%d,"%s",%d,"%s","%s","%s"),'
    huya_anchor_weekly_income_table_format = '("%s",%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d),'

    huya_anchor_info_list = []
    huya_anchor_weekly_income_list = []
    
    for anchor in anchor_inform_list:
        if anchor.anchor_id != 0:
            huya_anchor_info_list.append((anchor.anchor_id,anchor.anchor_name,anchor.subscriber_number,anchor.clan,anchor.live_first_class,anchor.live_second_clsss))
            anchor_id_with_date = str(anchor.anchor_id) + str(int(time.time()))
            huya_anchor_weekly_income_list.append((anchor_id_with_date,anchor.anchor_id) + tuple(anchor.anchor_weekly_income))

    mysql_object.insertManyDatas(tabel_name='huya_anchor_info',data_format=huya_anchor_info_table_format,datas_tuple=huya_anchor_info_list)
    mysql_object.insertManyDatas(tabel_name='huya_anchor_weekly_income',data_format=huya_anchor_weekly_income_table_format,datas_tuple=huya_anchor_weekly_income_list)
