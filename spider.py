#给远程窗口起别名：git remote add origin 远程仓库地址
#向远程推送代码：  git push -u origin 分支
#8.18使用六期的数据获取热度第二的号码去预测下一期
#程序有错
import re
from urllib import request
#注重断点调试 F5启动调试，F10单步执行，F5跳到断点，F11跳到函数内部
class Spider():
    url = "file:///F:/tmp_ky/h3.html"
    root_pattern = '<td class="wdh results codes-style([\s\S]*?)</td>'
    serial_pattern = '<div class="ball02">([\s\S]*?)</div>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls
    
    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        q = []
        anchor = []
        anchors = []
        for html in root_html:
            serail = re.findall(Spider.serial_pattern, html)
            tmp = int(serail[0])
            anchor.append(tmp)
        #print(anchor)
        for i in range(int(len(anchor)/5)):
            for j in range(5):
                q.append(anchor[i*5+j])
            anchors.append(q)
            q=[]
        #print(anchors)
        return(anchors)
    
    def __operatelist(self, anchors1):
        used_times = 6
        zero=0
        one=0
        two=0
        three=0
        four=0
        five=0
        six=0
        seven=0
        eight=0
        nine=0
        for i in range(used_times):
            for j in range(5):
                if anchors1[i][j]==0:
                        zero+=1
                elif anchors1[i][j]==1:
                        one+=1
                elif anchors1[i][j]==2:
                        two+=1
                elif anchors1[i][j]==3:
                        three+=1
                elif anchors1[i][j]==4:
                        four+=1
                elif anchors1[i][j]==5:
                        five+=1
                elif anchors1[i][j]==6:
                        six+=1
                elif anchors1[i][j]==7:
                        seven+=1
                elif anchors1[i][j]==8:
                        eight+=1
                else:
                        nine+=1
        total0 = [zero,one,two,three,four,five,six,seven,eight,nine]
        #print(anchors1)
        print("6期号码出现统计",total0)
        total1 =[]
        for i in range(10):
            total1.append(total0[i])
        total1.sort(reverse=True)
        hot_level = 1#表示热度排第二
        predict_num = total0.index(total1[hot_level])
        print("6期号码出现统计降序排列",total1)
        print("预测号码",predict_num)
        print(anchors1[used_times])
        tmp = anchors1[used_times].count(predict_num)
        print(tmp)

        

    #入口方法，也是总控方法，所有的其他方法都统一汇总到go中调用
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        self.__operatelist(anchors)

spider = Spider()
spider.go()