

def test_simple_accordion_text(accordion_page):
    p1 = 'Select different accordions and see all its contents.'
    accordion_page.driver.get('https://www.globalsqa.com/demo-site/accordion-and-tabs/')
    assert accordion_page.get_simple_accordion_text() == p1


def test_resizable_accordion(accordion_page):
    p2 = 'Some other text'
    accordion_page.driver.get('https://www.globalsqa.com/demo-site/accordion-and-tabs/')
    accordion_page.click_resize_accordion()
    with accordion_page.switch_to_resize_accordion_frame() as page:
        assert page.get_text_in_frame() == p2
        accordion_resizer = page.get_accordion_resizer_element()
        expected_size = [accordion_resizer.size['width'], accordion_resizer.size['height']]
        page.resize_accordion(200, 200)
        resized_size = page.get_resized_accordion_size()
        assert resized_size == expected_size


def test_toggle_icons_accordion(accordion_page):
    p3 = 'Toggle button present at the end of last accordion and verify icon against each accordion'
    accordion_page.driver.get('https://www.globalsqa.com/demo-site/accordion-and-tabs/')
    accordion_page.click_toggle_icons()
    with accordion_page.switch_to_toggle_icons_frame():
        assert accordion_page.get_toggle_icons_accordion_text() == p3
        accordion_icons = accordion_page.get_accordion_icons_elements()
        assert all(x.is_displayed() for x in accordion_icons)
        accordion_page.toggle_icons()
        assert not any(not x.is_displayed() for x in accordion_icons)

