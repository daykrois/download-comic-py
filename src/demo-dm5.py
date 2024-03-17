import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'Referer': 'https://tel.dm5.com/m5338/',
}

url = 'https://tel.dm5.com/m5338/chapterfun.ashx'
params = {
    'cid': '5338',
    'page': '2',  
    'key': '53dd75c1892f5413',  
    'language': '1',
    'gtk': '6',
    '_cid': '5338',
    '_mid': '455',
    '_dt': '2024-03-17 19:52:25',  
    '_sign': '03dfeeaf7d57c051dad8cb8a84e175a8'
}

# 发送GET请求
response = requests.get(url, params=params,headers=headers)
if response.status_code == 200:
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")