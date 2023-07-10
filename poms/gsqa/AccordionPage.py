from selenium.webdriver.common.by import By
import contextlib
from selenium.webdriver.common.action_chains import ActionChains

from base.browser.wrapper import find_element, click_element, get_text


class AccordionPage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return find_element(self.driver, by, value)

    def click_element(self, by, value):
        click_element(self.driver, by, value)

    def get_text(self, by, value):
        return get_text(self.driver, by, value)

    @contextlib.contextmanager
    def switch_to_frame(self, frame_xpath):
        frame = self.find_element(By.XPATH, frame_xpath)
        self.driver.switch_to.frame(frame)
        yield
        self.driver.switch_to.default_content()

    def get_simple_accordion_text(self):
        return self.get_text(By.XPATH, '//*[@aria-labelledby="tab_item-0"]/div')

    def switch_to_simple_accordion_frame(self):
        with self.switch_to_frame('//*[contains(@data-src,"coll")]'):
            pass

    def get_text_in_frame(self):
        return self.get_text(By.ID, 'ui-id-2')

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def click_resize_accordion(self):
        self.click_element(By.ID, 'Re-Size\ Accordion')

    def switch_to_resize_accordion_frame(self):
        with self.switch_to_frame('//*[contains(@data-src,"fill")]'):
            pass

    def get_accordion_resizer_element(self):
        return self.find_element(By.ID, 'accordion-resizer')

    def resize_accordion(self, offset_x, offset_y):
        resize = self.find_element(By.CLASS_NAME, 'ui-resizable-se')
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(resize, offset_x, offset_y).perform()

    def get_resized_accordion_size(self):
        elem = self.find_element(By.ID, 'accordion-resizer')
        return [elem.size['width'], elem.size['height']]

    def click_toggle_icons(self):
        self.click_element(By.ID, 'Toggle Icons')

    def switch_to_toggle_icons_frame(self):
        with self.switch_to_frame('//*[contains(@data-src,"custom")]'):
            pass

    def get_toggle_icons_accordion_text(self):
        return self.get_text(By.XPATH, '//*[@aria-labelledby="tab_item-2"]/div')

    def get_accordion_icons_elements(self):
        return self.driver.find_elements(By.CLASS_NAME, 'ui-accordion-icons')

    def toggle_icons(self):
        self.click_element(By.ID, 'toggle')