import re
import requests


def get_urls():
    url = 'https://qq.yh31.com/zjbq/2920180.html'

    response = requests.get(url)
    # print(response.text)

    url_add = r'<img border="0".*? src="(.*?)"'
    # 第三步
    url_list = re.findall(url_add, response.text)
    # print(url_list)
    return url_list


def get_gif(url, name):
    response = requests.get(url)
    with open('D:\logs\%d.gif' % name, 'wb') as ft:
        ft.write(response.content)


a = 1
url_list = get_urls()
for url in url_list:
    com_url = 'https://qq.yh31.com' + url

    # print(com_url)

    get_gif(com_url, a)
    a += 1
