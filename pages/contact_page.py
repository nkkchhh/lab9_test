"""
Page Object для контактной формы
"""

from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class ContactPage(BasePage):
    # Локаторы (селекторы элементов)
    # Поля ввода
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "email")
    PHONE_INPUT = (By.ID, "phone")
    AGE_SELECT = (By.ID, "age")
    MESSAGE_TEXTAREA = (By.ID, "message")
    
    # Радиокнопки темы
    SUBJECT_QUESTION = (By.ID, "question")
    SUBJECT_COMPLAINT = (By.ID, "complaint")
    SUBJECT_SUGGESTION = (By.ID, "suggestion")
    
    # Чекбоксы
    AGREE_CHECKBOX = (By.ID, "agree")
    SUBSCRIBE_CHECKBOX = (By.ID, "subscribe")
    
    # Кнопки
    SUBMIT_BUTTON = (By.ID, "submitBtn")
    RESET_BUTTON = (By.ID, "resetBtn")
    
    # Сообщения
    SUCCESS_MESSAGE = (By.ID, "successMessage")
    ERROR_MESSAGE = (By.ID, "errorMessage")
    
    # Ошибки полей
    NAME_ERROR = (By.ID, "nameError")
    EMAIL_ERROR = (By.ID, "emailError")
    PHONE_ERROR = (By.ID, "phoneError")
    SUBJECT_ERROR = (By.ID, "subjectError")
    MESSAGE_ERROR = (By.ID, "messageError")
    AGREE_ERROR = (By.ID, "agreeError")
    
    # Счетчик символов
    MESSAGE_COUNTER = (By.ID, "messageCounter")
    
    def open_contact_form(self):
        """Открыть форму контактов"""
        self.open("file:///путь/к/contact_form.html")
        return self
    
    def fill_name(self, name):
        """Заполнить поле имени"""
        self.type(self.NAME_INPUT, name)
        return self
    
    def fill_email(self, email):
        """Заполнить поле email"""
        self.type(self.EMAIL_INPUT, email)
        return self
    
    def fill_phone(self, phone):
        """Заполнить поле телефона"""
        self.type(self.PHONE_INPUT, phone)
        return self
    
    def select_age(self, age_group):
        """Выбрать возрастную группу"""
        from selenium.webdriver.support.ui import Select
        select = Select(self.find_element(self.AGE_SELECT))
        select.select_by_visible_text(age_group)
        return self
    
    def fill_message(self, message):
        """Заполнить поле сообщения"""
        self.type(self.MESSAGE_TEXTAREA, message)
        return self
    
    def select_subject(self, subject_type):
        """Выбрать тему обращения"""
        if subject_type == "question":
            self.click(self.SUBJECT_QUESTION)
        elif subject_type == "complaint":
            self.click(self.SUBJECT_COMPLAINT)
        elif subject_type == "suggestion":
            self.click(self.SUBJECT_SUGGESTION)
        return self
    
    def set_agreement(self, agree=True):
        """Установить/снять согласие"""
        checkbox = self.find_element(self.AGREE_CHECKBOX)
        if agree and not checkbox.is_selected():
            checkbox.click()
        elif not agree and checkbox.is_selected():
            checkbox.click()
        return self
    
    def set_subscription(self, subscribe=True):
        """Установить/снять подписку"""
        checkbox = self.find_element(self.SUBSCRIBE_CHECKBOX)
        if subscribe and not checkbox.is_selected():
            checkbox.click()
        elif not subscribe and checkbox.is_selected():
            checkbox.click()
        return self
    
    def submit_form(self):
        """Отправить форму"""
        self.click(self.SUBMIT_BUTTON)
        time.sleep(2)  # Ждем отправки
        return self
    
    def reset_form(self):
        """Очистить форму"""
        self.click(self.RESET_BUTTON)
        return self
    
    def is_success_message_displayed(self):
        """Проверить отображение сообщения об успехе"""
        return self.is_displayed(self.SUCCESS_MESSAGE)
    
    def is_error_message_displayed(self):
        """Проверить отображение сообщения об ошибке"""
        return self.is_displayed(self.ERROR_MESSAGE)
    
    def get_success_message_text(self):
        """Получить текст сообщения об успехе"""
        return self.get_text(self.SUCCESS_MESSAGE)
    
    def get_error_message_text(self):
        """Получить текст сообщения об ошибке"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def get_field_error_text(self, field_name):
        """Получить текст ошибки поля"""
        errors = {
            'name': self.NAME_ERROR,
            'email': self.EMAIL_ERROR,
            'phone': self.PHONE_ERROR,
            'subject': self.SUBJECT_ERROR,
            'message': self.MESSAGE_ERROR,
            'agree': self.AGREE_ERROR
        }
        if field_name in errors:
            return self.get_text(errors[field_name])
        return ""
    
    def get_message_counter_text(self):
        """Получить текст счетчика символов"""
        return self.get_text(self.MESSAGE_COUNTER)
    
    def fill_all_valid_data(self):
        """Заполнить все поля валидными данными"""
        self.fill_name("Иван Иванов")
        self.fill_email("ivan@example.com")
        self.fill_phone("+7 (999) 123-45-67")
        self.select_age("26-35 лет")
        self.select_subject("question")
        self.fill_message("Это тестовое сообщение для проверки работы формы.")
        self.set_agreement(True)
        self.set_subscription(True)
        return self
    
    def is_form_valid(self):
        """Проверить что все обязательные поля заполнены"""
        name = self.find_element(self.NAME_INPUT).get_attribute("value")
        email = self.find_element(self.EMAIL_INPUT).get_attribute("value")
        message = self.find_element(self.MESSAGE_TEXTAREA).get_attribute("value")
        agree = self.find_element(self.AGREE_CHECKBOX).is_selected()
        

        return bool(name and email and message and agree)
