# -*- coding:UTF-8 -*-
import requests
import sys
from bs4 import BeautifulSoup
'''
想要学习Python？Python学习交流群：452739833满足你的需求，资料都已经上传群文件流，可以自行下载！
'''
class downloader(object):

    def __init__(self):
        self.server = ''
        self.target = 'https://www.23us.so/files/article/html/24/24420/index.html'
        self.names = []            #存放章节名
        self.urls = []            #存放章节链接
        self.nums = 0            #章节数
    
    


    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')
            
            


    def geturl(self):

        url=requests.get(url=self.target)
        html = url.text.encode(url.encoding).decode('utf-8')
        
        bs = BeautifulSoup(html)
        #得到章节区域
        table = bs.find_all('table',id='at')
        #过滤标签,得到a标签，章节列表
        a = table[0].find_all('a')
        #章节数量
        self.nums = len(a)
        for each in a:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))
            

    def getcontent(self,target):
        url = requests.get(url=target)
        html = url.text.encode(url.encoding).decode('utf-8')
        bs = BeautifulSoup(html)
        content = bs.find_all('dd',id='contents')
        #text属性过滤br标签
        content = content[0].text
        
        return content
            
            
if __name__ == "__main__":
    
    dl = downloader()
    dl.geturl()
    
    
    for i in range(dl.nums):
        dl.writer(dl.names[i], '斗破苍穹.txt', dl.getcontent(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" %  float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《斗破苍穹》下载完成')
