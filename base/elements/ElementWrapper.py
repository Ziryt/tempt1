import contextlib

from selenium.webdriver.remote.webelement import WebElement
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

    @property
    def element(self) -> WebElement:
        try:
            self.wait_until_present()
            return Browser.get_driver().find_element(self.by, self.locator)
        except NoSuchElementException:
            raise Exception(f'Element at "{self.locator}" was not found')

    @property
    def text(self) -> str:
        self.wait_until_present()
        return self.element.text

    @property
    def size(self) -> dict:
        return self.element.size

    @property
    def location(self) -> dict:
        return self.element.location

    @property
    def invisibility(self):
        return EC.invisibility_of_element(self.element)

    def wait_until_present(self, timeout=10):
        try:
            WebDriverWait(Browser.get_driver(), timeout).until(
                EC.presence_of_element_located((self.by, self.locator))
            )
        except TimeoutException as e:
            raise Exception(f'Times went out during waiting of element:"{self.locator}" to be present')

    def is_displayed(self) -> bool:
        try:
            element = WebDriverWait(Browser.get_driver(), 10).until(
                EC.visibility_of_element_located((self.by, self.locator))
            )
            return element.is_displayed()
        except TimeoutException:
            return False

    def attribute(self, name) -> str:
        self.wait_until_present()
        return self.element.get_attribute(name)

    def click(self) -> None:
        self.element.click()

    def click_by_offset(self, x, y) -> None:
        ActionChains(Browser.get_driver()) \
            .move_to_element_with_offset(self.element, x, y) \
            .click() \
            .perform()

    @staticmethod
    def execute_js(script):
        return Browser.get_driver().execute_script(script)


class Text(BaseElement):
    pass


class Input(BaseElement):
    @property
    def value(self) -> str:
        self.wait_until_present()
        return self.element.get_attribute('value')


class TextInput(Input):
    def clear(self) -> WebElement:
        (ActionChains(Browser.get_driver())
         .key_down(Keys.CONTROL)
            .send_keys('a')
         .key_up(Keys.CONTROL)
         .send_keys(Keys.BACK_SPACE)
         .perform())
        return self.element
    
    def enter_text(self, text) -> WebElement:
        self.clear().send_keys(text)
        return self.element


class Button(BaseElement):
    pass


class Dropdown(BaseElement):
    @property
    def element(self) -> Select:
        return Select(super().element)

    @property
    def selected_value(self) -> str:
        return self.element.first_selected_option.text

    @property
    def selected_values(self) -> list[str]:
        return [value.text for value in self.element.all_selected_options]

    @property
    def options(self) -> list[WebElement]:
        return self.element.options

    def deselect_all(self) -> None:
        self.element.deselect_all()

    def select_option_by_visible_text(self, text) -> None:
        try:
            self.element.select_by_visible_text(text)
        except NoSuchElementException:
            raise Exception(f'Option "{text}" was not found in dropdown')

    def select_option_by_value(self, value) -> None:
        try:
            self.element.select_by_value(value)
        except NoSuchElementException:
            raise Exception(f'Option "{value}" was not found in dropdown')

    def select_option_by_index(self, index) -> None:
        try:
            self.element.select_by_index(index)
        except NoSuchElementException:
            raise Exception(f'Option at index "{index}" was not found in dropdown')

    def select_options_by_visible_text(self, texts) -> None:
        for text in texts:
            self.select_option_by_visible_text(text)

    def select_options_by_value(self, values) -> None:
        for value in values:
            self.select_option_by_value(value)

    def select_options_by_index(self, indices) -> None:
        for index in indices:
            self.select_option_by_index(index)


class Frame(BaseElement):
    @contextlib.contextmanager
    def switch_to_frame(self):
        Browser.get_driver().switch_to.frame(self.element)
        yield
        Browser.get_driver().switch_to.default_content()


class Container(BaseElement):
    def dragndrop(self, x, y) -> None:
        ActionChains(Browser.get_driver())\
            .drag_and_drop_by_offset(self.element, x, y) \
            .release() \
            .perform()


class ElementList:
    def __init__(self, locator, by=By.XPATH):
        self.by = by
        self.locator = locator

    @property
    def elements(self) -> list[WebElement]:
        return Browser.get_driver().find_elements(self.by, self.locator)

    @property
    def are_displayed(self) -> bool:
        return all(element.is_displayed() for element in self.elements)
