from base.browser.DriverManager import DriverManager


class BasePage:
    def __init__(self):
        self.wrapper = DriverManager.get_wrapper()
        self.verify()

    def verify(self):
        pass
