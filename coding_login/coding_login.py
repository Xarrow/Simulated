# coding=gbk
__author__ = 'root'
import requests
import hashlib
import ast
import json
import time

class Coding:
    # function structure
    def __init__(self, username, password):
        phone = None
        # 基本登陆信息,在构造函数中的变量，每次调用都被类的内部共享，这里指的的是
        # login中的session 和cookies会在类中其他函数共享，从而保证一个session连接
        self.username = username
        self.password = hashlib.sha1(password).hexdigest()
        self.url_getCookie = "https://coding.net/api/captcha/login"
        self.url_login = "https://coding.net/api/login"
        self.url_sendMsg = "https://coding.net/api/user/generate_phone_code"
        self.login_data = dict(email=self.username, password=self.password, remember_me="false")
        self.headers = {
            'Accept': 'image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,ja;q=0.2,zh-TW;q=0.2,en-GB;q=0.2',
            'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko)"
                          " Chrome/43.0.2357.81 Safari/537.36"}
        self.session = requests.session()

        self.startId = ""

    def login(self):
        """get login and return cookies"""
        cookies = dict(self.session.get(self.url_getCookie).cookies)
        print "[+] Cookies info:%s" % cookies
        # send a post to login 发送一个登陆post
        login_session = self.session.post(url=self.url_login,
                                          headers=self.headers,
                                          data=self.login_data,
                                          cookies=cookies)
        info = str(login_session.text.encode("gbk"))
        print "[+] Login info:%s" % info
        info_dict = ast.literal_eval(info[info.find('"data":') + len('"data":'):info.find('"followed"') - 1] + "}")
        print "[+]标签:" + info_dict["tags_str"]
        print "[+]年龄:" + info_dict["tags"]
        if info_dict["sex"] == 0:
            info_dict["sex"] = "男"
        else:
            info_dict["sex"] = "女"
        print "[+]性别:" + info_dict["sex"]
        print "[+]手机:" + info_dict["phone"]
        print "[+]生日:" + info_dict["birthday"]
        print "[+]头像:" + info_dict["avatar"]
        print "[+]账号创建时间:" + str(info_dict["created_at"])
        print "[+]最后登陆时间:" + str(info_dict["last_logined_at"])
        print "[+]最后活动时间:" + str(info_dict["last_activity_at"])
        print "[+]邮箱:" + info_dict["email"]
        print "[+]关注者:" + str(info_dict["follows_count"])
        print "[+]被关注数:" + str(info_dict["fans_count"])
        print "[+]冒泡条数:" + str(info_dict["tweets_count"])

        return cookies

    def pp(self):
        """post a tweet
        :rtype : object
        """

        cookies = self.login()
        # 冒泡编码 unicode->utf-8
        # 解决：http://www.crifan.com/unicodeencodeerror_gbk_codec_can_not_encode_character_in_position_illegal_multibyte_sequence/
        tweet = raw_input('[+] Enter your tweet to pp:').decode('gbk', 'ignore').encode('utf-8')
        # 重新构造headers，添加origin,referer，防止其验证验证，但是实际没有验证
        self.headers["Origin"] = "https://coding.net"
        self.headers["Referer"] = "https://coding.net/pp"
        # 改变headers 从而改变客户端为移动端
        change_platform = raw_input("[+] Choose other platform,default PC platform (Yes/No) :").upper()
        if not change_platform != "YES":
            self.headers["User-Agent"] = 'Mozilla/5.0 (Linux; Android 4.3; Nexus 10 Build/JSS15Q) ' \
                                         'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                                         'Chrome/42.0.2307.2 Mobile Safari/537.36'
        print "[+] structure a new headers:%s" % self.headers
        # 不知道为什么在冒泡时 coding对cookies没有要求，这里可以不添加
        send_tweet = self.session.post(url="https://coding.net/api/tweet",
                                       headers=self.headers,
                                       data={"content": tweet},
                                       cookies=cookies)
        print "[+] tweet info :%s" % send_tweet.text
        print "[+] cookies:%s"%self.session.cookies

        tweet_url ="https://coding.net/api/tweet/public_tweets"
        tweet_text = self.session.get(url=tweet_url,headers=self.headers,cookies=cookies).text
        self.startId = int(tweet_text[tweet_text.index('{"id":')+len('{"id":'):tweet_text.index('{"id":')+len('{"id":')+5])
        print "[+] tweet info:%s"%tweet_text
        print "[+] pp id %d"%self.startId

    def deletePP(self):
        print self.startId
        # need not to set cookies
        # cookies = self.login()
        delete_url = "https://coding.net/api/tweet/"+str(self.startId)
        delete_pp = self.session.delete(url=delete_url,
                                        headers=self.headers)
        # 删除冒泡
        print "[+] delete pp info:%s"%delete_pp.text

    def zan(self):
        cookies = self.login()
        tweet_url ="https://coding.net/api/tweet/public_tweets"
        tweet_text = self.session.get(url=tweet_url,headers=self.headers,cookies=cookies).text
        endId = int(tweet_text[tweet_text.find('{"id":')+len('{"id":'):tweet_text.find('{"id":')+len('{"id":')+5])
        startId = int(tweet_text[tweet_text.rindex('{"id":')+len('{"id":'):tweet_text.rindex('{"id":')+len('{"id":')+5])

        for count in xrange(startId,endId):
            zan_url = "https://coding.net/api/tweet/"+str(count)+"/like"
            time.sleep(1)
            zan_tweet = self.session.post(url=zan_url,
                                          headers= self.headers,
                                          cookies=cookies)
            print "[+] zan from %d  to %d ,left:%d, time:%s,info:%s"\
                  %(startId,endId,endId-count,time.ctime(),zan_tweet.text)
            startId+=1

    def getData(self):
        """get tweet data"""
        payload = dict(last_id="99999999", sort="time")
        url = "https://coding.net/api/tweet/public_tweets"
        data = self.session.get(url=url).json()
        data_json = json.dumps(data, ensure_ascii=False)
        print data_json

    def send_msg_valid(self):
        """send msg"""
        cookies = self.login()
        phone = raw_input("[+] Enter your phone number:")
        send_msg = self.session.post("https://coding.net/api/user/generate_phone_code",
                                     dict(phone=phone),cookies=cookies)
        print "[+] cookies:%s"%self.session.cookies
        print "[+] Send info :%s" % send_msg.text


if __name__ == "__main__":
    # username = raw_input("[+]Enter your username:")
    # password = raw_input("[+]Enter your password:")
    # phone = raw_input("[+]Enter your phone:")
    # test = coding(username,password,phone)
    # print test.login_and_send()
    test = Coding("yuious", "XXXXXXXXX")
    test.pp()
    choose = raw_input("[+] 是否删除冒泡(Yes/No)：")
    if choose[0].upper()=='Y':
        test.deletePP()
    else:
        pass
    # test.send_msg_valid()
    # test.getData()
    # test.zan()