import time
import unittest
from selenium import webdriver
import HtmlTestRunner
import sys
sys.path.append("C://Users/dhaya/Python UnitTestProject_POM Based")
from pageObjects.Loginpage import loginpage

class logintest(unittest.TestCase):
    baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    driver = webdriver.Chrome()


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_Login(self):
        lp = loginpage(self.driver)
        lp.setusername(self.username)
        lp.setpassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\reports"))
