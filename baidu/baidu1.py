from aip import AipOcr
APP_ID = '11602234'
API_KEY = 't2XwS9lXmIAWrf4QzSGssFTx'
SECRET_KEY = 'LBcY0HiEufTei33dhmUG87oxFDDmjrOT'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('D:\\python\\helloworld\\tencent\\maobizi.jpg')

options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
a=client.basicAccurate(image)
print(a)
