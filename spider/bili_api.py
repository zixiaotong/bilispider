import requests
import time
import json


def do_spider(page):
    print('第{}页'.format(page))
    url = 'https://api.bilibili.com/x/web-interface/search/type?__refresh__=true&_extra=&context=&page={}&page_size=42&order=click&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=%E8%AE%BE%E8%AE%A1&category_id=&search_type=video&dynamic_offset={}&preload=true&com2co=true'.format(
        page, (page - 1) * 24)
    r = requests.get(url)
    y = json.loads(r.text)
    for name in y["data"]["result"]:
        print('title:{}:url:{}'.format(name["title"], name["arcurl"]))


ss = time.time()
for x in range(1, 34):
    do_spider(x)
print(time.time() - ss)
