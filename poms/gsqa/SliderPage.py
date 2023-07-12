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

    """
    Simple Accordion
    """
    s_button = Button(locator='Steps', by=By.ID)
    s_text = Text(locator='//*[@aria-labelledby="tab_item-2"]/div')
    s_iframe = Frame(locator='//*[contains(@data-src,"step")]')

    def set_picker_color(self, red, green, blue):
        coefficient = 302 / 255
        self.cp_iframe_red.dragndrop(red * coefficient, 0)
        self.cp_iframe_green.dragndrop(green * coefficient, 0)
        self.cp_iframe_blue.dragndrop(blue * coefficient, 0)
