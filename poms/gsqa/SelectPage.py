from selenium.webdriver.common.by import By

from base.elements.ElementWrapper import Button, Text, Frame, Dropdown, ElementList


class SelectPage:

    """
    Multiple selection
    """
    ms_button = Button(locator='Multiple Selection', by=By.ID)
    ms_text = Text(locator='//*[@aria-labelledby="tab_item-0"]/div')
    ms_iframe = Frame(locator='//*[contains(@data-src,"default")]')
    item_list = ElementList(locator='//*[contains(@class,"ui-selectee")]')


    """
    Grid selection
    """
    gs_button = Button(locator='Grid Selection', by=By.ID)
    gs_text = Text(locator='//*[@aria-labelledby="tab_item-1"]/div')
    gs_iframe = Frame(locator='//*[contains(@data-src,"grid")]')

    """
    Serialize
    """
    s_button = Button(locator='Serialize', by=By.ID)
    s_text = Text(locator='//*[@aria-labelledby="tab_item-2"]/div')
    s_iframe = Frame(locator='//*[contains(@data-src,"serialize")]')

    def select_from_to(self, _from, _to):
        self.item_list.selection(self.item_list.elements[_from-1], self.item_list.elements[_to-1])

    def deselect(self, *args):
        pass