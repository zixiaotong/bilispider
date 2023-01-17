import requests


def upload_portrait(self):
    files = [
        ('file', ('home2.png', open('/Users/zcool/Downloads/93d1e30a565d983ac2756aa2791e7cf2.jpg', 'rb'), 'image/png'))
    ]
    heardes = {
        "Authorization": 'RmRiZ0s5WFdzUkpvdGcxQlU1N1doQT09'
    }
    payload = {}
    response = requests.request("POST", '127.0.0.1:8081/v4.0.1/upload/image', headers=heardes, data=payload,
                                files=files)
    print(response)


if __name__ == '__main__':
    upload_portrait()
