import re
import requests
import time

def getAllScriptCode(test_string = None):
    '''
    把分类界面中的 script javascript 文件的链接都找出来
    实际上，还有几个链接是其他类型的，因为找到了想要的文件（https://a.msstatic.com/huya/main3/app/all-live_58d4b.js），那剩余链接的匹配就不做了
    :param test_string: 当测试 re 匹配的时候使用
    '''
    script_url_list = None
    with open(r'./虎牙直播分类界面信息示例.txt','r',encoding='utf-8') as page_file:
        pattern = re.compile(r'<script src="(https://[\w\-\./]*?\.js)')
        page_content = page_file.read()
        script_url_list = re.findall(pattern,page_content)
        pattern = re.compile(r'<script charset="utf-8" src="(https://[\w\-\./]*?\.js)')
        script_url_list += re.findall(pattern,page_content)

        # print(script_url_list)
    return script_url_list

url_list = getAllScriptCode()
print(len(url_list))

def downScript(script_url_list):
    '''
    把分类界面中的 script javascript 代码都下载下来，原本是为了找到“下一页”这个按钮的 callback 代码，然后看是否能找到下一页的链接
    没有链接，是通过 javascript 在同一个页面上进行修改页面数据和进行推送
    为了不给被爬服务器造成不良影响，每5个文件暂停0.5s
    :param script_url_list: 链接元组/数组
    '''
    i = 1
    for url in script_url_list:
        response_page_object = requests.get(url)
        with open('./CrawlerModule/HuyaScript/{0}.js'.format(i),'w',encoding='utf-8') as f:
            f.write(response_page_object.text)
        if i%5 == 0:
            time.sleep(0.5)
        i += 1

def downOneurl(script_url,write_file):
    '''
    下载单个链接
    :param script_url：链接地址
    :param write_file: 写入的文件
    '''
    response_page_object = requests.get(script_url)
    with open(write_file,'w',encoding='utf-8') as f:
        f.write(response_page_object.text)

def writeDownTheUrlsName(list_write_down,write_file):
    '''
    写入元组/数组到文件中
    :param list_write_down: 元组/数组
    :param write_file: 写入的文件
    '''
    with open(write_file,'a',encoding='utf-8') as f:
        for row in list_write_down:
            f.write(row)
            f.write('\n')


## 现在因为暂时没有办法（不想去学）获取分类界面下一页的内容，就先每个界面手动获取
## 基于此来单个页面的获取直播间地址信息
def getUrlFromEachHallPage(hall_page_file,write_file):
    '''
    从每个大厅页面中获取每个直播间的链接
    :param hall_page_file: 大厅的代码，暂时只能自己从浏览器中复制出来
    :param write_file: 或许到的链接写入到的文件
    '''
    with open(hall_page_file,'r',encoding='utf-8') as page_file:
        pattern = re.compile(r'<a href="https://www\.huya\.com/(\w*?)" class="video-info' )
        
        ## testing
        # test_string = r'''<a href="https://www.huya.com/guying" class="video-info " target="_blank">
        # <img class="pic" data-original="//live-cover.msstatic.com/huyalive/1757672727-1757672727-7549146879536136192-3515468910-10057-A-0-1/20210301182619.jpg?x-oss-process=image/resize,limit_0,m_fill,w_338,h_190/sharpen,80/format,jpg/interlace,1/quality,q_90" src="//live-cover.msstatic.com/huyalive/1757672727-1757672727-7549146879536136192-3515468910-10057-A-0-1/20210301182619.jpg?x-oss-process=image/resize,limit_0,m_fill,w_338,h_190/sharpen,80/format,jpg/interlace,1/quality,q_90" data-default-img="338x190" alt="孤影的直播" title="孤影的直播">'''
        # url_list = re.findall(pattern,test_string)
        # print(url_list)
        
        url_list = re.findall(pattern,page_file.read())
        writeDownTheUrlsName(url_list,write_file)

# getUrlFromEachHallPage(r'./虎牙直播分类界面信息示例.txt',r'./CrawlerModule/huya_anchor_live_links.txt')

class AnchorInform():
    def __init__(self):
        self.anchor_id = None      
        self.anchor_name = None
        self.subscriber_number = None
        self.clan = None
        # 一级分类
        self.live_first_class = None 
        self.live_second_clsss = None
        self.anchor_weekly_income = None

    def showAllInform(self):
        print(self.anchor_id,self.anchor_name,self.subscriber_number,self.clan,self.live_first_class,self.live_second_clsss,self.anchor_weekly_income)

def fromUrlsGetLiveHousePage(url_index_save_file):
    url_index_list = None
    with open(url_index_save_file,'r',encoding='utf-8') as url_index_file:
        url_index_list = url_index_file.readlines()
    url_index_list = list(set(url_index_list))      ##去重
    url_list = [f"https://www.huya.com/{url_index}" for url_index in url_index_list]

    for url in url_list:
        response_page_object = requests.get(url)
        extractAndSaveLiveHouseInform(response_page_object.text)


def extractAndSaveLiveHouseInform(page_file):
    anchor = AnchorInform()

    ## ID
    pattern = re.compile(r'class="host-rid">\S+?(\d+)</')
    search_result = re.search(pattern,page_file)
    if search_result != None:
        anchor.anchor_id = int(search_result.group(1))
    
    ## name
    pattern = re.compile(r'class="host-name" title="(.*?)">')
    search_result = re.search(pattern,page_file)
    if search_result != None:
        anchor.anchor_name = search_result.group(1)
    
    ## subscriber_numbers
    pattern = re.compile(r'class="subscribe-count".*?>(\d+)</')
    search_result = re.search(pattern,page_file)
    if search_result != None:
        anchor.subscriber_number = int(search_result.group(1))
    
    ## weekly_donation
    pattern = re.compile(r'class="amout--[\w]+">([\d,]+)<')
    search_result = re.findall(pattern,page_file)
    if search_result != None:
        anchor.anchor_weekly_income = [int(i.replace(',','')) for i in search_result]
    
    ## anchor_clan
    pattern = re.compile(r'class="union-name">(.*?)</')
    search_result = re.search(pattern,page_file)
    if search_result != None:
        anchor.clan = search_result.group(1)
    
    ## anchor_class
    pattern = re.compile(r'class="host-spl clickstat".*?>(.*?)<')
    search_result = re.findall(pattern,page_file)
    if search_result != None:
        anchor.live_first_class = search_result[0]
        anchor.live_second_clsss = search_result[1]
    
    

## test
with open(r'./虎牙直播直播间内代码示例.txt','r',encoding='utf-8') as page_file:
    extractAndSaveLiveHouseInform(page_file.read())