from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class WebItem:
    def __init__(self, path, description, driver: webdriver):
        self.path = path
        self.description = description
        self.driver = driver

        self.element = self.driver.find_element(By.XPATH, self.path)

    # Метод для проверки наличия элемента на странице
    def waitElementDisplayed(self, maxWait_s=5, duration_s=1):
        print("Ожидание отображения " + self.description)

        timePassed = 0
        while (True):
            if timePassed < maxWait_s:
                try:
                    self.element.is_displayed()
                    return True
                except Exception as e:
                    time.sleep(duration_s)
                    timePassed += duration_s
            else:
                print("Не удалось найти элемент " + self.description)
                return False

    # Метод для нажатия на элемент
    def click(self):
        self.waitElementDisplayed()
        print("Нажатие на " + self.description)
        self.element.click()
        time.sleep(1)

    # Метод для двойного нажатия на элемент
    def doubleClick(self):
        self.waitElementDisplayed()
        print("Двойное нажатие на " + self.description)
        self.element.click()
        self.element.click()
        time.sleep(1)

    # Метод для ввода текста в элемент

    def sendKeys(self, text):
        self.waitElementDisplayed()
        print(f"Ввод текста {text} в {self.description}")
        self.element.send_keys(text)
        time.sleep(1)
