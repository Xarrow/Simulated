# -*- coding:utf-8 -*-
"""
version: 1.0
author: ZhangJian
site: unkonwn
software: PyCharm
file: alpha.py
time: 2016/9/30 15:07
"""
import logging
import requests
import lxml.html

level = logging.DEBUG
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
datefmt = '%Y-%m-%d %H:%M'
logging.basicConfig(level=level, format=format, datefmt=datefmt)
logger = logging.getLogger(__name__)

MUSIC_URL = 'http://music.163.com/'
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "_ntes_nnid=2a34c9331ccbb993963509d4a8d2da6e,1475209839563; _ntes_nuid=2a34c9331ccbb993963509d4a8d2da6e; playerid=41620608; __utma=94650624.1093574736.1475209827.1475211738.1475218290.3; __utmb=94650624.52.10.1475218290; __utmc=94650624; __utmz=94650624.1475209827.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); JSESSIONID-WYYY=189522fc707b31e09da46458682b0f48f456a54415cc67b58800994f7a35b3c1dc8759583521b8252143121a0187906c88aebf44e67bd753ce89bb6dfe51c2239d18e1c1f898062254de7b35237bd78f3789337408fcccddc00c3fe32d047c3d194275294337b9c70da74209d2f1d52dd508e64ae69c28241612be00bad582d9ebfd66a4%3A1475227010192; _iuqxldmzr_=25",
    "Host": "music.163.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
}


def hook_handle(r, *args, **kwargs):
    '''
    Hook handle
    :param url:
    :return:
    '''
    print r.content


def sub_handle(u):
    u2 = MUSIC_URL + u
    print u2
    r = requests.get(url=u2, headers=HEADERS, timeout=8)
    h = lxml.html.fromstring(r.content)
    author_name = ''.join(h.xpath("//span[@class='name']/a/text()"))
    author_link = ''.join(h.xpath("//span[@class='name']/a/@href"))
    author_face = ''.join(h.xpath("//a[@class='face']/img/@src"))
    tit = ''.join(h.xpath("//h2[@class='f-ff2 f-brk']/text()"))
    cover = ''.join(h.xpath("//img[@class='j-img']/@src"))
    name = ''.join(h.xpath("//span[@class='name']/a/text()"))
    time = ''.join(h.xpath("//span[@class='time s-fc4']/text()"))
    fav = ''.join(h.xpath("//a[@class='u-btni u-btni-fav ']/@data-count"))
    share = ''.join(h.xpath("//a[@class='u-btni u-btni-share ']/@data-count"))
    comment = ''.join(h.xpath("//span[@id='cnt_comment_count']/text()"))

    intro = ''.join(h.xpath("//p[@id='album-desc-more']//text()"))
    print 5 * '-----------'
    print 'author_name :\t%s' % author_name
    print 'author_link :\t%s' % author_link
    print 'author_face :\t%s' % author_face
    print 'tit:\t%s' % tit
    print 'cover:\t%s' % cover
    print 'name :\t%s' % name
    print 'time :\t%s' % time
    print 'fav :\t %s' % fav
    print 'share :\t%s' % share
    print 'comment :\t%s' % comment
    print 'intro:\t %s' % intro


def get_all(url):
    '''
    递归处理
    :param url:
    :return:
    '''

    try:
        # print '-->' + MUSIC_URL + url
        r = requests.get(url=url, headers=HEADERS, timeout=8)
        h = lxml.html.fromstring(r.content)
        links = h.xpath("//p[@class='dec']/a/@href")
        magicBox = list()
        for i in links:
            sub_handle(i)

    except Exception as e:
        print e
        pass


def tmp():
    for i in xrange(0, 1470, 35):
        url = "http://music.163.com/discover/playlist/?order=hot&cat=全部&limit=35&offset=%d" % i
        get_all(url)


if __name__ == '__main__':
    import threadpool

    pool = threadpool.ThreadPool(100)
    reqs = threadpool.makeRequests(tmp(), range(1, 100))
    [pool.putRequest(req) for req in reqs]
    pool.wait()
