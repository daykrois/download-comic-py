import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlencode
from py_mini_racer import MiniRacer


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'Referer': 'https://tel.dm5.com/m5338/',
}

url = 'https://tel.dm5.com/m5338/'

_cid = ''
_mid = ''
_dt = ''
_sign = ''
dm5_key = '09f55502cef672b4'


response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
scripts = soup.find_all('script')
for script in scripts:
    script_content = script.get_text()
    if 'DM5_VIEWSIGN' in script_content:
        # print(script_content)
        # 使用正则表达式匹配所有以 'var DM5_' 开头的行
        pattern = r'var\s+(DM5_[A-Za-z0-9_]+)\s*=\s*(.*?);'
        matches = re.findall(pattern, script_content)
        # 创建一个字典来存储提取的变量和值
        variables_dict = {}
        # 遍历匹配的结果，将变量和值添加到字典中
        for match in matches:
            variable, value = match
            variables_dict[variable] = value.strip("'")
        # 打印提取的变量和值
        for variable, value in variables_dict.items():
            if variable == 'DM5_VIEWSIGN':
                _sign = value.strip('"')
            if variable == 'DM5_VIEWSIGN_DT':
                _dt = value.strip('"')
            if variable == 'DM5_CID':
                _cid = value
            if variable == 'DM5_MID':
                _mid = value
    # if 'eval' in script_content:
    #     print(script_content)
        # ['0', '2', '9', '3', 'd', '3', '9', '8', '9', '8', '0', '8', '8', 'a', '4', 'c']
        # f293d39898f88a4c
        # 09f55502cef672b4
        # pattern = r'(\d|\w)\\'
        # matches = re.findall(pattern, script_content)
        # print(matches)
        
page = 1
url = 'https://tel.dm5.com/m5338/chapterfun.ashx'

# print(url+'?'+urlencode(params))
while(page < 10):
    params = {
    'cid': _cid,
    'page': page,  
    # 'key': dm5_key,  
    'language': '1',
    'gtk': '6',
    '_cid': _cid,
    '_mid': _mid,
    '_dt': _dt,  
    '_sign': _sign
    }
    response = requests.get(url,params=params,headers=headers)
    if response.status_code == 200:
        # print(response.text)
        ctx = MiniRacer()
        image_url = ctx.execute(response.text)[0]
        print(image_url)
        response = requests.get(image_url,headers=headers)
        if response.status_code == 200:
        # 如果成功，将图片内容写入文件
            with open('downloaded_image'+str(page)+'.jpg', 'wb') as file:
                file.write(response.content)
            print('图片已成功保存到本地。')
            page += 1
        else:   
            # 如果请求失败，打印错误信息
            print(f'图片下载失败，状态码：{response.status_code}')
    else:
        print(f"响应失败，状态码 {response.status_code}")