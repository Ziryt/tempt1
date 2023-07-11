

def test_simple_accordion_text(accordion_page):
    section = 'Mauris mauris ante, blandit et, ultrices a'
    p1 = 'Select different accordions and see all its contents.'
    assert accordion_page.sa_text.text == p1
    with accordion_page.sa_iframe.switch_to_frame():
        assert accordion_page.sa_iframe_s1_text.text.startswith(section)


def test_resizable_accordion(accordion_page):
    p2 = 'Some other text'
    accordion_page.rsa_button.click()
    # assert accordion_page.rsa_text.text == p2
    with accordion_page.rsa_iframe.switch_to_frame(): 
        subject = accordion_page.rsa_iframe_container 
        expected_size = [subject.size['width'] + 200, subject.size['height'] + 200]
        accordion_page.rsa_iframe_resizer.resize(200, 200)
        resized_size = [subject.size['width'], subject.size['height']]
        assert expected_size == resized_size


# def test_toggle_icons_accordion(accordion_page):
#     p3 = 'Toggle button present at the end of last accordion and verify icon against each accordion'
#     accordion_page.ti_button.click()
#     assert accordion_page.ti_text.text == p3
#     with accordion_page.ti_iframe.switch_to_frame():
#         assert all(x.is_displayed() for x in accordion_page.ti_icons_list)
#         accordion_page.toggle_icons()
#         assert not any(not x.is_displayed() for x in accordion_page.ti_icons_list)
#
