import pytest
import random
import allure

from pages.order_page import OrderPage

class TestPraktikum:


    @pytest.mark.parametrize(
        "first_name, last_name, delivery_address, phone_number, comment",
        [
            pytest.param("Тест", "Тест", "Тест 123", f"+7{random.randint(9000000000, 9999999999)}", "",  id="test_data_set_1"),
            pytest.param("Тигран", "Худавердян", "ул. Льва Толстого, 16", f"+7{random.randint(9000000000, 9999999999)}", "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",  id="test_data_set_2"),
        ],
    )
    
    @allure.title('Проверка заполнения формы заказа')
    @allure.description('Заполням форму заказа, проверяем, что заказ отправлен. Проверяем клики по лого сервиса и Яндекса.')
    def test_order_form(self, driver, first_name, last_name, delivery_address, phone_number, comment):

        order_page = OrderPage(driver)

        order_page.load_page(order_page.current_url)

        order_page.handle_cookie_banner()
        
        order_page.click_order_button()
        
        order_page.set_order_form_first_page(first_name, last_name, delivery_address, phone_number)
        order_page.set_order_form_second_page(comment)

        assert "Заказ оформлен" in order_page.find_element(order_page.confirmation_header).text

        order_page.click_view_status_button()
        
        order_page.click_scooter_logo()
        assert driver.current_url == order_page.current_url, f"Ожидаемый URL '{order_page.current_url}', но фактический - '{driver.current_url}'"

        original_window = order_page.get_current_window_handle()
        order_page.click_yandex_logo()
        
        assert order_page.yandex_url in driver.current_url, f"Ожидаемый URL должен включать '{order_page.yandex_url}', но фактически - '{driver.current_url}'"
        assert len(order_page.get_window_handles()) == 2, f"Ожидается 2 окна, но фактически - {len(order_page.get_window_handles())}"
        
        order_page.close_current_window()
        order_page.switch_to_window(original_window)
