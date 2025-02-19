import requests
import time
from bs4 import BeautifulSoup

# 获取网页内容
url = "https://movie.douban.com/top250"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
time.sleep(3)

# 解析数据
soup = BeautifulSoup(response.text, 'html.parser')
movies = soup.find_all('div', class_='item')[:10]  # 只取前10条

# 打印结果
for movie in movies:
    title = movie.find('span', class_='title').text
    rating = movie.find('span', class_='rating_num').text
    print(f"电影：{title}，评分：{rating}")
