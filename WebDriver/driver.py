from selenium import webdriver
import time

class ChromeDriver():
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(5)
        
    def getDriver(self):
        return self.driver
    
    