

def test_new_tab(frames_page):
    page, driver = frames_page
    page.new_button.click()
    assert driver.current_window_handle != driver.window_handles[0]


def test_new_window(frames_page):
    page, driver = frames_page
    page.onw_button.click()
    page.new_button.click()
    assert driver.current_window_handle != driver.window_handles[0]

