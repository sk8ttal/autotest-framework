from WebDriverItems.shadowWebItems import WebItem
from WebDriver.driverActions import Actions

class CaptchaFrame:
    def __init__(self, driver):
        self.driver = driver
    
    def checkForCaptcha(self):
        Actions().switchToFrame("(//iframe)[last()]", self.driver)
        frame = WebItem("//div[@class='button-submit button']", "Кнопка пропустить", self.driver)
        
        try:
            frame.click()
            print("Ура, капча!")
            return True
        except Exception:
            print("Нет капчи :(")
            return False