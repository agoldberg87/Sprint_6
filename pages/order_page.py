from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random

class OrderPage:
    
    order_button_top = [By.XPATH, './/button[@class="Button_Button__ra12g" and text()="Заказать"]'] # Кнопка "Заказать" верх
    order_button_button = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]'] # Кнопка "Заказать" низ
    forward_button = [By.XPATH, './/button[text()="Далее"]'] # Кнопка "Далее"
    confirmation_button = [By.XPATH, './/button[text()="Да"]'] # Кнопка "Да"
    confirmation_header = [By.XPATH, './/div[@class="Order_ModalHeader__3FDaJ" and text()="Заказ оформлен"]']
    cookie_consent_banner = [By.CLASS_NAME, 'App_CookieConsent__1yUIN'] # Cookie consent banner

    field_first_name = [By.XPATH, './/input[@placeholder="* Имя"]']
    field_last_name = [By.XPATH, './/input[@placeholder="* Фамилия"]']
    field_delivery_address = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
    dropdown_subway_station = [By.CLASS_NAME, 'select-search']

    field_subway_station_option = [By.XPATH, './/li[@class="select-search__row"]']
    
    field_phone_number = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']
    field_delivery_date = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
    field_delivery_date_month_backward = [By.XPATH, './/button[@class="react-datepicker__navigation react-datepicker__navigation--previous"]']
    field_delivery_date_month_forward = [By.XPATH, './/button[@class="react-datepicker__navigation react-datepicker__navigation--next"]']
    
    dropdown_delivery_period = [By.CLASS_NAME, 'Dropdown-root']
    field_delivery_period = [By.CLASS_NAME, 'Dropdown-option']
    field_color_checkbox = [By.CLASS_NAME, 'Checkbox_Label__3wxSf']
    field_comment = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]']

    view_status_button = [By.XPATH, './/button[text()="Посмотреть статус"]']

    scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']

    accordion_headings = (By.CSS_SELECTOR, '[id^="accordion__heading-"]')
    
    def get_accordion_heading(self, index):
        return [By.ID, 'accordion__heading-' + str(index)]
    
    def get_accordion_panel(self, index):
        return [By.ID, 'accordion__panel-' + str(index)]
    
    def __init__(self, driver):
        self.driver = driver
    
    def click_order_button(self):
        i = random.randint(1, 2)
        if i == 1:
            self.driver.find_element(*self.order_button_top).click()
        else:
            self.driver.find_element(*self.order_button_button).click()
    
    def click_order_button_bottom(self):
        self.driver.find_element(*self.order_button_button).click()

    def click_forward_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.forward_button)
        )
        self.driver.find_element(*self.forward_button).click()

    def click_confirmation_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.confirmation_button)
        )
        self.driver.find_element(*self.confirmation_button).click()

    def handle_cookie_banner(self):
        try:
            # Если баннер отображается, то клик
            self.driver.find_element(By.CLASS_NAME, 'App_CookieButton__3cvqF').click()

            # Убедиться, что баннер исчезает
            WebDriverWait(self.driver, 10).until(
                expected_conditions.invisibility_of_element_located(self.cookie_consent_banner)
            )
        except:
            # Если баннер не отображается, то продолжить
            pass

    def wait_for_load_order_form_first_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.field_first_name))

    def wait_for_load_order_form_second_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.field_delivery_date))

    def wait_for_confirmation_button(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(self.confirmation_button))

    def wait_for_load_confirmation_header(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.confirmation_header))

    def set_first_name(self, first_name):
        self.driver.find_element(*self.field_first_name).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(*self.field_last_name).send_keys(last_name)

    def set_delivery_address(self, delivery_address):
        self.driver.find_element(*self.field_delivery_address).send_keys(delivery_address)

    def set_subway_station(self):  
        self.driver.find_element(*self.dropdown_subway_station).click()
        self.driver.find_elements(*self.field_subway_station_option)[random.randint(1, len(self.driver.find_elements(*self.field_subway_station_option)))].click()


    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.field_phone_number).send_keys(phone_number)

    def set_delivery_date(self):
        self.driver.find_element(*self.field_delivery_date).click()
        i = random.randint(1, 2)
        if i == 1:
            for j in range(0, random.randint(1, 12)):
                self.driver.find_element(*self.field_delivery_date_month_forward).click()
        else:
            for j in range(0, random.randint(1, 12)):
                self.driver.find_element(*self.field_delivery_date_month_backward).click()
        
        week_number = random.randint(1, 5)
        day_number = random.randint(1, 7)
        delivery_date = [By.XPATH, f'.//div[@class="react-datepicker__week"][{week_number}]/div[contains(@class, "react-datepicker__day")][{day_number}]']
        self.driver.find_element(*delivery_date).click()
        

    def set_delivery_period(self):
        self.driver.find_element(*self.dropdown_delivery_period).click()
        self.driver.find_elements(*self.field_delivery_period)[random.randint(0, len(self.driver.find_elements(*self.field_delivery_period)) - 1)].click()

    def set_color(self):
        self.driver.find_elements(*self.field_color_checkbox)[random.randint(0, len(self.driver.find_elements(*self.field_color_checkbox)) - 1)].click()

    def set_comment(self, comment):
        self.driver.find_element(*self.field_comment).send_keys(comment)

    def click_view_status_button(self):
        self.driver.find_element(*self.view_status_button).click()

    def click_scooter_logo(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.scooter_logo)
        )
        self.driver.find_element(*self.scooter_logo).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/"))

    def click_yandex_logo(self):
        original_window = self.driver.current_window_handle
        
        self.driver.find_element(*self.yandex_logo).click()
        
        WebDriverWait(self.driver, 5).until(expected_conditions.number_of_windows_to_be(2))
        
        # Переход в новое окно
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains('dzen.ru'))

    def set_order_form_first_page(self, first_name, last_name, delivery_address, phone_number):
        self.wait_for_load_order_form_first_page()
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_delivery_address(delivery_address)
        self.set_subway_station()
        self.set_phone_number(phone_number)
        self.click_forward_button()
    
        
    def set_order_form_second_page(self, comment):
        self.wait_for_load_order_form_second_page()
        self.set_delivery_date()
        self.set_delivery_period()
        self.set_color()
        self.set_comment(comment)
        self.click_order_button_bottom()
        self.wait_for_confirmation_button()  
        self.click_confirmation_button()


