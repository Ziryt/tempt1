

def test_image(tooltips_page):
    with tooltips_page.ib_iframe.switch_to_frame():
        tooltips_page.first.hover()
        assert tooltips_page.tooltip.attribute('alt') == tooltips_page.first.text
        tooltips_page.second.hover()
        assert tooltips_page.tooltip.attribute('alt') == tooltips_page.second.text
        tooltips_page.third.hover()
        assert tooltips_page.tooltip.attribute('alt') == tooltips_page.third.text


def test_video(tooltips_page):
    pass


def test_form(tooltips_page):
    pass
