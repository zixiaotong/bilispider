from requests_html import HTMLSession
import time


def do_spider2(page):
    print('第{}页'.format(page))
    session = HTMLSession()
    if page == 1:
        url = 'https://search.bilibili.com/all?keyword=%E8%AE%BE%E8%AE%A1&o'
    else:
        url = 'https://search.bilibili.com/all?keyword=%E8%AE%BE%E8%AE%A1&page={}&o={}'.format(page, (page - 1) * 30)
    r = session.get(url)
    chapt_list = r.html.xpath("//*[@id='all-list']/div[1]/ul/li")
    if page == 1:
        chapt_list = r.html.xpath("//*[@id='all-list']/div[1]/div[2]/ul[3]/li")
    for chapt in chapt_list:
        print('title1:{} url1:{}'.format(chapt.xpath("//a/@title")[0], chapt.xpath("//a/@href")[0][2:]))


ss = time.time()
for x in range(1, 35):
    do_spider2(x)
print(time.time() - ss)
