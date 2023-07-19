from selenium.webdriver.common.by import By

from base.elements.elementWrapper import Button, Text, Frame, Container, Dropdown, Alert
from poms.BasePage import BasePage


class SpinnerPage(BasePage):

    """
    Simple Accordion
    """
    c_button = Button(locator='Currency', by=By.ID)
    c_text = Text(locator='//*[@aria-labelledby="tab_item-0"]/div')
    c_iframe = Frame(locator='//*[contains(@data-src,"currency")]')

    """
    Simple Accordion
    """
    ss_button = Button(locator='Simple Spinner', by=By.ID)
    ss_text = Text(locator='//*[@aria-labelledby="tab_item-1"]/div')
    ss_iframe = Frame(locator='//*[contains(@data-src,"default")]')

    field = Container(locator='//*[@id="spinner"]')
    currency = Dropdown(locator='//*[@id="currency"]')
    up = Button(locator='//*[contains(@class,"ui-spinner-up")]')
    down = Button(locator='//*[contains(@class,"ui-spinner-down")]')
    toggle_widget = Button(locator='//*[@id="destroy"]')
    toggle_state = Button(locator='//*[@id="disable"]')
    get_value = Button(locator='//*[@id="getvalue"]')
    default = Button(locator='//*[@id="setvalue"]')
    alert_box = Alert

    script = "var inputElement = document.querySelector('input[id=\"spinner\"]');" \
             "return inputElement.value.trim();"

    @property
    def selected_value(self):
        if self.field.exists:
            return self.field.execute_js(self.script)

    def wheel_up(self, times):
        for _ in range(times):
            self.field.scroll(-100)

    def wheel_down(self, times):
        for _ in range(times):
            self.field.scroll(100)
