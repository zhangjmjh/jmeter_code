import requests
import base64
import json
import time
import sys


path = "D:\\python_code\\jmeter_code\\imageCodes\\"


def get_image(str_reponse):
    # time_list = list(str(time.time()))
    img_name = time.strftime("%m%d-%H%M%S", time.localtime())
    # time_list.remove(".")
    # time_list = time_list[:13]
    # time_stamp = ''.join(time_list)
    # cookies = dict(JSESSIONID=str_jsession, CHECKCODE=str_checkcode)
    # url = "http://192.168.123.16:8082/user-center/code/getCode.ajax?timeStamp=" + time_stamp
    # img_res = requests.get(url, cookies=cookies)
    filepath = path + img_name + ".jpg"
    with open(filepath, 'wb') as f:
        f.write(str_reponse)
        f.close()
    return filepath


def get_code(image_name):
    filepath = path + image_name + ".jpg"
    with open(filepath, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        f.close()
    res = requests.post("http://192.168.123.156:5050/code", data={'imgcode': s})
    json_data = json.loads(res.text, encoding='utf-8')
    code = json_data['msg']
    return code


if __name__ == '__main__':
    image_name = sys.argv[1]
    time.sleep(1)
    print(get_code(image_name))
