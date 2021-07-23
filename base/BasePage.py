from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class BasePage():
    '''
    封装浏览器基本操作
    公共方法：等待时间，截图，点击，日志，浏览器所有操作
    需求：任何点击，自动去加等待时间
    关键字驱动：
        公共方法关键字：
        业务关键字：操作经常绑定在一起的，封装成关键字
    '''
    
    def __init__(self,driver):
        filePath = './tools/chromedriver.exe'
        self.driver = webdriver.Chrome(filePath)

    def find_ele(self,loc):
        '''
        找元素的方法，加上显式等待时间
        :param loc:
        :return: ele:webdriver对象
        '''
        try:
            ele=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            print(e)
        return ele

    def my_send_keys(self,loc,value):
        '''
        输入方法
        :param loc: 元素的定位
        :param value: 输入的值
        :return:
        '''
        self.find_ele(loc).send_keys(value)
    def my_click(self,loc):
        '''
        点击方法
        :param loc: 元素的定位
        :return: 
        '''
        self.find_ele(loc).click()

    def locator(self,loc):
        return self.driver.find_element(*loc)
        