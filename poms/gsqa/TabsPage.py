from selenium.webdriver.common.by import By
from base.elements.ElementWrapper import Button, Container, ElementList, Frame, Text


class TabsPage:

    """
    Simple Accordion
    """
    sa_button = Button(locator='Simple Accordion', by=By.ID)
    sa_text = Text(locator='//*[@aria-labelledby="tab_item-0"]/div')
    sa_iframe = Frame(locator='//*[contains(@data-src,"coll")]')
    sa_iframe_s1_text = Text(locator='ui-id-2', by=By.ID)

    """
    Re-size Accordion
    """
    rsa_button = Button(locator='Re-Size\ Accordion', by=By.ID)
    rsa_text = Text(locator='//*[@aria-labelledby="tab_item-1"]/div')
    rsa_iframe = Frame(locator='//*[contains(@data-src,"fill")]')
    rsa_iframe_container = Container(locator='accordion-resizer', by=By.ID)
    rsa_iframe_resizer = Container(locator='ui-resizable-se', by=By.CLASS_NAME)

    """
    Toggle Icons
    """
    ti_button = Button(locator='Toggle Icons', by=By.ID)
    ti_text = Text(locator='//*[@aria-labelledby="tab_item-2"]/div')
    ti_iframe = Frame(locator='//*[contains(@data-src,"custom")]')
    ti_icons_list = ElementList(locator='//*[contains(@class,"ui-accordion-header-icon")]')
    ti_icons_button = Button(locator='toggle', by=By.ID)
