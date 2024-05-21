from WebDriver.driver import ChromeDriver
from Pages.MainPage.mainPage import MainPage
from TestEntities.registration import RegistrationData


class InvalidEmail:
    def __init__(self):
        url = "https://koshelek.ru/"

        self.regData = RegistrationData(
            "vladzor",
            "example",
            "Qwerty123"
        )

        self.driver = ChromeDriver(url).getDriver()

    def main(self):
        result = MainPage(self.driver).openRegistrationPage()\
            .enterName(self.regData)\
            .enterEmail(self.regData)\
            .enterPassword(self.regData)\
            .submitRules()\
            .submitRegistration()\
            .checkForCaptcha()

        if not result:
            print("Test success")
        else:
            print("Test failed")

        self.driver.quit()
