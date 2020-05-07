import re
import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = 'http://maoyan.com/board/4?offset=0'
response = requests.get(url, headers=headers)
print(response.text)

data = re.findall('<p class="star">(.*?)</p>.*?<i class="integer">(\d\.)</i>', response.text, re.S)
# print(data)

for i in data:
    print(i)

"""
<dd>
                        <i class="board-index board-index-2">2</i>
    <a href="/films/4883" title="钢琴家" class="image-link" data-act="boarditem-click" data-val="{movieId:4883}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/bcbe59fc51580317adf94537a61a1a26142090.jpg@160w_220h_1e_1c" alt="钢琴家" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/4883" title="钢琴家" data-act="boarditem-click" data-val="{movieId:4883}">钢琴家</a></p>
        <p class="star">
                主演：艾德里安·布洛迪,艾米莉娅·福克斯,米哈乌·热布罗夫斯基
        </p>
<p class="releasetime">上映时间：2002-05-24(法国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">8.</i><i class="fraction">8</i></p>        
    </div>

      </div>
    </div>

                </dd>
"""


