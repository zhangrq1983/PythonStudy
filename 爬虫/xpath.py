import requests
from lxml import etree


def get_urls(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    response = requests.get(url, headers)
    return response.text


def html_result(text):
    html = etree.HTML(text)
    img_urls = html.xpath('//div[@class="main-content"]//img/@src')
    return img_urls


def get_img(url, img_name):
    print(url, img_name)
    response = requests.get(url)
    with open('D:\logs\%s.jpg' % img_name, 'wb') as f:
        f.write(response.content)


def main():
    url = 'https://www.manhuadao.cn/Comic/ComicView?comicid=58ddb12627a7c1392c23c427&chapterid=2182076'
    result = get_urls(url)
    img_urls = html_result(result)

    for u in img_urls:
        image_name = u.split('/')[-1]
        image_name2 = image_name.split('.')[0]
        image_name3 = image_name2.split('-')[-1]
        get_img(u, image_name3)


if __name__ == '__main__':
    main()





