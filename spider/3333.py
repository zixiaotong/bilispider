# 输出参数：请求响应报文
import requests

# request_url = 'https://api-test49.zcool.cn/v4.0.1/upload/image'
request_url = '172.16.6.223:8081/v4.0.1/upload/image'
head = {
    "Authorization": 'RmRiZ0s5WFdzUkpvdGcxQlU1N1doQT09'
}

fl = open('/Users/zcool/Downloads/93d1e30a565d983ac2756aa2791e7cf2.jpg', 'rb')
files = {'file': (
    'test.png', fl)}  # 字段名files 以及类型和application/octet-stream 和抓取到的接口一致

# r2 = requests.post(request_url, headers=head, file=files)

print(requests.Request('POST', request_url, headers=head, file=files))  # 可以打印出来真实请求的 字段名 以及类型等信息，如果和抓取接口不一致，调整
print(r2.text)
