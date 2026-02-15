import allure

from pages.order_page import OrderPage

class TestPraktikum:

    @allure.title('Проверка раскрывания FAQ')
    @allure.description('Проверяем, что все секции раздела FAQ раскрываются')
    def test_faq_section(self, driver):

        order_page = OrderPage(driver)

        order_page.load_page(order_page.current_url)

        order_page.handle_cookie_banner()
        
        # Узнаем количество раскрывающихся заголовков
        accordion_headings = order_page.find_elements(order_page.accordion_headings)
        
        for i in range(len(accordion_headings)):
            
            order_page.click_accordion_heading(i)
            
            assert order_page.find_element(order_page.get_accordion_panel(i)).is_displayed()
