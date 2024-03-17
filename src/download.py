import requests
from bs4 import BeautifulSoup
import re

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
#     'Referer': 'https://tel.dm5.com/m5338/',
# }

url = 'https://tel.dm5.com/m5338/'

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
            print(f"{variable}: {value}")
        break

