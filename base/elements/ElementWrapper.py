import contextlib
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.common import NoSuchElementException, TimeoutException
from base.browser.Wrapper import Browser


class BaseElement:
    def __init__(self,  locator, by=By.XPATH):
        self.by = by
        self.locator = locator

    def wait_until_present(self, timeout=10):
        try:
            WebDriverWait(Browser.get_driver(), timeout).until(
                EC.presence_of_element_located((self.by, self.locator))
            )
        except TimeoutException as e:
            print(e)

    @property
    def element(self):
        self.wait_until_present()
        return Browser.get_driver().find_element(self.by, self.locator)

    def click(self):
        self.element.click()

    def is_displayed(self):
        try:
            element = WebDriverWait(Browser.get_driver(), 10).until(
                EC.visibility_of_element_located((self.by, self.locator))
            )
            return element.is_displayed()
        except:
            return False

    @property
    def text(self):
        return self.element.text


class Text(BaseElement):
    pass


class TextInput(BaseElement):
    def clear(self):
        (ActionChains(Browser.get_driver())
         .key_down(Keys.CONTROL)
            .send_keys('a')
         .key_up(Keys.CONTROL)
         .send_keys(Keys.BACK_SPACE)
         .perform())
        return self
    
    def enter_text(self, text):
        self.element.clear().send_keys(text)
        return self

    @property
    def value(self):
        return self.element.get_attribute('value')


class Button(BaseElement):
    pass


class Dropdown(BaseElement):
    def select_option_by_visible_text(self, text):
        try:
            Select(self.element).select_by_visible_text(text)
        except NoSuchElementException:
            raise Exception(f'Option "{text}" was not found in dropdown')

    def select_option_by_value(self, value):
        try:
            Select(self.element).select_by_value(value)
        except NoSuchElementException:
            raise Exception(f'Option "{value}" was not found in dropdown')

    def select_option_by_index(self, index):
        try:
            Select(self.element).select_by_index(index)
        except NoSuchElementException:
            raise Exception(f'Option at index "{index}" was not found in dropdown')

    def select_options_by_visible_text(self, texts):
        for text in texts:
            self.select_option_by_visible_text(text)

    def select_options_by_value(self, values):
        for value in values:
            self.select_option_by_value(value)

    def select_options_by_index(self, indices):
        for index in indices:
            self.select_option_by_index(index)


class Frame(BaseElement):
    @contextlib.contextmanager
    def switch_to_frame(self):
        Browser.get_driver().switch_to.frame(self.element)
        yield
        Browser.get_driver().switch_to.default_content()


class Container(BaseElement):
    @property
    def size(self):
        return self.element.size
    
    def resize(self, x, y):
        ActionChains(Browser.get_driver())\
            .drag_and_drop_by_offset(self.element, x, y)\
            .perform()
            
            
class ElementList:
    def __init__(self, locator, by=By.XPATH):
        self.by = by
        self.locator = locator

    @property
    def elements(self):
        return Browser.get_driver().find_elements(self.by, self.locator)

    @property
    def are_displayed(self):
        return all(element.is_displayed() for element in self.elements)
