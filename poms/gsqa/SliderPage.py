import re

from selenium.webdriver.common.by import By
from base.elements.ElementWrapper import Button, Text, Frame, Container


class SliderPage:

    """
    Simple Accordion
    """
    cp_button = Button(locator='Color Picker', by=By.ID)
    cp_text = Text(locator='//*[@aria-labelledby="tab_item-0"]/div')
    cp_iframe = Frame(locator='//*[contains(@data-src,"color")]')
    cp_iframe_color = Container(locator='//*[@class="ui-widget-content ui-corner-all"]')
    cp_iframe_red = Container(locator='//*[@id="red"]/span')
    cp_iframe_green = Container(locator='//*[@id="green"]/span')
    cp_iframe_blue = Container(locator='//*[@id="blue"]/span')

    """
    Simple Accordion
    """
    r_button = Button(locator='Range', by=By.ID)
    r_text = Text(locator='//*[@aria-labelledby="tab_item-1"]/div')
    r_iframe = Frame(locator='//*[contains(@data-src,"range")]')
    r_iframe_bar = Container(locator='//*[@id="slider-range"]')
    r_iframe_left = Container(locator='//*[@tabindex="0"][1]')
    r_iframe_right = Container(locator='//*[@tabindex="0"][2]')

    """
    Simple Accordion
    """
    s_button = Button(locator='Steps', by=By.ID)
    s_text = Text(locator='//*[@aria-labelledby="tab_item-2"]/div')
    s_iframe = Frame(locator='//*[contains(@data-src,"step")]')
    s_iframe_text = Text(locator='//*[@for="amount"]')
    s_iframe_value = Text(locator='//*[@class="vsc-initialized"]/p')
    s_iframe_bar = Container(locator='//*[@id="slider"]')

    def set_picker_color(self, red, green, blue) -> None:
        coeff = 302 / 255
        self.cp_iframe_red.dragndrop(red * coeff, 0)
        self.cp_iframe_green.dragndrop(green * coeff, 0)
        self.cp_iframe_blue.dragndrop(blue * coeff, 0)

    def set_range_relative(self, left, right) -> None:
        coeff = 684 / 500
        self.r_iframe_left.dragndrop(left * coeff, 0)
        self.r_iframe_right.dragndrop(right * coeff, 0)

    def set_range_absolute(self, left, right) -> None:
        """
        Sets handle position in % value of bar length,
        For example it can set left handle at 43% of bar length, and 79% for right

        :param left: % for left handle
        :param right: % for left handle
        """
        coeff = 6.84
        self.set_range_relative(-76, 201)
        self.r_iframe_left.dragndrop(left * coeff, 0)
        self.r_iframe_right.dragndrop((-100 + right) * coeff, 0)
        self._adjust_range(self.r_iframe_left, left)
        self._adjust_range(self.r_iframe_right, right)

    def add_step(self, x) -> None:
        self.s_iframe_bar.click_by_offset(x, 0)

    @staticmethod
    def _adjust_range(element, goal) -> None:
        while (current := float(re.search('[0-9]+.*[0-9]+', element.attribute('style')).group(0)))\
                != (f_goal := float(goal)):
            if current > f_goal:
                element.dragndrop(-2, 0)
            if current < f_goal:
                element.dragndrop(2, 0)
