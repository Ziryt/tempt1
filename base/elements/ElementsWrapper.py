from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from base.browser.Wrapper import Browser
from base.elements.ElementWrapper import BaseElement, Container


class BaseElementList:

    of = BaseElement

    def __init__(self, locator, by=By.XPATH):
        self.by = by
        self.locator = locator

    @property
    def _finds(self) -> list[WebElement]:
        return Browser.get_driver().find_elements(self.by, self.locator)

    @property
    def elements(self) -> list[any]:
        self._elements = []
        for index, element in enumerate(self._finds):
            modified = self.of(self.locator, self.by, index)
            self._elements.append(modified)
        return self._elements

    @property
    def are_displayed(self) -> bool:
        return all(element.is_displayed() for element in self.elements)


class Containers(BaseElementList):

    of = Container

    def select_area(self, start, end) -> None:
        (ActionChains(Browser.get_driver())
         .drag_and_drop(self.elements[start].element, self.elements[end].element)
         .perform())
