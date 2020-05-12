import xml

import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = 'http://maoyan.com/board/4?offset=1'
# response = requests.get(url, headers=headers)
response = requests.get(url, headers)
print(response.text)


res_html = etree.HTML(response.text)
print(res_html)
dd_list = res_html.xpath('//dl//dd')

for dd in dd_list:
    print(dd.xpath('.//a/img[2]/@data-src')[0])
    print(dd.xpath('.//p[@class="star"]/text()')[0].strip())
    print(dd.xpath('.//p[@class="releasetime"]/text()')[0])
    print(dd.xpath('.//i[@class="integer"]/text()')[0])
    print(dd.xpath('.//i[@class="fraction"]/text()')[0])

"""
 <dd>
                        <i class="board-index board-index-10">10</i>
    <a href="/films/790" title="蝙蝠侠：黑暗骑士" class="image-link" data-act="boarditem-click" data-val="{movieId:790}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/09658109acfea0e248a63932337d8e6a4268980.jpg@160w_220h_1e_1c" alt="蝙蝠侠：黑暗骑士" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/790" title="蝙蝠侠：黑暗骑士" data-act="boarditem-click" data-val="{movieId:790}">蝙蝠侠：黑暗骑士</a></p>
        <p class="star">
                主演：克里斯蒂安·贝尔,希斯·莱杰,阿伦·伊克哈特
        </p>
<p class="releasetime">上映时间：2008-07-14(阿根廷)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">3</i></p>        
    </div>

      </div>
    </div>

                </dd>
"""

