"""
Базовый класс для Page Object Pattern
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.timeout = timeout
    
    def open(self, url):
        """Открыть страницу"""
        self.driver.get(url)
        return self
    
    def find_element(self, locator):
        """Найти элемент с ожиданием"""
        return self.wait.until(
            EC.presence_of_element_located(locator),
            f"Элемент не найден: {locator}"
        )
    
    def find_elements(self, locator):
        """Найти несколько элементов"""
        return self.wait.until(
            EC.presence_of_all_elements_located(locator),
            f"Элементы не найдены: {locator}"
        )
    
    def click(self, locator):
        """Кликнуть по элементу"""
        element = self.find_element(locator)
        element.click()
        return element
    
    def type(self, locator, text):
        """Ввести текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return element
    
    def get_text(self, locator):
        """Получить текст элемента"""
        return self.find_element(locator).text
    
    def is_displayed(self, locator):
        """Проверить видимость элемента"""
        try:
            return self.find_element(locator).is_displayed()
        except:
            return False
    
    def wait_for_element(self, locator):
        """Ждать появления элемента"""
        return self.find_element(locator)
    
    def wait_for_element_to_disappear(self, locator):
        """Ждать исчезновения элемента"""
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            f"Элемент не исчез: {locator}"
        )
    
    def take_screenshot(self, filename):
        """Сделать скриншот"""
        self.driver.save_screenshot(filename)
        print(f"Скриншот сохранен: {filename}")
    
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url