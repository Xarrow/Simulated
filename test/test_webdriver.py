# -*- coding:utf-8 -*-
# Author: zhangjian
# Time :20160927
# see :http://seleniumhq.github.io/selenium/docs/api/py/
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utils import config


def p_test():
    startTime = time.time()
    driver = webdriver.PhantomJS(config.PHANTOMJS_DRIVER_PATH)
    driver.get("http://tuniu.com")
    # print driver.page_source
    endTime = time.time()
    print (endTime - startTime)


if __name__ == '__main__':
    p_test()
