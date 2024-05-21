from Pages.RegistrationPage.mainPage import RegistrationPage
from WebDriverItems.baseitems import WebItem
import time

class MainPage:
    def __init__(self, driver):
        self.driver = driver
    
    def openRegistrationPage(self) -> RegistrationPage:
        WebItem("//span[text()='Зарегистрироваться']", "Кнопка регистрации", self.driver).click()
        time.sleep(5)
                
        return RegistrationPage(self.driver)