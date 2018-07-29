import requests
url='http://www.163.com'
req =requests.get(url)
print(req.text)