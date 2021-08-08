
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    :   2020/4/15
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
 
from selenium import webdriver
from time import sleep
import os
 
base_url = 'https://www.baidu.com'
filePath = './tools/chromedriver.exe'
result = os.path.exists(filePath)

browser = webdriver.Chrome(filePath)
browser.get(base_url)
 
# window.scrollTo()方法用于设置浏览器窗口滚动条的水平和垂直位置。方法的第一个参数表示水平的左间距，第二个参数表示垂直的上边距。
browser.maximize_window()
browser.find_element_by_id('kw').send_keys('百度')
browser.find_element_by_id('su').click()
sleep(2)
 
# 通过javascript设置浏览器窗口的滚动条位置
js = "window.scrollTo(100, 450);"
browser.execute_script(js)
sleep(2)

browser.quit()