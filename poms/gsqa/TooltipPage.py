from selenium.webdriver.common.by import By

from base.elements.elementWrapper import Button, Text, Frame, Container
from poms.BasePage import BasePage


class TooltipPage(BasePage):

    """
    Simple Accordion
    """
    ib_button = Button(locator='Image Based', by=By.ID)
    ib_text = Text(locator='//*[@aria-labelledby="tab_item-0"]/div')
    ib_iframe = Frame(locator='//*[contains(@data-src,"custom")]')
    first = Container(locator='//*[contains(text(),"Vienna, Austria")]')
    second = Container(locator='//*[contains(text(),"London, England")]')
    third = Container(locator='//*[contains(text(),"CC BY-SA 3.0")]')
    tooltip = Container(locator='//*[@class="ui-tooltip-content"]/img')

    """
    Simple Accordion
    """
    vb_button = Button(locator='Video Based', by=By.ID)
    vb_text = Text(locator='//*[@aria-labelledby="tab_item-1"]/div')
    vb_iframe = Frame(locator='//*[contains(@data-src,"video")]')

    """
    Simple Accordion
    """
    fb_button = Button(locator='Forms Based', by=By.ID)
    fb_text = Text(locator='//*[@aria-labelledby="tab_item-2"]/div')
    fb_iframe = Frame(locator='//*[contains(@data-src,"form")]')
