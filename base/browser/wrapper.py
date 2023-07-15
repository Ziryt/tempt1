from selenium import webdriver
import threading

from selenium.webdriver.chrome.webdriver import WebDriver


class Browser:

    __Driver_dict = {}

    @staticmethod
    def create_instance() -> WebDriver:
        def driver_type():
            driver = webdriver.Chrome()
            driver.implicitly_wait(10)
            return driver
        Browser.__map(threading.current_thread(), driver_type())
        return Browser.get_driver()

    @staticmethod
    def get_driver() -> WebDriver:
        return Browser.__Driver_dict[threading.current_thread()]

    @staticmethod
    def __map(thread, driver) -> None:
        Browser.__Driver_dict[thread] = driver

    @staticmethod
    def quit() -> None:
        Browser.get_driver().quit()

    @staticmethod
    def visit(target) -> None:
        Browser.get_driver().get(target)

    @staticmethod
    def set_wait(wait) -> None:
        Browser.get_driver().implicitly_wait(wait)

    @staticmethod
    def refresh() -> None:
        Browser.get_driver().refresh()

    @staticmethod
    def maximize_window() -> None:
        Browser.get_driver().maximize_window()

    @staticmethod
    def set_position(x, y) -> None:
        Browser.get_driver().set_window_position(x, y)
