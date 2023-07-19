import calendar
from datetime import datetime

from selenium.webdriver.common.by import By
from base.elements.elementWrapper import Button, Text, Frame, Container, Dropdown
from base.elements.elementsWrapper import Containers
from poms.BasePage import BasePage


class DatePickerPage(BasePage):
    """
    Simple Accordion
    """
    sdp_button = Button(locator='Simple Date Picker', by=By.ID)
    sdp_text = Text(locator='//*[@aria-labelledby="tab_item-0"]/div')
    sdp_iframe = Frame(locator='//*[contains(@data-src,"default")]')

    """
    Simple Accordion
    """
    ddp_button = Button(locator='DropDown DatePicker', by=By.ID)
    ddp_text = Text(locator='//*[@aria-labelledby="tab_item-1"]/div')
    ddp_iframe = Frame(locator='//*[contains(@data-src,"dropdown")]')

    """
    Simple Accordion
    """
    icdp_button = Button(locator='Icon Trigger', by=By.ID)
    icdp_text = Text(locator='//*[@aria-labelledby="tab_item-2"]/div')
    icdp_iframe = Frame(locator='//*[contains(@data-src,"icon")]')

    prev = Button(locator='//*[@data-handler="prev"]')
    next = Button(locator='//*[@data-handler="next"]')
    date_month = Dropdown(locator='//*[@class="ui-datepicker-month"]')
    date_year = Dropdown(locator='//*[@class="ui-datepicker-year"]')
    date_day = Containers(locator='//*[@data-handler="selectDay"]')
    date_field = Container(locator='//*[@id="datepicker"]')

    script = "var inputElement = document.querySelector('input[type=\"text\"]');" \
             "return inputElement.value.trim();"

    @property
    def date_set(self):
        return self.date_field.execute_js(self.script)

    def set_date(self, raw):
        date = datetime.strptime(raw, '%d/%m/%Y')
        self.date_field.click()
        self.date_month.is_displayed()
        diff = (int(self.date_year.text) - date.year) * 12 + \
            list(calendar.month_name).index(self.date_month.text) - date.month
        if diff < 0:
            for _ in range(abs(diff)):
                self.next.click()
        elif diff > 0:
            for _ in range(diff):
                self.prev.click()
        self.date_day.elements[date.day - 1].click()
        return date.strftime('%m/%d/%Y')

    def set_date_dropdown(self, raw):
        date = datetime.strptime(raw, '%d/%m/%Y')
        self.date_field.click()
        self.date_month.is_displayed()
        self.date_month.select_option_by_value(date.month - 1)
        self.date_year.select_option_by_value(date.year)
        self.date_day.elements[date.day - 1].click()
        return date.strftime('%m/%d/%Y')
