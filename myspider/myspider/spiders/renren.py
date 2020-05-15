# -*- coding: utf-8 -*-
import re
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/224803205']

    def start_requests(self):
        cookies = "anonymid=ka7ufn1f8n3vja; depovince=BJ; _r01_=1; taihe_bi_sdk_uid=ae3b614c8f1be1d52910e71198dfeaee; taihe_bi_sdk_session=eddaa01774307ea20192cdd9b53127ed; ick_login=5f10c478-9779-4005-95a6-c19052f4c972; _de=F55CD8F60A539A85E672161CC1DD0FB944B0A57815E527E7696BF75400CE19CC; ick=c8fb98b5-275d-4c2f-afb4-5a61f3e2c572; __utma=151146938.204674319.1589525617.1589525617.1589525617.1; __utmc=151146938; __utmz=151146938.1589525617.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=151146938.4.10.1589525617; jebecookies=a0c0da99-9668-4408-bbc5-bd1e7d285da7|||||; p=f0f5e86f85d9025e00aacdb2e76813d55; first_login_flag=1; ln_uact=zhangrongqianglo@163.com; ln_hurl=http://head.xiaonei.com/photos/20070526/1515/main475041.jpg; t=e0755f30fcf2debfff4320f6f45019cb5; societyguester=e0755f30fcf2debfff4320f6f45019cb5; id=224803205; xnsid=e8e1d0ea; ver=7.0; loginfrom=null; jebe_key=21aca4f9-59c0-410d-b7c4-d8fe1fcc44b7%7C3215767af58978375c62df507eefcd66%7C1589525755818%7C1%7C1589525757634; wp_fold=0"

        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split(";")}
        print("111111:")
        print(cookies)
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        # with open("renren.html", 'w', encoding='utf-8') as f:
        #     f.write(response.body.decode())
        #     # f.write(str(response.body))
        #
        # name = re.findall("张荣强", response.body.decode())
        # print(name)

        yield scrapy.Request(
            'http://www.renren.com/224803205/profile',
            callback=self.detail
        )

    def detail(self, response):
        name = re.findall("张荣强", response.body.decode())
        print(name)

