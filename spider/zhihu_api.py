import json

import requests

url = "https://www.zhihu.com/api/v3/feed/topstory/recommend?session_token=9702d0261e21c87aa5677786cfb21459&desktop=true&page_number=6&limit=6&action=down&after_id=29&ad_interval=-10"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
}

cookie = " z_c0=2|1:0|10:1660788742|4:z_c0|92:Mi4xU284M0FBQUFBQUFBNEJCeTVobGtGU1lBQUFCZ0FsVk5CZTdxWXdCdlV3cjJZNlFmTUM5NjRNTnBNV1ZNcGVHS1NR|fd3be650e392c38d8caef4611eace30c8e1844a06a533fbd81a0e970f344ed25;"

cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in cookie.split("; ")}
response = requests.get(url, headers=headers, cookies=cookie_dict)
y = json.loads(response.text)
for name in y["data"]:
    print('title:{}:excerpt:{}'.format(name["target"]["question"]["title"], name["target"]["excerpt"]))
