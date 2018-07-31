import requests
face_detect = 'https://api-us.faceplusplus.com/facepp/v3/detect'
face_analyze='https://api-us.faceplusplus.com/facepp/v3/face/analyze'

params1 ={
    'api_key':'d6z_dJ3GByC1imsakEi38VdFWuweFNqh',
    'api_secret':'5ZY01K3UDqemSEmlc0hxfHWAcxqAAGcn',
    'image_url':'https://www.voguepro.top/usr/uploads/2018/05/1714792681.jpg',

}
params2 ={
    'api_key':'d6z_dJ3GByC1imsakEi38VdFWuweFNqh',
    'api_secret':'5ZY01K3UDqemSEmlc0hxfHWAcxqAAGcn',
    'image_url':'https://www.voguepro.top/usr/uploads/2018/05/1714792681.jpg',
    'return_attributes':'gender,age,smiling,headpose,facequality'
}
req= requests.post(face_detect,params=params1)
print(req.json())
print(req.json()['faces'][0]['face_token'])
print(req.json()['faces'][1]['face_token'])
token = req.json()['faces'][0]['face_token']+','+req.json()['faces'][1]['face_token']
#params2['face_tokens']=req.json()['faces'][0]['face_token']
params2['face_tokens']=token
req2=requests.post(face_analyze,params=params2)
print(req2.json())