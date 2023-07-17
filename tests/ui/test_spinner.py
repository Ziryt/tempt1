

def test_currency(spinner_page):
    with spinner_page.c_iframe.switch_to_frame():
        assert spinner_page.selected_value == '$5.00'
        spinner_page.wheel_up(2)
        assert spinner_page.selected_value == '$55.00'
        spinner_page.wheel_down(1)
        assert spinner_page.selected_value == '$30.00'
        spinner_page.currency.select_option_by_index(1)
        assert spinner_page.selected_value == '30,00 €'


def test_simple_spinner(spinner_page):
    pass

