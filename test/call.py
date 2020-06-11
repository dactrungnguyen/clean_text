import requests

# res = requests.get('http://127.0.0.1:5000/hello')
# print(res.text)

# files = {'file': open('input_text', 'rb')}
# res = requests.post('http://127.0.0.1:5000/clean', files=files)
# print(res.json())


function_url = 'http://172.17.0.2:31112/function/clean-text--v0-10'
for i in range(100):
    payload = open('input_text', 'rb')
    res = requests.post(function_url, data=payload)
    payload.close()
    print(len(res.text))