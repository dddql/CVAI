import requests
from bs4 import BeautifulSoup
import os

# 设置目标URL
#url = 'https://nordicmicroalgae.org/gallery/all/'
url = 'https://nordicmicroalgae.org/gallery/all/?media=azadinium-caudatum-var-margalefii-2'

# 发送HTTP请求获取网页内容
response = requests.get(url)
response.raise_for_status()  # 检查请求是否成功

# 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 创建文件夹保存图片
if not os.path.exists('images'):
    os.makedirs('images')

# 查找所有图片标签
images = soup.find_all('img')

for img in images:
    img_url = img.get('src')
    if not img_url:
        continue
    
    # 处理相对路径的图片链接
    if not img_url.startswith('http'):
        img_url = 'https://nordicmicroalgae.org' + img_url

    # 获取图片的名称
    img_name = os.path.basename(img_url)

    # 下载图片并保存
    img_response = requests.get(img_url)
    img_response.raise_for_status()

    with open(os.path.join('images', img_name), 'wb') as f:
        f.write(img_response.content)

    print(f'已下载 {img_name}')

print('所有图片已下载完成。')
