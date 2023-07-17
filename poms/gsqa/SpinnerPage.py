from selenium.webdriver.common.by import By

from base.elements.ElementWrapper import Button, Text, Frame, Container, Dropdown


class SpinnerPage:

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
    toggle_widget = Button(locator='//*[contains(@class,"ui-spinner-down")]')
    toggle_state = Button(locator='//*[contains(@class,"ui-spinner-down")]')
    get_value = Button(locator='//*[contains(@class,"ui-spinner-down")]')
    default = Button(locator='//*[contains(@class,"ui-spinner-down")]')

    script = "var inputElement = document.querySelector('input[id=\"spinner\"]');" \
             "return inputElement.value.trim();"

    @property
    def selected_value(self):
        self.field.is_displayed()
        return self.field.execute_js(self.script)

    def wheel_up(self, times):
        for _ in range(times):
            self.field.scroll(-100)

    def wheel_down(self, times):
        for _ in range(times):
            self.field.scroll(100)

