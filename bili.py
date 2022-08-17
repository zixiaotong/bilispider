import requests
from requests_html import HTMLSession

session = HTMLSession()
url = "https://search.bilibili.com/all?keyword=%E8%AE%BE%E8%AE%A1"
r = session.get(url)
print(r.encoding)
print(r.html.html)
