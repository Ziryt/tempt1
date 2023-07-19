from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from base.elements.elementWrapper import Button, Text, Frame
from base.elements.elementsWrapper import Containers
from poms.BasePage import BasePage


class SelectPage(BasePage):

    """
    Multiple selection
    """
    ms_button = Button(locator='Multiple Selection', by=By.ID)
    ms_text = Text(locator='//*[@aria-labelledby="tab_item-0"]/div')
    ms_iframe = Frame(locator='//*[contains(@data-src,"default")]')

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
    select_text = Text(locator='//*[@id="feedback"]/span')
    select_values = Text(locator='//*[@id="select-result"]')

    """
    Lists
    """
    items_list = Containers(locator='//*[contains(@class,"ui-selectee")]')
    selected_list = Containers(locator='//*[contains(@class,"ui-selected")]')

    def select_from_to(self, _from, _to) -> None:
        self.items_list.select_area(_from - 1, _to - 1)

    def chane(self, *args) -> None:
        if args:
            for num in args:
                self.items_list.elements[num - 1].click_with_key(Keys.CONTROL)
        else:
            for element in self.items_list.elements:
                element.click_with_key(Keys.CONTROL)

    def deselect_all(self):
        self.items_list.elements[0].click().click_with_key(Keys.CONTROL)
