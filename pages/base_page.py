from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
    
    def find_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located(locator)
        )
        
    
    def find_elements(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_all_elements_located(locator)
        )
    
    def click_element(self, locator, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )
        element.click()
    
    def fill_field(self, locator, text, timeout=5):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
    
    def wait_for_element_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )
    
    def wait_for_element_invisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.invisibility_of_element_located(locator)
        )
    
    def wait_for_url_to_be(self, url, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_to_be(url)
        )
    
    def wait_for_url_contains(self, text, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.url_contains(text)
        )
    
    def wait_for_number_of_windows(self, number, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.number_of_windows_to_be(number)
        )
    
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)
    
    def get_current_window_handle(self):
        return self.driver.current_window_handle
    
    def get_window_handles(self):
        return self.driver.window_handles
    
    def close_current_window(self):
        self.driver.close()
    
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)
    
    def load_page(self, url):
        self.driver.get(url)