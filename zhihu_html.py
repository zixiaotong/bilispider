from requests_html import HTMLSession

session = HTMLSession()
url = "https://www.zhihu.com"
cookie = " z_c0=2|1:0|10:1660788742|4:z_c0|92:Mi4xU284M0FBQUFBQUFBNEJCeTVobGtGU1lBQUFCZ0FsVk5CZTdxWXdCdlV3cjJZNlFmTUM5NjRNTnBNV1ZNcGVHS1NR|fd3be650e392c38d8caef4611eace30c8e1844a06a533fbd81a0e970f344ed25;"

cookie_dict = {i.split("=")[0]: i.split("=")[-1] for i in cookie.split("; ")}

r = session.request(
    method='get',
    url=url,
    cookies=cookie_dict
)
chapt_list = r.html.xpath("//*[@id='TopstoryContent']/div/div/div/div")
for chapt in chapt_list:
    print('content:{}'.format(chapt.xpath("//div/div/div/h2/div/meta/@content")))
