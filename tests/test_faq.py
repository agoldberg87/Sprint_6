import sys
import os
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
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

    @allure.title('Проверка раскрывания FAQ')
    @allure.description('Проверяем, что все секции раздела FAQ раскрываются')
    @allure.step("По очереди раскрыть каждую секцию FAQ")
    def test_faq_section(self):
        # перешли на страницу тестового приложения
        self.driver.get('https://qa-scooter.praktikum-services.ru/')

        order_page = OrderPage(self.driver)

        order_page.handle_cookie_banner()
        
        # Get all accordion headings
        accordion_headings = self.driver.find_elements(*order_page.accordion_headings)
        
        for i in range(len(accordion_headings)):
            accordion_heading = order_page.get_accordion_heading(i)
            accordion_panel = order_page.get_accordion_panel(i)
            
            element = self.driver.find_element(*accordion_heading)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            
            WebDriverWait(self.driver, 5).until(
                expected_conditions.element_to_be_clickable(accordion_heading)
            )
            
            self.driver.execute_script("arguments[0].click();", element)
            
            # Wait for panel to be displayed
            WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located(accordion_panel)
            )
            
            assert self.driver.find_element(*accordion_panel).is_displayed()

    @classmethod
    def teardown_class(cls):
        # Закрой браузер
        cls.driver.quit()