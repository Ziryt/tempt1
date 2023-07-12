

def test_color_picker(slider_page):
    with slider_page.cp_iframe.switch_to_frame():
        assert "255, 140, 60" in slider_page.cp_iframe_color.attribute("style")
        slider_page.set_picker_color(-200, -20, 37)
        assert "55, 120, 97" in slider_page.cp_iframe_color.attribute("style")


def test_range(slider_page):
    pass


def test_steps(slider_page):
    pass
