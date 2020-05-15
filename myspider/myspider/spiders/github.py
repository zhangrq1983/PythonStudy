# -*- coding: utf-8 -*-
import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):

        # commit: Sign in
        # authenticity_token: A36fYWB3x6hLQBAFdQ8A/Bs8mDi/6VbA7425F9uhVTZXbzijiJrP8NmP1DNOVmnrcnD8uTe6XEOaXz6i0o2toA==
        # ga_id: 486094911.1582633516
        # login: zhangrongqiang1983 @ aliyun.com
        # password: 123
        print(123)

        commit = response.xpath("//input[@name='commit']/@value").extract_first()
        authenticity_token = response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        ga_id = response.xpath("//input[@name='ga_id']/@value").extract_first()

        post_data = {
            'login': 'zhangrongqiang1983@aliyun.com',
            'password': '123',
            'commit': str(commit),
            'authenticity_token': str(authenticity_token),
            'ga_id': str(ga_id)
        }

        # post_data = dict(
        #     login='zhangrongqiang1983@aliyun.com',
        #     password='123'
        # )

        print(post_data)

        yield scrapy.FormRequest(
            'https://github.com/session',
            formdata=post_data,
            callback=self.after_login
        )

    def after_login(self, response):
        with open("github.html", 'w', encoding='utf-8') as f:
            f.write(response.body.decode())


