#### 基本环境配置

**版本：**Python3.6

**系统：**Windows

**相关模块：**tkinter、PIL、requests

- tkinter是内置模块不需要安装
- PIL：pip install pillow
- equests:pip install requests

#### 实现效果图

![img](https://mmbiz.qpic.cn/mmbiz_jpg/Kad3LZzM7n5d4V0zzbgUo5zUnCUOc4JViaSPH2IHPDNheTd8KiatHdHkyrWjLe1qhkRU4qGoUb53E3Fj5wNYic6hw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

#### GUI用户使用界面

```
from tkinter import *
from tkinter import messagebox
#创建窗口
root = Tk()
#标题
root.title('Python学习群：452739833')
#窗口大小     宽 高
root.geometry('600x300')
#窗口初始位置
root.geometry('-500+200')
#标签控件
label = Label(root,text = '签名',font = ('华文行楷',20),fg = 'blue')
label.grid(row =0,column=0)

#设计输入框
entry = Entry(root,font=('微软雅黑',20))
entry.grid(row =0,column=1)
#点击按钮
button = Button(root,text = '设计签名',font=('微软雅黑',22)
                ,command =download)
button.grid(row =1,column=0)
#消息循环  显示窗口
root.mainloop()
```

#### 爬取设计签名网站数据

```
import requests
import re

#模拟浏览器发送请求
def download():

    startUrl ='http://www.uustv.com/'
    #获取用户输入的姓名
    name = entry.get()
    #去空格
    name = name.strip()
    if name =='':
        messagebox.showinfo('提示：','请输入用户名')
    else:
        date = {
            'word':name,
            'sizes':'60',
            'fonts':'jfcs.ttf',
            'fontcolor':'#000000'
        }
        result = requests.post(startUrl,data=date)
        result.encoding = 'utf-8'
        #获取网站的源代码
        html =result.text
        reg = '<div class="tu">.<img src="(.*?)"/></div>'
        #正则表达  （.*?）全部都需要匹配
        imagePath = re.findall(reg,html)
        #获取图片的完整路径
        imgUrl = startUrl + imagePath[0]
        print(imgUrl)
         #获取图片内容
        response = requests.get(imgUrl).content
        f = open('{}.gif'.format(name),'wb')
        f.write(response)

        #图片显示到窗口上
        bm = ImageTk.PhotoImage(file ='{}.gif'.format(name))

        label2= Label(root,image = bm)
        label2.bm = bm
        label2.grid(row = 2,columnspan= 2)
```

以上就是这篇文章的全部内容了，希望本文的内容对大家的学习或者工作具有一定的参考学习价值，谢谢大家对小编的支持。

想要学习Python？Python学习交流群：452739833满足你的需求，资料都已经上传群文件流，可以自行下载！