from WebDriverItems.shadowWebItems import ShadowWebItem, WebItem
from Pages.RegistrationPage.captchaFrame import CaptchaFrame

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.field = lambda fieldName: ShadowWebItem("div[class='remoteComponent']", f"form[novalidate='novalidate']  [data-wi='{fieldName}']", f"Поле {fieldName}", self.driver)
        self.input = lambda fieldName: ShadowWebItem("div[class='remoteComponent']", f"form[novalidate='novalidate']  [data-wi='{fieldName}'] input", f"Импут поля {fieldName}", self.driver)
    
    def enterName(self, regData):
        self.field("user-name").click()
        self.input("user-name").sendKeys(regData.name)
        
        return RegistrationPage(self.driver)
    
    def enterEmail(self, regData):
        self.field("identificator").click()
        self.input("identificator").sendKeys(regData.email)
        
        return RegistrationPage(self.driver)
    
    def enterPassword(self, regData):
        self.field("password").click()
        self.input("password").sendKeys(regData.password)
        
        return RegistrationPage(self.driver)
                
    def enterReferalCode(self, regData):
        self.field("referral").click()
        self.input("referral").sendKeys(regData.promocode)
        
        return RegistrationPage(self.driver)
    
    def submitRules(self):
        ShadowWebItem("div[class='remoteComponent']", "[specialtoken='k-checkbox-auth']", "Чекбокс пользовательского соглашения", self.driver).click()
        
        return RegistrationPage(self.driver)
    
    def submitRegistration(self):
        ShadowWebItem("div[class='remoteComponent']", "form[novalidate='novalidate']  [data-wi='submit-button']", "Кнопка далее", self.driver).doubleClick()
        WebItem("(//iframe)[last()]", "Фрейм с капчей", self.driver).waitElementDisplayed()
        
        return CaptchaFrame(self.driver)
    