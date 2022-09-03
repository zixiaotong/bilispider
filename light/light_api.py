import requests
import time
import json


def do_light():
    url = 'http://zishang.top/api/node/get_data'
    r = requests.get(url)
    y = json.loads(r.text)
    if len(y) > 0:
        light_switch = y[0]["light_switch"]
        print(light_switch)
        # 1 开灯 0关灯
        if light_switch == 1:
            print('执行开灯操作')
        if light_switch == 0:
            print('执行关灯操作')

        # 执行完。制成null
        requests.get('http://zishang.top/api/node/set_data_null')
    else:
        1
        print('没数据')


while True:
    time.sleep(2)
    do_light()
