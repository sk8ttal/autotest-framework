from selenium.webdriver.common.by import By

class Actions:
    def refresh(self, driver):
        driver.refresh()

    def switchToFrame(self, frame, driver):
        driver.switch_to.frame(driver.find_element(By.XPATH, frame))
