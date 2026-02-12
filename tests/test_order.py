import sys
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import random
import allure

# Add the parent directory to Python path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from pages.order_page import OrderPage

class TestPraktikum:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()


    @pytest.mark.parametrize(
        "first_name, last_name, delivery_address, phone_number, comment",
        [
            pytest.param("Тест", "Тест", "Тест 123", f"+7{random.randint(9000000000, 9999999999)}", "",  id="test_data_set_1"),
            pytest.param("Тигран", "Худавердян", "ул. Льва Толстого, 16", f"+7{random.randint(9000000000, 9999999999)}", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",  id="test_data_set_2"),
        ],
    )
    
    @allure.title('Проверка заполнения формы заказа')
    @allure.description('Заполням форму заказа, проверяем, что заказ отправлен. Проверяем клики по лого сервиса и Яндекса.')
    @allure.step("Заполнить форму заказа")
    def test_order_form(self, first_name, last_name, delivery_address, phone_number, comment):
        # перешли на страницу тестового приложения
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        # создали объект класса OrderPage
        order_page = OrderPage(self.driver)

        order_page.handle_cookie_banner()
        
        order_page.click_order_button()
        
        order_page.set_order_form_first_page(first_name, last_name, delivery_address, phone_number)
        order_page.set_order_form_second_page(comment)

        assert "Заказ оформлен" in self.driver.find_element(*order_page.confirmation_header).text

        order_page.click_view_status_button()
        
        order_page.click_scooter_logo()
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/"))
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/", f"Ожидаемый URL 'https://qa-scooter.praktikum-services.ru/', но фактический - '{self.driver.current_url}'"

        original_window = self.driver.current_window_handle
        order_page.click_yandex_logo()
        
        assert 'dzen.ru' in self.driver.current_url, f"Ожидаемый URL должен включать 'dzen.ru', но фактически - '{self.driver.current_url}'"
        assert len(self.driver.window_handles) == 2, f"Ожидается 2 окна, но фактически - {len(self.driver.window_handles)}"
        
        self.driver.close()
        self.driver.switch_to.window(original_window)

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()