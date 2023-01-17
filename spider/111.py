import requests

headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
    'Authorization': 'RmRiZ0s5WFdzUkpvdGcxQlU1N1doQT09',
}

data = {
  'upload_type': 'moments',
  'file': '@/Users/zcool/Downloads/93d1e30a565d983ac2756aa2791e7cf2.jpg'
}

response = requests.post('127.0.0.1:8081/v4.0.1/upload/image', headers=headers, data=data)

print(response)