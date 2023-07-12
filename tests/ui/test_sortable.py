

def test_portlets(slider_page):
    assert driver.find_element(By.XPATH, '//*[contains(@style,"255, 140, 60")]')
    red = driver.find_element(By.XPATH, '//*[@id="red"]/span')
    action.drag_and_drop_by_offset(red, -200, 0).perform()
    green = driver.find_element(By.XPATH, '//*[@id="green"]/span')
    action.drag_and_drop_by_offset(green, -20, 0).perform()
    blue = driver.find_element(By.XPATH, '//*[@id="blue"]/span')
    action.drag_and_drop_by_offset(blue, 37, 0).perform()
    assert driver.find_element(By.XPATH, '//*[contains(@style,"55, 120, 97")]')


def test_multiple_list(slider_page):
    pass


def test_simple_list(slider_page):
    pass


def test_grid_sorting(slider_page):
    pass
