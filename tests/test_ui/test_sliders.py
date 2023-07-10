
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_slider(driver):
    action = ActionChains(driver)

    driver.set_window_position(-1000, 0)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.globalsqa.com/demo-site/sliders/')

    '''
    Color Picker
    '''
    assert driver.find_element(By.XPATH, '//*[contains(@style,"255, 140, 60")]')
    red = driver.find_element(By.XPATH, '//*[@id="red"]/span')
    action.drag_and_drop_by_offset(red, -200, 0).perform()
    green = driver.find_element(By.XPATH, '//*[@id="green"]/span')
    action.drag_and_drop_by_offset(green, -20, 0).perform()
    blue = driver.find_element(By.XPATH, '//*[@id="blue"]/span')
    action.drag_and_drop_by_offset(blue, 37, 0).perform()
    assert driver.find_element(By.XPATH, '//*[contains(@style,"55, 120, 97")]')

    '''
    Range
    '''

    '''
    Steps
    '''