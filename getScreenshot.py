#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    :   2020/4/15
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
 
from selenium import webdriver
from time import sleep
 
base_url = 'http://www.baidu.com/'
browser = webdriver.Chrome('./tools/chromedriver.exe')
 
browser.get(base_url)
 
browser.find_element_by_id('kw').send_keys('python selenium')
browser.find_element_by_id('su').click()
sleep(2)
 
# 截取当前窗口并指定报错截图的位置
# browser.get_screenshot_as_file('ScreenShot/14_screenShot.jpg')
browser.get_screenshot_as_file('./ScreenShot/14_screenShot.png')
 
browser.quit()