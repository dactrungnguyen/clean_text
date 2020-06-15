import requests
from datetime import datetime

# res = requests.get('http://127.0.0.1:5000/hello')
# print(res.text)

# files = {'file': open('input_text', 'rb')}
# res = requests.post('http://127.0.0.1:5000/clean', files=files)
# print(res.json())


function_url = 'http://172.17.0.2:31112/function/clean-text'
for i in range(100):
    payload = open('input_text', 'rb')
    start = datetime.now()
    res = requests.post(function_url, data=payload)
    print(f'Request took {datetime.now() - start}')
    payload.close()
    