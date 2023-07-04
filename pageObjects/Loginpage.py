from selenium.webdriver.common.by import By

class loginpage():
     # locators of all the elements
     textbox_username_name ="username"
     textbox_username_id ="password"
     button_login_xpath="//button[@type='submit']"
     link_logout="Logout"

     def __init__(self,driver):    #constructor use
          self.driver=driver

     def setusername(self, username):
          self.driver.find_element(By.NAME,self.textbox_username_name).send_keys(username)

     def setpassword(self, password):
          self.driver.find_element(By.NAME,self.textbox_username_id).send_keys(password)

     def clickLogin(self):
          self.driver.find_element(By.XPATH,self.button_login_xpath).click()

     def clickLogout(self):
          self.driver.find_element(By.LINK_TEXT,self.link_logout).click()