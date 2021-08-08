
from base import BasePage

class LoginPage(BasePage):

	url = BasePage.url + ''
	user = (By.NAME,'accounts')
	pwd = (By.NAME,'pwd')
	button = (By.XPATH,'')
	
    def login(self,account,password):
        self.visit();
		self.input_(self.user,account)
		self.input_(self.pwd,password)
		self.click(self.button)

if __name__ == '__main__'
	driver = webdriver.Chrome()
    