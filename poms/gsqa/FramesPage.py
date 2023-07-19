from selenium.webdriver.common.by import By

from base.elements.elementWrapper import Button, Text, Frame
from poms.BasePage import BasePage


class FramesPage(BasePage):

    """
    Simple Accordion
    """
    ont_button = Button(locator='Open New Tab', by=By.ID)
    ont_text = Text(locator='//*[@aria-labelledby="tab_item-0"]/div')

    """
    Simple Accordion
    """
    onw_button = Button(locator='Open New Window', by=By.ID)
    onw_text = Text(locator='//*[@aria-labelledby="tab_item-1"]/div')

    """
    Simple Accordion
    """
    f_button = Button(locator='iFrame', by=By.ID)
    f_text = Text(locator='//*[@aria-labelledby="tab_item-2"]/div')
    f_iframe = Frame(locator='//*[contains(@data-src,"trainings")]')

    new_button = Button(locator='//*[contains(@class,"resp-tab-content-active")]/a')
