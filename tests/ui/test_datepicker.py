

def test_simple_date_picker(date_picker_page):
    with date_picker_page.sdp_iframe.switch_to_frame():
        assert date_picker_page.set_date('4/8/2023') == date_picker_page.date_set
        assert date_picker_page.set_date('21/12/2021') == date_picker_page.date_set


def test_date_picker_dropdown(date_picker_page):
    date_picker_page.ddp_button.click()
    with date_picker_page.ddp_iframe.switch_to_frame():
        assert date_picker_page.set_date_dropdown('13/1/2024') == date_picker_page.date_set
        assert date_picker_page.set_date_dropdown('9/5/2022') == date_picker_page.date_set
