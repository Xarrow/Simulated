# -*- coding:utf-8 -*-
import time

import utils.config as CONFIG
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import lxml.html

KUAIDAILI = "http://www.kuaidaili.com/free/outha/"


def getMetaData(pageUrl):
    driver = webdriver.Chrome(executable_path=CONFIG.CHROME_DRIVER_PATH)
    # driver = webdriver.PhantomJS(executable_path=CONFIG.PHANTOMJS_DRIVER_PATH)
    for i in xrange(1, 1260, 1):
        url = 'http://www.kuaidaili.com/free/outha/' + str(i)
        driver.get(url)
        c = driver.page_source
        h = lxml.html.fromstring(c)
        nextUrl = ''.join(h.xpath("//div[@id='listnav']/ul/li[3]/a/@href"))
        hosts = h.xpath("//tr/td[1]/text()")
        ports = h.xpath("//tr/td[2]/text()")
        protocols = h.xpath("//tr/td[4]/text()")

        xyz = zip(protocols, hosts, ports)
        for i in xyz:
            print i


# getMetaData(KUAIDAILI)

def vistTaoBaoByPhantomjs():
    startTime = time.time()
    driver = webdriver.PhantomJS(executable_path=CONFIG.PHANTOMJS_DRIVER_PATH)
    driver.get("http://taobao.com")
    h = lxml.html.fromstring(driver.page_source)
    for i in h.xpath("//a/text()"):
        pass
    driver.close()
    endTime = time.time()
    print 'phantomjs Time is :%s' % (endTime - startTime)


def vistTaoBaoByChrome():
    startTime = time.time()
    driver = webdriver.Chrome(executable_path=CONFIG.CHROME_DRIVER_PATH)
    driver.get("http://taobao.com")
    h = lxml.html.fromstring(driver.page_source)
    for i in h.xpath("//a/text()"):
        pass
    driver.close()
    endTime = time.time()
    print 'chrome Time is :%s' % (endTime - startTime)


def visitQQ():
    driver = webdriver.Chrome(executable_path=CONFIG.CHROME_DRIVER_PATH)
    driver.get(
        "http://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=http%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=http%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=%E6%89%8B%E6%9C%BAQQ%E7%A9%BA%E9%97%B4&pt_qr_link=http%3A//z.qzone.com/download.html&self_regurl=http%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=http%3A//z.qzone.com/download.html")
    # driver.find_element_by_id('img_out_1056484272').click()
    driver.find_element_by_id('switcher_plogin').click()
    driver.find_element_by_id('u').clear()
    driver.find_element_by_id('u').send_keys('1056484272')
    driver.find_element_by_id('p').clear()
    driver.find_element_by_id('p').send_keys('#Yuious135')
    driver.find_element_by_id('login_button').click()
    print driver.get_cookies()
    driver.get('http://user.qzone.qq.com/1056484272')
    js = '''
        alert(document.cookie)
    '''
    driver.execute_async_script(js)


# vistTaoBaoByChrome()
# vistTaoBaoByPhantomjs()
visitQQ()
