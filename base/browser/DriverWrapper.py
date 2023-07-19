from selenium.webdriver.remote.webdriver import WebDriver


class DriverWrapper:
    def __init__(self, driver: WebDriver = None):
        self.driver: WebDriver = driver

    def quit(self) -> None:
        self.driver.quit()

    def visit(self, target) -> None:
        self.driver.get(target)

    def set_wait(self, wait) -> None:
        self.driver.implicitly_wait(wait)

    def refresh(self) -> None:
        self.driver.refresh()

    def maximize_window(self) -> None:
        self.driver.maximize_window()

    def set_position(self, x, y) -> None:
        self.driver.set_window_position(x, y)

    def switch_tab(self, tab) -> None:
        self.driver.switch_to.window(tab)
