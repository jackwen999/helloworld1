import time
import random
import requests
import string
import hashlib
import urllib
from urllib.parse import quote
a=''
import base64
#app id= 1107231522
#app key = j63SAfpb4SQ9B8Zd
url = 'https://api.ai.qq.com/fcgi-bin/ocr/ocr_generalocr'
ur2 = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
with open('D:\\python\\helloworld\\tencent\\maobizi.jpg','rb') as f:
    imgbase64 = base64.b64encode(f.read()).decode('utf-8')

#print(basedata)

def curlmd5(src):
    m = hashlib.md5(src.encode('UTF-8'))
    # 将得到的MD5值所有字符转换成大写
    return m.hexdigest().upper()

def get_params():
    # 请求时间戳（秒级），用于防止请求重放（保证签名5分钟有效）
    t = time.time()
    time_stamp=str(int(t))
    # 请求随机字符串，用于保证签名不可预测
    nonce_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    # 应用标志，这里修改成自己的id和key
    app_id = '1107274771'
    app_key = 'tTV2E1Gvc3a4iiFK'
    img='asd'
    params = {'app_id':app_id,
              'image':imgbase64,
              'time_stamp':time_stamp,
              'nonce_str':nonce_str
              # 'session':'10000'
             }
    sorted_dict=sorted(params)
    sign_before = ''
    #sorted_dict=sorted(params.items(),key=lambda item:item[0],reverse=False)
    for key in sorted(params):
        # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写。
        sign_before += '{}={}&'.format(key, quote(params[key], safe=''))
    sign_before += 'app_key={}'.format(app_key)
    print(sorted_dict)
    print(sign_before)


    sha= hashlib.md5()
    print("排序后字典")
    sign = curlmd5(sign_before)
    params['sign'] = sign
    print(sign)
    print(sorted_dict)
    #sign = curlmd5(rawtext)
    print(sha)
    print("param's value")
    print(params)

    # print('md5签名'+curlmd5(rawtext))
    # print(curlmd5(rawtext).upper())
    # print('s123')
    # sign=curlmd5(rawtext).upper()
    sign_before = ''
    # 要对key排序再拼接
    # for key in sorted_params:
    #     # 键值拼接过程value部分需要URL编码，URL编码算法用大写字母，例如%E8。quote默认大写。
    #     sign_before += '{}={}&'.format(key,quote(params[key], safe=''))
    #     # sign_before += '{}={}&'.format(key,params[key])
    # print('签名前排序'+sign_before)
    # 将应用密钥以app_key为键名，拼接到字符串sign_before末尾
    # sign_before += 'app_key={}'.format(app_key)
    # print('添加key后的参数'+sign_before)
    # 对字符串sign_before进行MD5运算，得到接口请求签名

    # print(sign)

    return params

print(get_params())

def req():
    print(get_params())
    reqq_1=requests.post(url,data=get_params())
    print(reqq_1.text)

req()

