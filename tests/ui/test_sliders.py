

def test_color_picker(slider_page):
    with slider_page.cp_iframe.switch_to_frame():
        assert '255, 140, 60' in slider_page.cp_iframe_color.attribute('style')
        slider_page.set_picker_color(-200, -20, 37)
        assert '55, 120, 97' in slider_page.cp_iframe_color.attribute('style')


def test_range_collapse(slider_page):
    slider_page.r_button.click()
    with slider_page.r_iframe.switch_to_frame():
        slider_page.set_range_relative(71, -200)
        assert slider_page.r_iframe_left.attribute('style') == \
            slider_page.r_iframe_right.attribute('style')
        assert '29.2' in slider_page.r_iframe_right.attribute('style')


def test_range_absolute(slider_page):
    slider_page.r_button.click()
    with slider_page.r_iframe.switch_to_frame():
        slider_page.set_range_absolute(39, 77)
        assert '39%' in slider_page.r_iframe_left.attribute('style')
        assert '77%' in slider_page.r_iframe_right.attribute('style')


def test_steps(slider_page):
    pass
