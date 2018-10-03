from django.contrib.auth.models import User
from django.test import override_settings
from django.urls import reverse

from main.base_selenium_test_case import BaseSeleniumTestCase


class IndexPageObject:
    def __init__(self):
        self.show_meanings_link = "a[data=test-show-meanings-link]"
        self.meanings_container = "div[data=test-meanings-values]"


class IndexTest(BaseSeleniumTestCase):
    page_object_class = IndexPageObject

    def test_show_meanings(self):
        password = 'test12345678'
        user = User.objects.create_user(
            username='test_username',
            email='{}@debugmail.io'.format('test_username'),
            password=password
        )
        self.force_login(user)
        link = self.find_element(self.page_object.show_meanings_link)
        link.click()
        meanings_container = self.find_element(self.page_object.meanings_container)
        assert meanings_container.visible

    def test_show_main_page(self):
        password = 'test12345678'
        user = User.objects.create_user(
            username='test_username',
            email='{}@debugmail.io'.format('test_username'),
            password=password
        )
        self.force_login(user)
        self.browser.screenshot()
        # Запустить xvfb, отрисовать главную стрницу с помощью self.browser и сделать скриншот
        # https://stackoverflow.com/questions/6183276/how-do-i-run-selenium-in-xvfb
