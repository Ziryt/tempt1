from selenium import webdriver
import threading

from selenium.webdriver.remote.webdriver import WebDriver

from base.browser.DriverWrapper import DriverWrapper


class DriverManager:

    __Driver_dict = {}

    @staticmethod
    def create_instance() -> WebDriver:
        def driver_type():
            driver = webdriver.Chrome()
            driver.implicitly_wait(10)
            return driver
        DriverManager.__map(threading.current_thread(), driver_type())
        return DriverManager.get_driver()

    @staticmethod
    def get_driver() -> WebDriver:
        if threading.current_thread() in DriverManager.__Driver_dict.keys():
            return DriverManager.__Driver_dict[threading.current_thread()]
        return DriverManager.create_instance()

    @staticmethod
    def remove_driver() -> DriverWrapper:
        if threading.current_thread() in DriverManager.__Driver_dict.keys():
            del DriverManager.__Driver_dict[threading.current_thread()]

    @staticmethod
    def __map(thread, driver) -> None:
        DriverManager.__Driver_dict[thread] = driver
