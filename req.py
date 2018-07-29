import requests
import bs4  as bd
from bs4 import BeautifulSoup
import pandas as pd
import re
import telebot
from telebot import apihelper
import logging
import json
from telebot.types import InputMediaPhoto, InputMediaVideo
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
bot=telebot.AsyncTeleBot("487800407:AAERnRGN-XA7N3jHavAaBfFweCvZGptXdbY")
xiao_cao= 'http://www.t66y.com/'
apihelper.proxy={'http':'http:127.0.0.1:1080'}


# bs = BeautifulSoup(req.content,'lxml')
# all_img = bs.find_all(type='image')
# print(all_img)
# i=0
# for link in all_img:
#     print(link.get('data-src'))
#     i+=1
# print(i)
#     #print(pic)
# print(bs.prettify())
# print((bs.title))
#
# print(sys.stdout.encoding)

req1 = requests.get('http://www.t66y.com/thread0806.php?fid=16')#获取草榴社区第一页帖子列表
bs = BeautifulSoup(req1.content,'lxml')
comp = re.compile(r'htm_data/16/')#正则表达式取帖子列表
comp2 = re.compile(r'.::')#去重
liiist = bs.find_all()
liiist1 = bs.find_all('a',id='',target='_blank')
#print(liiist1)
i=0
post_list=[]
post_name=[]
for each in liiist1:

    if (comp.match(each.get('href'))) != None:

        print(each.string)

        try:
            print(comp2.match(each.string))
            if '::' in each.string:
                pass
            else:
                if (each['href']=='htm_data/16/1707/2519480.html' or
                        each['href']=='htm_data/16/1110/622028.html' or
                        each['href']=='htm_data/16/1109/594741.html' or
                        each['href']=='htm_data/16/1802/344501.html' or
                        each['href']=='htm_data/16/1106/524942.html' or
                        each['href']=='htm_data/16/0805/136474.html' or
                        each['href']=='htm_data/16/1706/2424348.html'):
                     pass
                else:
                     post_list.append(xiao_cao + each['href'])
                     caoliu = xiao_cao + each['href']  # 拼接地址
                     post_name.append(each.string)

        except:
            pass
   # print(post_list)
    post_list_df=pd.DataFrame({'0':post_list})
    post_name_df=pd.DataFrame({'1':post_name})
    da_pd = pd.concat([post_list_df,post_name_df],axis=1)

    da_pd.to_csv('da_pd.csv', encoding='gb18030')

print(post_list)
#print(da_pd.iloc[:,0].size)#获取帖子列表总数
#print(da_pd.loc[7]['1'])

def get_caoliu_photo(i):
    req = requests.get(post_list[i])
    bs = BeautifulSoup(req.content,'lxml')
    all_img = bs.find_all(type='image')
    photo_add=[]#数组存放帖子图片地址
    i=i
    for link in all_img:
        photo_add.append(link.get('data-src'))
    return photo_add






# print(len(get_caoliu_photo(i)) )
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    a=get_caoliu_photo(15)

    print(get_caoliu_photo(11))
    print(a.__len__())
    print(a[0:9])
    try:
        inputMediaPhoto = [InputMediaPhoto(item) for item in a]
        for i in range(0, len(inputMediaPhoto), 10):
            bot.send_media_group(message.chat.id, inputMediaPhoto[i:i + 10])
        # bot.send_media_group(message.chat.id,
        #                      [InputMediaPhoto(a[0:9])])
        # bot.send_media_group(message.chat.id,
        #                      [InputMediaPhoto(a[10]), InputMediaPhoto(a[11]),
        #                       InputMediaPhoto(a[12]), InputMediaPhoto(a[13]),
        #                       InputMediaPhoto(a[14]), InputMediaPhoto(a[15]),
        #                       InputMediaPhoto(a[16]), InputMediaPhoto(a[17]),
        #                       InputMediaPhoto(a[18]), InputMediaPhoto(a[19])])
        # bot.send_media_group(message.chat.id,
        #                      [InputMediaPhoto(a[20]), InputMediaPhoto(a[21]),
        #                       InputMediaPhoto(a[22]), InputMediaPhoto(a[23]),
        #                       InputMediaPhoto(a[24]), InputMediaPhoto(a[25]),
        #                       InputMediaPhoto(a[26]), InputMediaPhoto(a[27]),
        #                       InputMediaPhoto(a[28]), InputMediaPhoto(a[29])])
        # bot.send_media_group(message.chat.id,
        #                      [InputMediaPhoto(a[30]), InputMediaPhoto(a[31]),
        #                       InputMediaPhoto(a[32]), InputMediaPhoto(a[33]),
        #                       InputMediaPhoto(a[34]), InputMediaPhoto(a[35]),
        #                       InputMediaPhoto(a[36]), InputMediaPhoto(a[37]),
        #                       InputMediaPhoto(a[38]), InputMediaPhoto(a[39])])
        # bot.send_media_group(message.chat.id,
        #                      [InputMediaPhoto(a[40]), InputMediaPhoto(a[41]),
        #                       InputMediaPhoto(a[42]), InputMediaPhoto(a[43]),
        #                       InputMediaPhoto(a[44]), InputMediaPhoto(a[45]),
        #                       InputMediaPhoto(a[46]), InputMediaPhoto(a[47]),
        #                       InputMediaPhoto(a[48]), InputMediaPhoto(a[49])])
        # bot.send_media_group(message.chat.id,
        #                      [InputMediaPhoto(a[50]), InputMediaPhoto(a[51]),
        #                       InputMediaPhoto(a[52]), InputMediaPhoto(a[53]),
        #                       InputMediaPhoto(a[54]), InputMediaPhoto(a[55]),
        #                       InputMediaPhoto(a[56]), InputMediaPhoto(a[57]),
        #                       InputMediaPhoto(a[58]), InputMediaPhoto(a[59])])
        # bot.send_media_group(message.chat.id,
        #                      [InputMediaPhoto(a[60]), InputMediaPhoto(a[61]),
        #                       InputMediaPhoto(a[62]), InputMediaPhoto(a[63]),
        #                       InputMediaPhoto(a[64]), InputMediaPhoto(a[65]),
        #                       InputMediaPhoto(a[66]), InputMediaPhoto(a[67]),
        #                       InputMediaPhoto(a[68]), InputMediaPhoto(a[69])])
    except Exception as e:
        print(e)
        pass




bot.polling()









#ulist=comp.findall(liiist1.get('href'))

#print(liiist1)
# print(liiist)
# print(liiist1)
#comp = re.compile(r'<a href="htm_data.{0,30}html" target="_blank" id=""><font color=g')

# b= []
# for link in liiist:
#     print(link['href'])
#
#     if link.string=='':
#         pass
#     else:
#         b.append(link.string)
#
# print(b)
# print(len(b))
# for link in liiist:
#
#     i+=1
#     print(liiist[i-1].get_text())
# df =  pd.DataFrame(a)
# df.to_csv('caoliu.csv',encoding='gb18030')
#print(liiist)
# print(len(liiist))
