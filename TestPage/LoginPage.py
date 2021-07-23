from selenium.webdriver.common.by import By
import PO.BasePage

class LoginPage(BasePage):

    username=(By.ID,'userName')
    pwd=(By.ID,'passWord')
    login_button=(By.XPATH,'/html/body/div/div/div/div[2]/div/form/div[4]/div/div/span/button')

    def username_input(self,value):
        self.my_send_keys(self.username,value)
    def pwd_input(self,value):
        self.my_send_keys(self.pwd,value)

    def click_button(self):
        self.my_click(self.login_button)

    def login(self,username,password):
        '''
        登陆方法
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        self.username_input(username)
        self.pwd_input(password)
        self.click_button()