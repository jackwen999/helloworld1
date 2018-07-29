import requests

sdaders = {
    'App-Secret': 'xStyz9kDILRKT5Fq',
    'Hash': 'OqY1MQNbVmNDnitVbXtK6NoPzgzsmfSaFQcsGZDCm'
}

url = 'https://api.cloudcone.com/api/v1/compute/:id/info'

req = requests.get(url, headers=sdaders)
print(req.content)