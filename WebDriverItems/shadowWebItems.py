from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from WebDriverItems.baseitems import WebItem

class ShadowWebItem(WebItem):
    def __init__(self, shadowRoot, elementPath, description, driver: webdriver.Chrome):
        self.elementPath = elementPath
        self.description = description
        self.driver = driver
        
        self.shadowRoot = self.driver.find_element(By.CSS_SELECTOR, shadowRoot).shadow_root
        self.element = self.shadowRoot.find_element(By.CSS_SELECTOR, self.elementPath)