from selenium import webdriver
import threading


class Browser:
    
    __Driver_dict = {}

    @staticmethod
    def create_instance():
        def driver_type():
            driver = webdriver.Chrome()
            driver.implicitly_wait(10)
            return driver
        Browser.__map(threading.current_thread(), driver_type())
        return Browser.get_driver()

    @staticmethod
    def get_driver():
        return Browser.__Driver_dict[threading.current_thread()]

    @staticmethod
    def __map(thread, driver):
        Browser.__Driver_dict[thread] = driver

    @staticmethod
    def quit():
        Browser.get_driver().quit()
    
    
