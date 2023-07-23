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
    ib_first = Container(locator='//*[contains(text(),"Vienna, Austria")]')
    ib_second = Container(locator='//*[contains(text(),"London, England")]')
    ib_third = Container(locator='//*[contains(text(),"CC BY-SA 3.0")]')
    ib_tooltip = Container(locator='//*[@class="ui-tooltip-content"]/img')

    """
    Simple Accordion
    """
    vb_button = Button(locator='Video Based', by=By.ID)
    vb_text = Text(locator='//*[@aria-labelledby="tab_item-1"]/div')
    vb_iframe = Frame(locator='//*[contains(@data-src,"video")]')
    vb_like = Button(locator='//*[@data-icon="ui-icon-circle-arrow-n"]')
    vb_dislike = Button(locator='//*[@data-icon="ui-icon-circle-arrow-s"]')
    vb_watch_later = Button(locator='//*[@data-icon="ui-icon-circle-plus"]')
    vb_play_list = Button(locator='//*[@data-icon="ui-icon-triangle-1-s"]')
    vb_share = Button(locator='//*[@class="tools"]/button[1]')
    vb_report = Button(locator='//*[@data-icon="ui-icon-alert"]')
    vb_tooltip = Container(locator='//*[@class="ui-tooltip-content"]')

    """
    Simple Accordion
    """
    fb_button = Button(locator='Forms Based', by=By.ID)
    fb_text = Text(locator='//*[@aria-labelledby="tab_item-2"]/div')
    fb_iframe = Frame(locator='//*[contains(@data-src,"form")]')


