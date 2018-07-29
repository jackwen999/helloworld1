import requests
import telebot
import hashlib
import logging
import time
import random
import string
from urllib.parse import quote
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
bot=telebot.AsyncTeleBot("671788309:AAGCR4t_PY1xFdWTa-M2_IQP1_z9Wd3MYto")


def curlmd5(src):
    m = hashlib.md5(src.encode('UTF-8'))
    # 将得到的MD5值所有字符转换成大写
    return m.hexdigest().upper()


def get_params(plus_item):
    # 请求时间戳（秒级），用于防止请求重放（保证签名5分钟有效）
    t = time.time()
    time_stamp = str(int(t))
    # 请求随机字符串，用于保证签名不可预测
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    # 应用标志，这里修改成自己的id和key
    app_id = '1107274771'
    app_key = 'tTV2E1Gvc3a4iiFK'
    params = {'app_id': app_id,
              'question': plus_item,
              'time_stamp': time_stamp,
              'nonce_str': nonce_str,
              'session': '10000'
              }
    sign_before = ''
    #print(sorted(params))
    # 要对key排序再拼接
    for key in sorted(params):
        # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写。
        sign_before += '{}={}&'.format(key, quote(params[key], safe=''))
        # print(params[key])
        # print(sign_before)
        # 将应用密钥以app_key为键名，拼接到字符串sign_before末尾
    sign_before += 'app_key={}'.format(app_key)
    # 对字符串sign_before进行MD5运算，得到接口请求签名
    sign = curlmd5(sign_before)
    params['sign'] = sign
    return params


import requests



def get_content(plus_item):
    # 聊天的API地址
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
    # 获取请求参数
    plus_item = plus_item.encode('utf-8')
    payload = get_params(plus_item)
    # r = requests.get(url,params=payload)
    r = requests.post(url, data=payload)

    return r.json()["data"]["answer"]

@bot.message_handler(content_types=['text'])
def Ai_reply(message):
    reply=get_content(message.text)
    bot.send_message(message.chat.id,reply)


bot.polling(none_stop=True, interval=0, timeout=20)