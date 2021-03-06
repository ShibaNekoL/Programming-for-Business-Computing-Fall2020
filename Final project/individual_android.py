import pygame as pg
from datetime import datetime
import matplotlib
import datetime as dt
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.font_manager
import matplotlib.backends.backend_agg as agg
from wordcloud import WordCloud
import PIL .Image as image
import jieba

dateformat = "%Y/%m/%d"
dateFormatter = "%Y/%m/%d %H:%M"
timeformat = "%H:%M"
calltimeformat = "%H:%M:%S"


class Android:
    line = ""

    def inputfile(self, path):
        with open(file=path, mode="r", encoding="utf-8") as f:
            Android.line = f.readlines()

        # 去除前2列沒用的資訊
        Android.line = Android.line[2:]

        for i in range(len(Android.line)):
            # get rid of "\n"
            Android.line[i] = Android.line[i].strip("\n")
            # 將每則訊息的元素分開變成list中的元素 一則訊息為一小list
            Android.line[i] = Android.line[i].split(sep="\t")
        # print(lines_for_word)
        # 刪除空行和日期行
        indexes = list()

        # 在每則訊息前加上日期
        for i in range(len(Android.line)):

            # 若找到空行 則在其後數行都加上日期元素
            if Android.line[i] == ['']:
                try:
                    # date 把後面沒用的星期幾刪掉
                    date = Android.line[i + 1][0][:-4]

                    # 要再檢查日期是不是符合格式 因為有智障一則訊息裡包含空行
                    datetime.strptime(date, dateformat)

                    # 把空行和日期行位置append到indexes list中，等等加完日期就可以刪掉
                    # 空行
                    indexes.append(i)
                    # 日期行
                    indexes.append(i + 1)

                    k = i + 2
                    # 因為android版退群會是空行 所以要加個判斷 避免最後一則訊息是空行然後超出list長度
                    if k + 1 <= len(Android.line):
                        # 判斷其後數行是否為空行 否則持續迴圈 加上日期元素
                        while Android.line[k] != ['']:
                            if k + 1 > len(Android.line):
                                break

                            Android.line[k].insert(0, date)  # date

                            if k + 1 == len(Android.line):
                                break

                            k += 1

                except ValueError:
                    indexes.append(i)
                    continue

        # delete space and date elements
        for index in sorted(indexes, reverse=True):
            del Android.line[index]

        # 若錯誤代表有人一次傳很多行訊息(而且裡面可能還有空行)
        # 直接刪掉就好 因為群組訊息我不需要做內容相關的功能 則數就夠了

        # 長度4: 正常
        # 此時訊息長度1(內容): 一則訊息內有數行 前一行是空行
        # 此時訊息長度2(日期,內容): 一則訊息內有數行
        # 此時訊息長度3(時間,人名,內容): 前面訊息有智障一次傳數行內有空行 所以沒讀到日期 等等解決
        # 長度3(日期,時間,內容): 有人退群/有人收回訊息 直接刪除

        # 加日期到沒日期的訊息
        for i in range(len(Android.line)):
            try:
                datetemp = Android.line[i][0]
                datetime.strptime(datetemp, dateformat)
            except:
                Android.line[i].insert(0, date)  # date
            date = Android.line[i][0]
        # print(lines_for_word)

        delete = list()
        for i in range(len(Android.line)):
            if len(Android.line[i]) == 2:  # 補回用換行的文字內容
                Android.line[i].insert(1, Android.line[i - 1][1])
                Android.line[i].insert(2, Android.line[i - 1][2])
            if len(Android.line[i]) == 3:
                Android.line[i][1] = Android.line[i - 1][1]
                Android.line[i].insert(2, Android.line[i - 1][2])

        # delete space and date elements
        for index in sorted(delete, reverse=True):
            del Android.line[index]

        # 日期和時間兩元素合併 然後轉格式
        delete_indexes = list()
        for i in range(len(Android.line)):
            datetimestr = Android.line[i][0] + " " + Android.line[i][1]
            dtformat = datetime.strptime(datetimestr, dateFormatter)
            Android.line[i].insert(0, dtformat)

        # 刪掉一次多則訊息的剩下訊息
        for index in sorted(delete_indexes, reverse=True):
            del Android.line[index]

    def inputfile2(self, path):
        with open(file=path, mode="r", encoding="utf-8") as f:
            Android.line = f.readlines()

        # 去除前2列沒用的資訊
        Android.line = Android.line[2:]

        for i in range(len(Android.line)):
            # get rid of "\n"
            Android.line[i] = Android.line[i].strip("\n")
            # 將每則訊息的元素分開變成list中的元素 一則訊息為一小list
            Android.line[i] = Android.line[i].split(sep="\t")
        # print(lines)
        # 刪除空行和日期行
        indexes = list()

        # 在每則訊息前加上日期
        for i in range(len(Android.line)):

            # 若找到空行 則在其後數行都加上日期元素
            if Android.line[i] == ['']:
                try:
                    # date 把後面沒用的星期幾刪掉
                    date = Android.line[i + 1][0][:-4]

                    # 要再檢查日期是不是符合格式 因為有智障一則訊息裡包含空行
                    datetime.strptime(date, dateformat)

                    # 把空行和日期行位置append到indexes list中，等等加完日期就可以刪掉
                    # 空行
                    indexes.append(i)
                    # 日期行
                    indexes.append(i + 1)

                    k = i + 2

                    # 因為android版退群會是空行 所以要加個判斷 避免最後一則訊息是空行然後超出list長度
                    if k + 1 <= len(Android.line):
                        # 判斷其後數行是否為空行 否則持續迴圈 加上日期元素
                        while Android.line[k] != ['']:
                            if k + 1 > len(Android.line):
                                break

                            Android.line[k].insert(0, date)  # date

                            if k + 1 == len(Android.line):
                                break

                            k += 1

                except ValueError:
                    indexes.append(i)
                    continue

        # delete space and date elements
        for index in sorted(indexes, reverse=True):
            del Android.line[index]

        # 若錯誤代表有人一次傳很多行訊息(而且裡面可能還有空行)
        # 直接刪掉就好 因為群組訊息我不需要做內容相關的功能 則數就夠了

        # 長度4: 正常
        # 此時訊息長度1(內容): 一則訊息內有數行 前一行是空行
        # 此時訊息長度2(日期,內容): 一則訊息內有數行
        # 此時訊息長度3(時間,人名,內容): 前面訊息有智障一次傳數行內有空行 所以沒讀到日期 等等解決
        # 長度3(日期,時間,內容): 有人退群/有人收回訊息 直接刪除

        # 加日期到沒日期的訊息
        for i in range(len(Android.line)):
            try:
                datetemp = Android.line[i][0]
                datetime.strptime(datetemp, dateformat)
            except:
                Android.line[i].insert(0, date)  # date
            date = Android.line[i][0]

        delete = list()
        for i in range(len(Android.line)):
            if len(Android.line[i]) == 2 or len(Android.line[i]) == 3:
                delete.append(i)

        # delete space and date elements
        for index in sorted(delete, reverse=True):
            del Android.line[index]

        # 日期和時間兩元素合併 然後轉格式
        delete_indexes = list()
        for i in range(len(Android.line)):
            datetimestr = Android.line[i][0] + " " + Android.line[i][1]
            dtformat = datetime.strptime(datetimestr, dateFormatter)
            Android.line[i].insert(0, dtformat)

        # 刪掉一次多則訊息的剩下訊息
        for index in sorted(delete_indexes, reverse=True):
            del Android.line[index]
        # print(lines)
        # print(lines[-1][1:6])  # ['2020/12/18', '20:19', '昀真', '通話時間 2:41']

    def words(self):
        def pie_words(list_message):
            # 建立兩人名字的list
            name = []
            name.append(list_message[0][3])
            for i in range(len(list_message)):
                if list_message[i][3] != name[0]:
                    name.append(list_message[i][3])
                    break

            word_1 = 0  # 第一人的字數
            word_2 = 0  # 第二人的字數
            for i in range(len(list_message)):
                if list_message[i][3] == name[0]:  # 如果名字與第一人相同
                    if list_message[i][4] == "[貼圖]" \
                            or list_message[i][4] == "[照片]" \
                            or list_message[i][4] == "[影片]" \
                            or list_message[i][4] == "[語音訊息]" \
                            or list_message[i][4] == "[檔案]" \
                            or list_message[i][4] == "未接來電" \
                            or list_message[i][4] == "相簿建立成功" \
                            or list_message[i][4] == "[聯絡資訊]" \
                            or list_message[i][4] == "[位置資訊]" \
                            or list_message[i][4][0:4] == "通話時間" \
                            or list_message[i][4] == "您已結束通話" \
                            or list_message[i][4] == "[禮物]" \
                            or list_message[i][4] == "無人接聽":
                        pass
                    else:
                        word_1 += len(list_message[i][4])  # 計算第一人字數
                if list_message[i][3] == name[1]:  # 如果名字與第二人相同
                    if list_message[i][4] == "[貼圖]" \
                            or list_message[i][4] == "[照片]" \
                            or list_message[i][4] == "[影片]" \
                            or list_message[i][4] == "[語音訊息]" \
                            or list_message[i][4] == "[檔案]" \
                            or list_message[i][4] == "未接來電" \
                            or list_message[i][4] == "相簿建立成功" \
                            or list_message[i][4] == "[聯絡資訊]" \
                            or list_message[i][4] == "[位置資訊]" \
                            or list_message[i][4][0:4] == "通話時間" \
                            or list_message[i][4] == "您已結束通話" \
                            or list_message[i][4] == "[禮物]" \
                            or list_message[i][4] == "無人接聽":
                        pass
                    else:
                        word_2 += len(list_message[i][4])  # 計算第二人字數

            return [word_1, word_2, name]

        totalwords = pie_words(Android.line)
        # print(totalwords)[7493, 11004, ['映權姑姑', '昀真']]
        # 畫雙方字數圓餅圖
        fig_pie = plt.figure(figsize=(3.5, 3.5))  # 設定圖形大小
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']  # 匯入中文字型
        labels = [totalwords[2][0], totalwords[2][1]]  # 名字list
        word = [totalwords[0], totalwords[1]]  # 字數list
        plt.pie(word, labels=labels, autopct="%3.1f%%", colors=['Pink', 'lightblue'])
        plt.title('從古至今雙方總字數圓餅圖')  # 設定圖形標題
        plt.legend(loc="best")

        canvas = agg.FigureCanvasAgg(fig_pie)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf1 = pg.image.fromstring(raw_data, size, "RGB")

        # plt.show()

        '''近30日雙方總字數折線圖'''

        def linechart_words(list_message):

            name = []
            name.append(list_message[0][3])
            for i in range(len(list_message)):
                if list_message[i][3] != name[0]:
                    name.append(list_message[i][3])
                    break
            member_1_msglist = []
            member_2_msglist = []
            for i in range(len(list_message)):
                if list_message[i][3] == name[0]:
                    member_1_msglist.append(list_message[i])
                else:
                    member_1_msglist.append(list_message[i])
            for i in range(len(list_message)):
                if list_message[i][3] == name[1]:
                    member_2_msglist.append(list_message[i])
                else:
                    member_2_msglist.append(list_message[i])

            # 第一則訊息絕對日期
            origin_1 = datetime.date(member_1_msglist[0][0])
            last_1 = datetime.date(member_1_msglist[- 1][0])
            passday_1 = (last_1 - origin_1).days + 1

            origin_2 = datetime.date(member_2_msglist[0][0])
            last_2 = datetime.date(member_2_msglist[- 1][0])
            passday_2 = (last_2 - origin_2).days + 1
            # 做每天天數的list
            interval_1 = []
            interval_2 = []
            for i in range(passday_1):
                interval_1.append(i + 1)

            for i in range(passday_2):
                interval_2.append(i + 1)

            # dict 天數:[每日字數, 日期]
            day_1 = dict()
            for i in interval_1:
                day_1[i] = [0, str(datetime.date(member_1_msglist[0][0] + dt.timedelta(days=i - 1)))]

            day_2 = dict()
            for i in interval_2:
                day_2[i] = [0, str(datetime.date(member_2_msglist[0][0] + dt.timedelta(days=i - 1)))]

            # 加總每天有多少字數
            for i in range(len(member_1_msglist)):
                if member_1_msglist[i][3] == name[0]:
                    if list_message[i][4] == "[貼圖]" \
                            or list_message[i][4] == "[照片]" \
                            or list_message[i][4] == "[影片]" \
                            or list_message[i][4] == "[語音訊息]" \
                            or list_message[i][4] == "[檔案]" \
                            or list_message[i][4] == "未接來電" \
                            or list_message[i][4] == "相簿建立成功" \
                            or list_message[i][4] == "[聯絡資訊]" \
                            or list_message[i][4] == "[位置資訊]" \
                            or list_message[i][4][0:4] == "通話時間" \
                            or list_message[i][4] == "您已結束通話" \
                            or list_message[i][4] == "[禮物]" \
                            or list_message[i][4] == "無人接聽":
                        pass
                    else:
                        d1 = (member_1_msglist[i][0] - datetime.strptime(str(origin_1), "%Y-%m-%d")).days
                        day_1[d1 + 1][0] += len(member_1_msglist[i][4])

            for i in range(len(member_2_msglist)):
                if member_1_msglist[i][3] == name[1]:
                    if list_message[i][4] == "[貼圖]" \
                            or list_message[i][4] == "[照片]" \
                            or list_message[i][4] == "[影片]" \
                            or list_message[i][4] == "[語音訊息]" \
                            or list_message[i][4] == "[檔案]" \
                            or list_message[i][4] == "未接來電" \
                            or list_message[i][4] == "相簿建立成功" \
                            or list_message[i][4] == "[聯絡資訊]" \
                            or list_message[i][4] == "[位置資訊]" \
                            or list_message[i][4][0:4] == "通話時間" \
                            or list_message[i][4] == "您已結束通話" \
                            or list_message[i][4] == "[禮物]" \
                            or list_message[i][4] == "無人接聽":
                        pass
                    else:
                        d2 = (member_2_msglist[i][0] - datetime.strptime(str(origin_2), "%Y-%m-%d")).days
                        day_2[d2 + 1][0] += len(member_1_msglist[i][4])

            # 取近30日的字數
            month_1 = list(day_1.values())[-30:]  # 第一個人的近30日的總字數
            month_2 = list(day_2.values())[-30:]  # 第二個人的近30日的總字數

            member_date_1 = []
            member_word_1 = []
            for i in range(len(month_1)):
                # 第一人的日期
                member_date_1.append(month_1[i][1])
                # 第一人總字數訊息
                member_word_1.append(month_1[i][0])

            member_date_2 = []
            member_word_2 = []
            for i in range(len(month_2)):
                # 第二人的日期
                member_date_2.append(month_2[i][1])
                # 第二人總字數訊息
                member_word_2.append(month_2[i][0])
            return [member_date_1, member_word_1, member_date_2, member_word_2, name]

        both_totalwords = linechart_words(Android.line)
        # print(both_totalwords)
        # 折線圖
        fig_line = plt.figure(figsize=(5, 5))  # 設定圖形大小
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']  # 匯入中文字型
        # plt.xticks(fontsize=8)  # x軸刻度大小
        plt.xticks([])
        plt.yticks(fontsize=8)  # y軸刻度大小
        plt.plot(both_totalwords[0], both_totalwords[1], marker='o', ms=5,
                 label=str(both_totalwords[4][0]) + "的近30日總字數", color='Pink')
        plt.plot(both_totalwords[2], both_totalwords[3], marker='s', ms=5,
                 label=str(both_totalwords[4][1]) + "的近30日總字數", color='lightblue')
        # plt.xticks(rotation=45, ha='right')
        # 顯示圖例
        plt.legend(loc='best', fontsize=10)
        plt.title('近30日雙方總字數折線圖')  # 設定圖形標題
        plt.ylabel("字數", fontsize=10)  # 設定y軸標題
        # 顯示圖形
        canvas = agg.FigureCanvasAgg(fig_line)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf2 = pg.image.fromstring(raw_data, size, "RGB")

        #plt.show()

        return surf1, surf2    # 2

    def sentences(self):
        def sentence(list_message):
            member = dict()
            for i in range(len(list_message)):
                name = list_message[i][3]

                if name in member:
                    member[name] += 1
                else:
                    member[name] = 1

            sorted_items = sorted(member.items(), key=lambda x: x[1], reverse=True)

            # 只取前8名 到時候介面可以呈現大的第一名第二名第三名 其他五名用列表小字

            return sorted_items

        sent = sentence(Android.line)
        # print(sent)
        # 畫雙方回覆則數圓餅圖
        fig_line = plt.figure(figsize=(4,3))  # 設定圖形大小
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']  # 匯入中文字型
        labels = [sent[0][0], sent[1][0]]  # 名字
        sentences = [sent[0][1], sent[1][1]]  # 訊息數
        plt.pie(sentences, labels=labels, autopct="%3.1f%%", colors=['Gold', 'YellowGreen'])
        plt.title('從古至今雙方回覆則數圓餅圖')  # 設定圖形標題
        plt.legend(loc="best")

        canvas = agg.FigureCanvasAgg(fig_line)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf1 = pg.image.fromstring(raw_data, size, "RGB")
        # plt.show()
        '''近30日雙方總訊息數折線圖'''

        def total_msg(list_message):
            name = []
            name.append(list_message[0][3])
            for i in range(len(list_message)):
                if list_message[i][3] != name[0]:
                    name.append(list_message[i][3])
                    break
            member_1_msglist = []
            member_2_msglist = []
            for i in range(len(list_message)):
                if list_message[i][3] == name[0]:
                    member_1_msglist.append(list_message[i])
                else:
                    member_1_msglist.append(list_message[i])
            for i in range(len(list_message)):
                if list_message[i][3] == name[1]:
                    member_2_msglist.append(list_message[i])
                else:
                    member_2_msglist.append(list_message[i])

            # 分別抓兩個人的第一則訊息絕對日期
            origin_1 = datetime.date(member_1_msglist[0][0])
            last_1 = datetime.date(member_1_msglist[- 1][0])
            passday_1 = (last_1 - origin_1).days + 1

            origin_2 = datetime.date(member_2_msglist[0][0])
            last_2 = datetime.date(member_2_msglist[- 1][0])
            passday_2 = (last_2 - origin_2).days + 1
            # 做每天天數的list
            interval_1 = []
            interval_2 = []
            for i in range(passday_1):
                interval_1.append(i + 1)

            for i in range(passday_2):
                interval_2.append(i + 1)

            # dict 天數:[每日訊息則數, 日期]
            day_1 = dict()
            for i in interval_1:
                day_1[i] = [0, str(datetime.date(member_1_msglist[0][0] + dt.timedelta(days=i - 1)))]

            day_2 = dict()
            for i in interval_2:
                day_2[i] = [0, str(datetime.date(member_2_msglist[0][0] + dt.timedelta(days=i - 1)))]

            # 加總每天有多少則訊息
            for i in range(len(member_1_msglist)):
                if member_1_msglist[i][3] == name[0]:
                    d1 = (member_1_msglist[i][0] - datetime.strptime(str(origin_1), "%Y-%m-%d")).days
                    day_1[d1 + 1][0] += 1

            for i in range(len(member_2_msglist)):
                if member_1_msglist[i][3] == name[1]:
                    d2 = (member_2_msglist[i][0] - datetime.strptime(str(origin_2), "%Y-%m-%d")).days
                    day_2[d2 + 1][0] += 1

            # 取近30日的句數訊息
            month_1 = list(day_1.values())[-30:]  # 第一個人的近30日的總句數訊息
            month_2 = list(day_2.values())[-30:]  # 第二個人的近30日的總句數訊息

            member_date_1 = []
            member_sent_1 = []
            for i in range(len(month_1)):
                # 第一人的日期
                member_date_1.append(month_1[i][1])
                # 第一人句數訊息
                member_sent_1.append(month_1[i][0])

            member_date_2 = []
            member_sent_2 = []
            for i in range(len(month_2)):
                # 第二人的日期
                member_date_2.append(month_2[i][1])
                # 第二人句數訊息
                member_sent_2.append(month_2[i][0])
            return [member_date_1, member_sent_1, member_date_2, member_sent_2, name]

        temp = total_msg(Android.line)
        # print(temp)
        # 折線圖
        fig_line2 = plt.figure(figsize=(4, 3))  # 設定圖形大小
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
        # plt.xticks(fontsize=7)
        plt.xticks([])
        plt.yticks(fontsize=5)
        plt.title('近30日雙方總訊息數折線圖')  # 設定圖形標題
        plt.ylabel("訊息數")  # 設定y軸標題
        plt.plot(temp[0], temp[1], marker='o', ms=5, label=str(temp[4][0]) + "的訊息數", color='Gold')
        plt.plot(temp[2], temp[3], marker='s', ms=5, label=str(temp[4][1]) + "的訊息數", color='YellowGreen')
        # plt.xticks(rotation=45, ha='right')
        # 顯示圖例
        plt.legend(loc='best', fontsize=10)
        # 顯示圖形
        canvas = agg.FigureCanvasAgg(fig_line2)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf2 = pg.image.fromstring(raw_data, size, "RGB")

        # plt.show()
        ########################################################
        '''24小時平均訊息數長條圖'''

        def avghour_msg(list_message):
            origin = datetime.date(list_message[0][0])
            last = datetime.date(list_message[- 1][0])
            passday = (last - origin).days + 1

            time = dict()
            for i in range(24):
                time[i] = 0
            # 做每個小時的絕對時間的list
            interval = list()
            for i in range(24):
                hh = str()
                if i < 10:
                    hh = "0" + str(i)
                else:
                    hh = str(i)
                interval.append(datetime.strptime(hh + ":00", timeformat))

            # 加總每小時有多少則訊息
            for i in range(len(list_message)):
                for j in interval:
                    if (list_message[i][0] - j).seconds / 60 / 60 < 1:
                        hour = (j - datetime.strptime("1900-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")).seconds / 60 / 60
                        time[hour] += 1
            msg_perhour = []
            perhour = []
            for i in range(len(time)):
                msg_perhour.append(time[i] / passday)
            for i in range(24):
                perhour.append(i)
            return [msg_perhour, perhour]

        # 畫長條圖
        avghour = avghour_msg(Android.line)

        x_labels = np.array(avghour[1])  # 每個小時
        height = np.array(avghour[0])  # 總回應則數
        fig_square = plt.figure(figsize=(4, 3))  # 設定圖形大小
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
        plt.title('24小時平均訊息數長條圖')  # 設定圖形標題
        plt.bar(x_labels, height, width=0.5, color=['YellowGreen'])
        # plt.xlabel("時間(24小時制)")  # 設定y軸標題
        plt.ylabel("訊息數")  # 設定y軸標題
        plt.yticks(fontsize=5)
        plt.xlim((-0.5, 24))

        canvas = agg.FigureCanvasAgg(fig_square)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf3 = pg.image.fromstring(raw_data, size, "RGB")
        # plt.show()

        return surf1, surf2, surf3    # 3

    def relationships(self):
        name = []
        name.append(Android.line[0][3])
        for i in range(len(Android.line)):
            if Android.line[i][3] != name[0]:
                name.append(Android.line[i][3])
                break

        def relationship(list_message):
            # 建立兩人名字的list
            name = []
            name.append(list_message[0][3])
            for i in range(len(list_message)):
                if list_message[i][3] != name[0]:
                    name.append(list_message[i][3])
                    break
            word_1 = 0  # 第一人的字數
            word_2 = 0  # 第二人的字數
            for i in range(len(list_message)):
                if list_message[i][3] == name[0]:  # 如果名字與第一人相同
                    if list_message[i][4] == "[貼圖]" \
                            or list_message[i][4] == "[照片]" \
                            or list_message[i][4] == "[影片]" \
                            or list_message[i][4] == "[語音訊息]" \
                            or list_message[i][4] == "[檔案]" \
                            or list_message[i][4] == "未接來電" \
                            or list_message[i][4] == "相簿建立成功" \
                            or list_message[i][4] == "[聯絡資訊]" \
                            or list_message[i][4] == "[位置資訊]" \
                            or list_message[i][4][0:4] == "通話時間" \
                            or list_message[i][4] == "您已結束通話" \
                            or list_message[i][4] == "[禮物]" \
                            or list_message[i][4] == "無人接聽":
                        pass
                    else:
                        word_1 += len(list_message[i][4])  # 計算第一人字數
                if list_message[i][3] == name[1]:  # 如果名字與第二人相同
                    if list_message[i][4] == "[貼圖]" \
                            or list_message[i][4] == "[照片]" \
                            or list_message[i][4] == "[影片]" \
                            or list_message[i][4] == "[語音訊息]" \
                            or list_message[i][4] == "[檔案]" \
                            or list_message[i][4] == "未接來電" \
                            or list_message[i][4] == "相簿建立成功" \
                            or list_message[i][4] == "[聯絡資訊]" \
                            or list_message[i][4] == "[位置資訊]" \
                            or list_message[i][4][0:4] == "通話時間" \
                            or list_message[i][4] == "您已結束通話" \
                            or list_message[i][4] == "[禮物]" \
                            or list_message[i][4] == "無人接聽":
                        pass
                    else:
                        word_2 += len(list_message[i][4])  # 計算第二人字數
            total_word = word_1 + word_2
            return total_word

        # 只看訊息
        only_text1 = []
        only_text2 = []
        for i in range(len(Android.line)):
            if Android.line[i][3] == name[0]:  # 如果名字與第一人相同
                if Android.line[i][4] == "[貼圖]" \
                        or Android.line[i][4] == "[照片]" \
                        or Android.line[i][4] == "[影片]" \
                        or Android.line[i][4] == "[語音訊息]" \
                        or Android.line[i][4] == "[檔案]" \
                        or Android.line[i][4] == "未接來電" \
                        or Android.line[i][4] == "相簿建立成功" \
                        or Android.line[i][4] == "[聯絡資訊]" \
                        or Android.line[i][4] == "[位置資訊]" \
                        or Android.line[i][4][0:4] == "通話時間" \
                        or Android.line[i][4] == "您已結束通話" \
                        or Android.line[i][4] == "[禮物]" \
                        or Android.line[i][4] == "無人接聽":
                    pass
                else:
                    only_text1.append(Android.line[i][4])
            if Android.line[i][3] == name[1]:  # 如果名字與第二人相同
                if Android.line[i][4] == "[貼圖]" \
                        or Android.line[i][4] == "[照片]" \
                        or Android.line[i][4] == "[影片]" \
                        or Android.line[i][4] == "[語音訊息]" \
                        or Android.line[i][4] == "[檔案]" \
                        or Android.line[i][4] == "未接來電" \
                        or Android.line[i][4] == "相簿建立成功" \
                        or Android.line[i][4] == "[聯絡資訊]" \
                        or Android.line[i][4] == "[位置資訊]" \
                        or Android.line[i][4][0:4] == "通話時間" \
                        or Android.line[i][4] == "您已結束通話" \
                        or Android.line[i][4] == "[禮物]" \
                        or Android.line[i][4] == "無人接聽":
                    pass
                else:
                    only_text1.append(Android.line[i][4])

        keyword_eat = ['吃', '早餐', '午餐', '晚餐', '宵夜', '好料', '甜點', '餐廳', '點心', '口味', 'ㄔ', '飯', '喝', '飲料']
        eat1 = 0
        eat2 = 0
        for text in only_text1:
            for i in range(len(keyword_eat)):
                if text.find(keyword_eat[i]) != -1:
                    eat1 += 1
        for text in only_text2:
            for i in range(len(keyword_eat)):
                if text.find(keyword_eat[i]) != -1:
                    eat2 += 1
        eat = eat1 + eat2
        eat_relationship = round(eat / relationship(Android.line) * 10000, 2)
        if eat_relationship > 99.99:
            eat_relationship = 99.99

        keyword_study = ['作業', 'hw', 'Hw', 'HW', '寫', '算', '教', '學', '報告']
        study1 = 0
        study2 = 0
        for text in only_text1:
            for i in range(len(keyword_study)):
                if text.find(keyword_study[i]) != -1:
                    study1 += 1
        for text in only_text2:
            for i in range(len(keyword_study)):
                if text.find(keyword_study[i]) != -1:
                    study2 += 1
        study = study1 + study2
        study_relationship = round(study / relationship(Android.line) * 10000, 2)
        if study_relationship > 99.99:
            eat_relationship = 99.99

        keyword_dirty = ['幹', '乾', '靠', '操', '媽的', '他媽', 'shit', 'fuck']
        dirty1 = 0
        dirty2 = 0
        for text in only_text1:
            for i in range(len(keyword_dirty)):
                if text.find(keyword_dirty[i]) != -1:
                    dirty1 += 1
        for text in only_text2:
            for i in range(len(keyword_dirty)):
                if text.find(keyword_dirty[i]) != -1:
                    dirty2 += 1
        dirty = dirty1 + dirty2
        dirty_relationship = round(dirty / relationship(Android.line) * 10000, 2)
        if dirty_relationship > 99.99:
            dirty_relationship = 99.99

        keyword_ha = ['哈']
        ha1 = 0
        ha2 = 0
        for text in only_text1:
            for i in range(len(keyword_ha)):
                if text.find(keyword_ha[i]) != -1:
                    ha1 += 1
        for text in only_text2:
            for i in range(len(keyword_ha)):
                if text.find(keyword_ha[i]) != -1:
                    ha2 += 1
        ha = ha1 + ha2
        ha_relationship = round(ha / relationship(Android.line) * 10000, 2)
        if ha_relationship > 99.99:
            ha_relationship = 99.99

        keyword_sex = ['變態', '色', '奶', '女', '男', '帥', '漂亮', '抓', '可愛', '妹', '寫真', '暈', '裸', '噁', '壞壞']
        sex1 = 0
        sex2 = 0
        for text in only_text1:
            for i in range(len(keyword_sex)):
                if text.find(keyword_sex[i]) != -1:
                    sex1 += 1
        for text in only_text2:
            for i in range(len(keyword_sex)):
                if text.find(keyword_sex[i]) != -1:
                    sex2 += 1
        sex = sex1 + sex2
        sex_relationship = round(sex / relationship(Android.line) * 10000, 2)
        if sex_relationship > 99.99:
            sex_relationship = 99.99

        keyword_number = [ha_relationship, sex_relationship, dirty_relationship, study_relationship, eat_relationship]
        keyword_level = []
        for i in keyword_number:
            if i == 0:
                keyword_level.append(0)
            if 0 < i < 20:
                keyword_level.append(1)
            if 20 <= i < 40:
                keyword_level.append(2)
            if 40 <= i < 60:
                keyword_level.append(3)
            if 60 <= i < 80:
                keyword_level.append(4)
            if 80 <= i:
                keyword_level.append(5)

        keyword_type = ['「哈」' + '\n' + '的使用頻率', '變態程度', '髒話使用', '學術討論', '關於「吃」']
        y = np.arange(len(keyword_type))  # 產生 Y 軸座標序列
        x = np.arange(0, 6, 1)  # 產生 X 軸座標序列
        fig_square = plt.figure(figsize=(8, 6))  # 設定圖形大小
        plt.barh(y, keyword_level, color=['orange', 'gold', 'lightgreen', 'lightblue', 'plum'])  # 繪製長條圖
        plt.yticks(y, keyword_type)  # 設定 Y 軸刻度標籤
        x_ticks = np.arange(0, 6, 1)  # X 軸刻度陣列
        plt.xticks(x, x_ticks)  # 設定 X 軸刻度標籤
        plt.title(name[0] + " & " + name[1] + '\n' + "聊天紀錄等級分析")  # 設定圖形標題
        plt.xlabel('等級')  # 設定 X 軸標籤

        canvas = agg.FigureCanvasAgg(fig_square)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf = pg.image.fromstring(raw_data, size, "RGB")
        # plt.show()

        return surf  # 等級圖

    def wordclouds(self):
        # 建立兩人名字的list
        name = []
        name.append(Android.line[0][3])
        for i in range(len(Android.line)):
            if Android.line[i][3] != name[0]:
                name.append(Android.line[i][3])
                break
        # print(name)
        """文字雲"""
        only_text1 = []
        only_text2 = []
        for i in range(len(Android.line)):
            if Android.line[i][4] == '[貼圖]':
                continue
            if Android.line[i][4] == '[照片]':
                continue
            if Android.line[i][4] == '[影片]':
                continue
            if Android.line[i][4] == '[語音訊息]':
                continue
            if Android.line[i][4] == '[檔案]':
                continue
            if Android.line[i][4] == '未接來電':
                continue
            if Android.line[i][4] == '相簿建立成功':
                continue
            if Android.line[i][4] == '[聯絡資訊]':
                continue
            if Android.line[i][4] == '[位置資訊]':
                continue
            if Android.line[i][4][0:4] == '通話時間':
                continue
            if Android.line[i][4] == '您已結束通話':
                continue
            if Android.line[i][4] == '[禮物]':
                continue
            if Android.line[i][4] == '無人接聽':
                continue
            if Android.line[i][3] == name[0]:
                only_text1.append(Android.line[i][4])
            if Android.line[i][3] == name[1]:
                only_text2.append(Android.line[i][4])
        # print(only_text1)
        # print(only_text2)

        enter_text1 = ''
        enter_text2 = ''
        for text1 in only_text1:
            enter_text1 += text1 + '\n'
        for text2 in only_text2:
            enter_text2 += text2 + '\n'

        background_color = "white"
        font = 'C:\\Users\\j3699\\.matplotlib\\TaipeiSansTCBeta-Regular.ttf'  # 要自己從使用者的電腦放字型檔
        mask = np.array(image.open("C:\\Users\\j3699\\OneDrive\\桌面\gp14\\circle.jpg"))  # 要自己從使用者的電腦下載文字雲圖形模板

        word_list1 = jieba.cut(enter_text1)  # 第一個人傳的訊息
        result1 = " ".join(word_list1)  # 斷句以空格隔開
        wordcloud1 = WordCloud(mask=mask, background_color='white', font_path=font).generate(result1)

        # 這裡會合併兩個圖(所以用到subplot)
        fig_cloud = plt.figure(figsize=(4.5, 4.5))
        # plt.subplot(1, 2, 1)
        plt.title(str(name[0]) + "常用的字")
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
        plt.imshow(wordcloud1)
        plt.axis("off")

        canvas = agg.FigureCanvasAgg(fig_cloud)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf = pg.image.fromstring(raw_data, size, "RGB")

        word_list2 = jieba.cut(enter_text2)  # 第二個人傳的訊息
        result2 = " ".join(word_list2)
        wordcloud2 = WordCloud(mask=mask, background_color='white', font_path=font).generate(result2)

        fig_cloud2 = plt.figure(figsize=(4.5, 4.5))
        # plt.subplot(1, 2, 2)
        plt.title(str(name[1]) + "常用的字")
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
        plt.axis("off")
        plt.imshow(wordcloud2)

        canvas = agg.FigureCanvasAgg(fig_cloud2)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf2 = pg.image.fromstring(raw_data, size, "RGB")
        # 顯示圖形
        # plt.show()

        return surf, surf2  # 回傳兩人的文字雲

    def calls(self):
        def call_time(list_message):
            # 先建立兩人名字的list，方便後面分層
            name = []
            name.append(list_message[0][3])
            for i in range(len(list_message)):
                if list_message[i][3] != name[0]:
                    name.append(list_message[i][3])
                    break
            # 先分開兩人的通話時間[通話時間]
            call_temp_1 = []
            call_temp_2 = []
            for i in range(len(list_message)):
                if list_message[i][3] == name[0] and list_message[i][4][0:4] == "通話時間":
                    call_temp_1.append(list_message[i][4][5:])

                if list_message[i][3] == name[1] and list_message[i][4][0:4] == "通話時間":
                    call_temp_2.append(list_message[i][4][5:])
            # 轉換成時間格式
            call_1 = []
            call_2 = []
            for i in call_temp_1:
                if len(i) == 7:  # 通話是大於一個小時但小於十個小時(7個字元)
                    call_1.append(datetime.strptime("0" + i, calltimeformat))
                if len(i) == 8:  # 通話是大於十個小時(8個字元)
                    call_1.append(datetime.strptime(i, calltimeformat))
                if len(i) == 4:  # 通話小於一個小時且小於十分鐘(4個字元)
                    call_1.append(datetime.strptime("00:0" + i, calltimeformat))
                if len(i) == 5:  # 通話小於一個小時且大於十分鐘(5個字元)
                    call_1.append(datetime.strptime("00:" + i, calltimeformat))
                else:
                    pass
            for i in call_temp_2:
                if len(i) == 7:  # 通話是大於一個小時但小於十個小時(7個字元)
                    call_2.append(datetime.strptime("0" + i, calltimeformat))
                if len(i) == 8:  # 通話是大於十個小時(8個字元)
                    call_2.append(datetime.strptime(i, calltimeformat))
                if len(i) == 4:  # 通話小於一個小時且小於十分鐘(4個字元)
                    call_2.append(datetime.strptime("00:0" + i, calltimeformat))
                if len(i) == 5:  # 通話小於一個小時且大於十分鐘(5個字元)
                    call_2.append(datetime.strptime("00:" + i, calltimeformat))
                else:
                    pass
            # 加總雙方各別通話時間
            time_1 = float()
            time_2 = float()
            for i in call_1:
                hour_1 = (i - datetime.strptime("1900-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")).seconds / 60
                time_1 += hour_1
            for i in call_2:
                hour_2 = (i - datetime.strptime("1900-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")).seconds / 60
                time_2 += hour_2

            return [[name[0], round(time_1, 2)], [name[1], round(time_2, 2)]]

        calltime = call_time(Android.line)
        # print(calltime)

        # 畫雙方通話時間圓餅圖
        if calltime[0][1] != 0 and calltime[1][1] != 0:
            call1 = str(calltime[0][0]) + "打給對方的通話時間(分鐘): " + str(calltime[0][1])
            call2 = str(calltime[1][0]) + "打給對方的通話時間(分鐘): " + str(calltime[1][1])
            fig_pie = plt.figure(figsize=(4, 3))  # 設定圖形大小
            labels = [calltime[0][0], calltime[1][0]]  # 是名字
            calltime_pie = [calltime[0][1], calltime[1][1]]  # 是通話時間
            # 顯示圖例
            plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
            plt.pie(calltime_pie, labels=labels, autopct="%3.1f%%")
            plt.title('從古至今雙方通話時間圓餅圖')  # 設定圖形標題
            plt.legend(loc="best")
            # plt.show()
            canvas = agg.FigureCanvasAgg(fig_pie)
            canvas.draw()
            renderer = canvas.get_renderer()
            raw_data = renderer.tostring_rgb()
            size = canvas.get_width_height()
            surf = pg.image.fromstring(raw_data, size, "RGB")

            '''只有一人有打過電話'''
        if calltime[0][1] == 0 and calltime[1][1] != 0:  # 只有第一人有打過電話
            call1 = str(calltime[0][0]) + "打給對方的通話時間(分鐘): " + str(calltime[0][1])
            call2 = str(calltime[1][0]) + "打給對方的通話時間(分鐘): " + str(calltime[1][1])
            fig_pie = plt.figure(figsize=(4, 3))  # 設定圖形大小
            labels = [calltime[1][0]]  # 是名字
            calltime_pie = [1]  # 是通話時間
            # 顯示圖例
            plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
            plt.pie(calltime_pie, labels=labels, autopct="%3.1f%%")
            plt.title('從古至今雙方通話時間圓餅圖')  # 設定圖形標題
            plt.legend(loc="best")
            #plt.show()
            canvas = agg.FigureCanvasAgg(fig_pie)
            canvas.draw()
            renderer = canvas.get_renderer()
            raw_data = renderer.tostring_rgb()
            size = canvas.get_width_height()
            surf = pg.image.fromstring(raw_data, size, "RGB")

        if calltime[0][1] != 0 and calltime[1][1] == 0:  # 只有第二人有打過電話
            call1 = str(calltime[0][0]) + "打給對方的通話時間(分鐘): " + str(calltime[0][1])
            call2 = str(calltime[1][0]) + "打給對方的通話時間(分鐘): " + str(calltime[1][1])
            fig_pie = plt.figure(figsize=(4, 3))  # 設定圖形大小
            labels = [calltime[0][0]]  # 是名字
            calltime_pie = [1]  # 是通話時間
            # 顯示圖例
            plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
            plt.pie(calltime_pie, labels=labels, autopct="%3.1f%%")
            plt.title('從古至今雙方通話時間圓餅圖')  # 設定圖形標題
            plt.legend(loc="best")
            # plt.show()
            canvas = agg.FigureCanvasAgg(fig_pie)
            canvas.draw()
            renderer = canvas.get_renderer()
            raw_data = renderer.tostring_rgb()
            size = canvas.get_width_height()
            surf = pg.image.fromstring(raw_data, size, "RGB")

        if calltime[0][1] == 0 and calltime[1][1] == 0:
            call1 = str(calltime[0][0]) + "打給對方的通話時間(分鐘): " + '0'
            call2 = str(calltime[1][0]) + "打給對方的通話時間(分鐘): " + '0'
            surf = "你們還沒有通話過喔"
        ###############################################################################
        '''近30日雙方通話次數折線圖'''

        def phonecall_times(list_message):
            # 抓兩人第一則的訊息
            name = []
            name.append(list_message[0][3])
            for i in range(len(list_message)):
                if list_message[i][3] != name[0]:
                    name.append(list_message[i][3])
                    break
            member_1_calltimes = []  # 把有通話的放到list中[日期, 名字, 次數]
            member_2_calltimes = []
            for i in range(len(list_message)):
                if list_message[i][3] == name[0] and list_message[i][4][0:4] == "通話時間":
                    member_1_calltimes.append([list_message[i][0], list_message[i][3], 1])
                if list_message[i][3] == name[0] and list_message[i][4][0:4] != "通話時間":
                    member_1_calltimes.append([list_message[i][0], list_message[i][3], 0])
            for i in range(len(list_message)):
                if list_message[i][3] == name[1] and list_message[i][4][0:4] == "通話時間":
                    member_2_calltimes.append([list_message[i][0], list_message[i][3], 1])
                if list_message[i][3] == name[1] and list_message[i][4][0:4] != "通話時間":
                    member_2_calltimes.append([list_message[i][0], list_message[i][3], 0])
            # 第一則訊息絕對日期
            origin_1 = datetime.date(member_1_calltimes[0][0])
            last_1 = datetime.date(member_1_calltimes[- 1][0])
            passday_1 = (last_1 - origin_1).days + 1

            origin_2 = datetime.date(member_2_calltimes[0][0])
            last_2 = datetime.date(member_2_calltimes[- 1][0])
            passday_2 = (last_2 - origin_2).days + 1
            # 做每天天數的list
            interval_1 = []
            interval_2 = []
            for i in range(passday_1):
                interval_1.append(i + 1)

            for i in range(passday_2):
                interval_2.append(i + 1)

            # dict 天數:[每日通話數, 日期]
            day_1 = dict()
            for i in interval_1:
                day_1[i] = [0, str(datetime.date(member_1_calltimes[0][0] + dt.timedelta(days=i - 1)))]

            day_2 = dict()
            for i in interval_2:
                day_2[i] = [0, str(datetime.date(member_2_calltimes[0][0] + dt.timedelta(days=i - 1)))]

            # 加總每天有多少通電話
            for i in range(len(member_1_calltimes)):
                if member_1_calltimes[i][1] == name[0]:
                    d1 = (member_1_calltimes[i][0] - datetime.strptime(str(origin_1), "%Y-%m-%d")).days
                    day_1[d1 + 1][0] += member_1_calltimes[i][2]

            for i in range(len(member_2_calltimes)):
                if member_2_calltimes[i][1] == name[1]:
                    d2 = (member_2_calltimes[i][0] - datetime.strptime(str(origin_2), "%Y-%m-%d")).days
                    day_2[d2 + 1][0] += member_2_calltimes[i][2]

            # 取近30日的句數訊息
            month_1 = list(day_1.values())[-30:]  # 第一個人的近30日的通話數
            month_2 = list(day_2.values())[-30:]  # 第二個人的近30日的通話數

            member_date_1 = []
            member_times_1 = []
            for i in range(len(month_1)):
                # 第一人的日期
                member_date_1.append(month_1[i][1])
                # 第一人的通話數
                member_times_1.append(month_1[i][0])

            member_date_2 = []
            member_times_2 = []
            for i in range(len(month_2)):
                # 第二人的日期
                member_date_2.append(month_2[i][1])
                # 第二人的通話數
                member_times_2.append(month_2[i][0])
            return [member_date_1, member_times_1, member_date_2, member_times_2, name]

        calltimes_temp = phonecall_times(Android.line)
        # print(calltimes_temp)
        # 近30日通話次數折線圖

        fig_line = plt.figure(figsize=(4, 3))  # 設定圖形大小
        plt.plot(calltimes_temp[0], calltimes_temp[1], marker='o', ms=5, linestyle="--",
                 label=str(calltimes_temp[4][0]) + "打給" + str(calltimes_temp[4][1]) + "的次數")
        plt.plot(calltimes_temp[0], calltimes_temp[3], marker='s', ms=5,
                 label=str(calltimes_temp[4][1]) + "打給" + str(calltimes_temp[4][0]) + "的次數")
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
        # 顯示圖例
        # plt.xticks(fontsize=7)  # x刻度
        plt.xticks([])
        plt.yticks(fontsize=5)
        plt.ylabel("通話次數")  # 設定y軸標題
        plt.title('近30日雙方通話次數折線圖')  # 設定圖形標題
        # plt.xticks(rotation=45, ha='right')
        plt.legend(loc='best', fontsize=10)
        # 顯示圖形
        #plt.show()
        canvas = agg.FigureCanvasAgg(fig_line)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf2 = pg.image.fromstring(raw_data, size, "RGB")
        ##################################################################################
        '''近30日雙方通話時間折線圖'''

        # dict資料長這樣 (從第一天至今第幾天:[幾則訊息, 日期].....) 848: [0, '2020-11-22'], 849: [4, '2020-11-23'], 850: [1, '2020-11-24']}

        def day_calltime(list_message):
            name = []
            name.append(list_message[0][3])
            for i in range(len(list_message)):
                if list_message[i][3] != name[0]:
                    name.append(list_message[i][3])
                    break
            # 先分開兩人的通話時間[日期, 名字, 通話時間][datetime.datetime(2020, 12, 18, 20, 19), '昀真', '2:41']
            call_temp_1 = []
            call_temp_2 = []
            for i in range(len(list_message)):
                if list_message[i][3] == name[0] and list_message[i][4][0:4] == "通話時間":
                    call_temp_1.append([list_message[i][0], list_message[i][3], list_message[i][4][5:]])
                else:
                    call_temp_1.append([list_message[i][0], list_message[i][3], "0"])
            for i in range(len(list_message)):
                if list_message[i][3] == name[1] and list_message[i][4][0:4] == "通話時間":
                    call_temp_2.append([list_message[i][0], list_message[i][3], list_message[i][4][5:]])
                else:
                    call_temp_2.append([list_message[i][0], list_message[i][3], "0"])
            # 轉換成時間格式
            call_1 = []
            call_2 = []
            for i in range(len(call_temp_1)):
                if len(call_temp_1[i][2]) == 1:
                    call_1.append([call_temp_1[i][0], call_temp_1[i][1], datetime.strptime("00:00:00", calltimeformat)])
                if len(call_temp_1[i][2]) == 7:  # 通話是大於一個小時但小於十個小時(7個字元)
                    call_1.append([call_temp_1[i][0], call_temp_1[i][1],
                                   datetime.strptime("0" + call_temp_1[i][2], calltimeformat)])
                if len(call_temp_1[i][2]) == 8:  # 通話是大於十個小時(8個字元)
                    call_1.append(
                        [call_temp_1[i][0], call_temp_1[i][1], datetime.strptime(call_temp_1[i][2], calltimeformat)])
                if len(call_temp_1[i][2]) == 4:  # 通話小於一個小時且小於十分鐘(4個字元)
                    call_1.append([call_temp_1[i][0], call_temp_1[i][1],
                                   datetime.strptime("00:0" + call_temp_1[i][2], calltimeformat)])
                if len(call_temp_1[i][2]) == 5:  # 通話小於一個小時且大於十分鐘(5個字元)
                    call_1.append([call_temp_1[i][0], call_temp_1[i][1],
                                   datetime.strptime("00:" + call_temp_1[i][2], calltimeformat)])

            for i in range(len(call_temp_2)):
                if len(call_temp_2[i][2]) == 1:
                    call_2.append([call_temp_2[i][0], call_temp_2[i][1], datetime.strptime("00:00:00", calltimeformat)])
                if len(call_temp_2[i][2]) == 7:  # 通話是大於一個小時但小於十個小時(7個字元)
                    call_2.append([call_temp_2[i][0], call_temp_2[i][1],
                                   datetime.strptime("0" + call_temp_2[i][2], calltimeformat)])
                if len(call_temp_2[i][2]) == 8:  # 通話是大於十個小時(8個字元)
                    call_2.append(
                        [call_temp_2[i][0], call_temp_2[i][1], datetime.strptime(call_temp_2[i][2], calltimeformat)])
                if len(call_temp_2[i][2]) == 4:  # 通話小於一個小時且小於十分鐘(4個字元)
                    call_2.append([call_temp_2[i][0], call_temp_2[i][1],
                                   datetime.strptime("00:0" + call_temp_2[i][2], calltimeformat)])
                if len(call_temp_2[i][2]) == 5:  # 通話小於一個小時且大於十分鐘(5個字元)
                    call_2.append([call_temp_2[i][0], call_temp_2[i][1],
                                   datetime.strptime("00:" + call_temp_2[i][2], calltimeformat)])

            # 第一則訊息絕對日期
            origin_1 = datetime.date(call_1[0][0])
            last_1 = datetime.date(call_1[- 1][0])
            passday_1 = (last_1 - origin_1).days + 1

            origin_2 = datetime.date(call_2[0][0])
            last_2 = datetime.date(call_2[- 1][0])
            passday_2 = (last_2 - origin_2).days + 1
            # 做每天天數的list
            interval_1 = []
            interval_2 = []
            for i in range(passday_1):
                interval_1.append(i + 1)

            for i in range(passday_2):
                interval_2.append(i + 1)

            # dict 天數:[每日通話時間, 日期]
            day_1 = dict()
            for i in interval_1:
                day_1[i] = [0, str(datetime.date(call_1[0][0] + dt.timedelta(days=i - 1)))]

            day_2 = dict()
            for i in interval_2:
                day_2[i] = [0, str(datetime.date(call_2[0][0] + dt.timedelta(days=i - 1)))]

            # 加總雙方各別通話時間
            hour_1 = float()
            hour_2 = float()
            for i in range(len(call_1)):
                d1 = (call_1[i][0] - datetime.strptime(str(origin_1), "%Y-%m-%d")).days
                hour_1 = (call_1[i][2] - datetime.strptime("1900-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")).seconds / 60
                day_1[d1 + 1][0] += hour_1

            for i in range(len(call_2)):
                d2 = (call_2[i][0] - datetime.strptime(str(origin_2), "%Y-%m-%d")).days
                hour_2 = (call_2[i][2] - datetime.strptime("1900-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")).seconds / 60
                day_2[d2 + 1][0] += hour_2

            # 取近30日的通話時間
            month_1 = list(day_1.values())[-30:]  # 第一個人的近30日的通話時間
            month_2 = list(day_2.values())[-30:]  # 第二個人的近30日的通話時間

            member_date_1 = []
            member_time_1 = []
            time_1 = float()
            time_2 = float()
            for i in range(len(month_1)):
                # 第一人的日期
                member_date_1.append(month_1[i][1])
                # 第一人通話時間
                time_1 = round(month_1[i][0], 4)
                member_time_1.append(time_1)

            member_date_2 = []
            member_time_2 = []
            for i in range(len(month_2)):
                # 第一人的日期
                member_date_2.append(month_2[i][1])
                # 第一人通話時間
                time_2 = round(month_2[i][0], 4)
                member_time_2.append(time_2)

            return [member_date_1, member_time_1, member_date_2, member_time_2, name]

        calltime = day_calltime(Android.line)
        # print(calltime)

        fig_line2 = plt.figure(figsize=(4, 3))  # 設定圖形大小
        plt.plot(calltime[0], calltime[1], marker='o', ms=5, linestyle="--",
                 label=str(calltime[4][0]) + "打給" + str(calltime[4][1]))
        plt.plot(calltime[0], calltime[3], marker='s', ms=5,
                 label=str(calltime[4][1]) + "打給" + str(calltime[4][0]))
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
        # 顯示圖例
        plt.yticks(fontsize=5)
        # plt.xticks(rotation=45, ha='right', fontsize=7)
        plt.xticks([])
        plt.title("近30日雙方通話時間折線圖")
        plt.ylabel("通話時間(分鐘)")  # 設定y軸標題
        # 顯示圖例
        plt.legend(loc='best', fontsize=10)
        # 顯示圖形
        # plt.show()
        canvas = agg.FigureCanvasAgg(fig_line2)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf3 = pg.image.fromstring(raw_data, size, "RGB")

        return surf, surf2, surf3, call1, call2    # 3 surf有可能為一串文字(需設條件式)

    def others(self):
        '''雙方貼圖次數圓餅圖'''
        # 建立兩人名字的list
        name = []
        name.append(Android.line[0][3])
        for i in range(len(Android.line)):
            if Android.line[i][3] != name[0]:
                name.append(Android.line[i][3])
                break
        sticker_1 = 0
        sticker_2 = 0
        for i in range(len(Android.line)):
            if Android.line[i][3] == name[0]:  # 如果名字與第一人相同
                if Android.line[i][4] != "[貼圖]":  # 跳過不是貼圖的對話
                    pass
                else:
                    sticker_1 += 1  # 計算第一人字數
            if Android.line[i][3] == name[1]:  # 如果名字與第二人相同
                if Android.line[i][4] != "[貼圖]":  # 跳過不是貼圖的對話
                    pass
                else:
                    sticker_2 += 1  # 計算第二人字數
        sticker11 = str(name[0]) + "貼圖數: " + str(sticker_1)
        sticker12 = str(name[1]) + "貼圖數: " + str(sticker_2)
        # 畫雙方貼圖數圓餅圖

        fig_pie = plt.figure(figsize=(3.5, 3.5))  # 設定圖形大小
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']

        labels = [name[0], name[1]]  # 名字
        sticker = [sticker_1, sticker_2]  # 貼圖數
        plt.pie(sticker, labels=labels, autopct="%3.1f%%")
        plt.title('從古至今雙方貼圖次數圓餅圖')  # 設定圖形標題
        plt.legend(loc="best")
        # plt.show()
        canvas = agg.FigureCanvasAgg(fig_pie)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf = pg.image.fromstring(raw_data, size, "RGB")

        '''等待對方回覆的平均時間'''

        def replytime(list_message):
            # dict item存list: [他人回話間隔時間(分鐘),別人有回過他的他的訊息次數,平均間隔時間(分鐘)]
            member = dict()
            for i in range(len(list_message)):
                # 除去最後一則訊息i+1超出index的情況
                if i + 1 < len(list_message):
                    # 若下一個訊息是別人回話(但如果很久沒有聊天突然聊天的話的話就會讓回覆時間)
                    if list_message[i + 1][3] != list_message[i][3]:
                        name = list_message[i][3]

                        if name in member:
                            time = (list_message[i + 1][0] - list_message[i][0]).seconds / 60
                            member[name][1] += 1
                            member[name][0] += time
                        else:
                            time = (list_message[i + 1][0] - list_message[i][0]).seconds / 60
                            member[name] = [time, 1, 0]

            for i in member:
                member[i][2] = (member[i][0] / member[i][1])

            sorted_items = sorted(member.items(), key=lambda x: x[1][2], reverse=True)

            return sorted_items

        # 長條圖
        reply_time = replytime(Android.line)
        reply_timelist_1 = [name[0]]
        reply_timelist_2 = [name[1]]
        # print(reply_time[0][1][2])
        for i in range(len(reply_time)):
            if reply_time[i][0] == name[0]:  # 第一人的名字
                reply_timelist_1.append(reply_time[i][1][2])
            if reply_time[i][0] == name[1]:  # 第二人的名字
                reply_timelist_2.append(reply_time[i][1][2])
        sticker21 = str(name[0]) + "等待回覆的平均時間: " + str(round(reply_timelist_1[1], 2))
        sticker22 = str(name[1]) + "等待回覆的平均時間: " + str(round(reply_timelist_2[1], 2))
        # print(reply_timelist_1, reply_timelist_2)
        # 匯入x y 字型資料
        x_labels = np.array([reply_timelist_1[0], reply_timelist_2[0]])  # 名字
        height = np.array([reply_timelist_1[1], reply_timelist_2[1]])  # 回覆時間
        plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
        # 顯示圖例
        fig_square = plt.figure(figsize=(5, 5))  # 設定圖形大小
        plt.bar(x_labels, height, width=0.3)
        plt.title('等待對方回覆的平均時間')  # 設定圖形標題

        plt.ylabel("平均回覆時間(分鐘)")  # 設定x軸標題
        # plt.show()
        canvas = agg.FigureCanvasAgg(fig_square)
        canvas.draw()
        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf2 = pg.image.fromstring(raw_data, size, "RGB")

        return surf, surf2, sticker11, sticker12, sticker21, sticker22    # 6
