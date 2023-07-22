import contextlib

from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.common import NoSuchElementException, TimeoutException, InvalidSelectorException
from base.browser.DriverManager import DriverManager as dm


class BaseElement:
    def __init__(self,  locator, by=By.XPATH, index=None):
        self.by = by
        self.locator = locator
        self.index = index

    @property
    def driver(self):
        self._dw = dm.get_wrapper()
        return self._dw.driver

    @property
    def element(self) -> WebElement:
        self._find()
        return self._element

    @property
    def text(self) -> str:
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

    @property
    def tag_name(self) -> str:
        self.wait_until_present()
        return self.element.tag_name

    @property
    def exists(self) -> bool:
        try:
            if self.driver.find_element(self.by, self.locator):
                return True
        except NoSuchElementException:
            return False

    def _find(self):
        if self.index:
            self._element = self.driver.find_elements(self.by, self.locator)[self.index]
        else:
            try:
                self.wait_until_present()
                self._element = self.driver.find_element(self.by, self.locator)
            except NoSuchElementException:
                raise Exception(f'Element at "{self.locator}" was not found')

    def wait_until_present(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((self.by, self.locator))
            )
        except TimeoutException:
            raise Exception(f'Time went out during waiting of element:"{self.locator}" to be present')
        except InvalidSelectorException:
            raise Exception(f'Xpath provided:"{self.locator}" is either invalid or doesn\'t return WebElement')

    def is_displayed(self) -> bool:
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((self.by, self.locator))
            )
            return element.is_displayed()
        except TimeoutException:
            return False

    def is_clickable(self) -> bool:
        if WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((self.by, self.locator))
        ):
            return True
        else:
            return False

    def is_enabled(self) -> bool:
        return self.element.is_enabled()

    def attribute(self, name: any) -> str:
        self.wait_until_present()
        return self.element.get_attribute(name)

    def click(self, times: int = 1):
        temp = self.driver.window_handles
        self.element.click()
        if len(handles := self.driver.window_handles) != temp:
            self.driver.switch_to.window(handles[-1])
        [self.element.click() for _ in range(times - 1)]
        return self

    def double_click(self):
        (ActionChains(self.driver)
            .move_to_element(self.element)
            .double_click()
            .perform())
        return self

    def hover(self):
        self.is_clickable()
        (ActionChains(self.driver)
            .move_to_element(self.element)
            .perform())

    def scroll(self, amount: int = 100):
        (ActionChains(self.driver)
            .scroll_from_origin(ScrollOrigin(self.element, 0, 0), 0, amount)
            .perform())
        return self

    def execute_js(self, script):
        self.wait_until_present()
        return self.driver.execute_script(script)


class Text(BaseElement):
    pass


class Input(BaseElement):
    @property
    def value(self) -> str:
        self.wait_until_present()
        return self.element.get_attribute('value')


class TextInput(Input):
    def clear(self) -> WebElement:
        (ActionChains(self.driver)
            .key_down(Keys.CONTROL)
            .send_keys('a')
            .key_up(Keys.CONTROL)
            .send_keys(Keys.BACK_SPACE)
            .perform())
        return self.element
    
    def enter_text(self, text: any) -> WebElement:
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

    def select_option_by_visible_text(self, text: str) -> None:
        try:
            self.element.select_by_visible_text(text)
        except NoSuchElementException:
            raise Exception(f'Option "{text}" was not found in dropdown')

    def select_option_by_value(self, value: str) -> None:
        try:
            self.element.select_by_value(value)
        except NoSuchElementException:
            raise Exception(f'Value "{value}" was not found in dropdown')

    def select_option_by_index(self, index: str) -> None:
        try:
            self.element.select_by_index(index)
        except NoSuchElementException:
            raise Exception(f'Index "{index}" was not found in dropdown')

    def select_options_by_visible_text(self, texts: list[str]) -> None:
        for text in texts:
            self.select_option_by_visible_text(text)

    def select_options_by_value(self, values: list[str]) -> None:
        for value in values:
            self.select_option_by_value(value)

    def select_options_by_index(self, indices: list[str]) -> None:
        for index in indices:
            self.select_option_by_index(index)


class Container(BaseElement):
    def drag_drop_by_offset(self, x: any, y: any) -> None:
        (ActionChains(self.driver)
            .drag_and_drop_by_offset(self.element, x, y)
            .perform())

    def click_by_offset(self, x: any, y: any) -> None:
        (ActionChains(self.driver)
            .move_to_element_with_offset(self.element, x, y)
            .click()
            .perform())
        return self

    def click_with_key(self, key: any):
        (ActionChains(self.driver)
            .move_to_element(self.element)
            .key_down(key)
            .click()
            .key_up(key)
            .perform())
        return self


class Frame(BaseElement):
    @contextlib.contextmanager
    def switch_to_frame(self):
        self.driver.switch_to.frame(self.element)
        yield
        self.driver.switch_to.default_content()


class Alert:
    def __init__(self):
        self.alert = self.driver.switch_to.alert

    def __enter__(self):
        return self.alert

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.switch_to.default_content()

    @property
    def driver(self):
        self._dw = dm.get_wrapper()
        return self._dw.driver

    @property
    def text(self):
        return self.alert.text

    def accept(self):
        self.alert.accept()

    def dismiss(self):
        self.alert.dismiss()

    def send_keys(self, text):
        self.alert.send_keys(text)
