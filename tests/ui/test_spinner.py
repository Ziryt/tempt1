

def test_currency_scroll(spinner_page):
    with spinner_page.c_iframe.switch_to_frame():
        assert spinner_page.selected_value == '$5.00'
        spinner_page.wheel_up(2)
        assert spinner_page.selected_value == '$55.00'
        spinner_page.wheel_down(1)
        assert spinner_page.selected_value == '$30.00'
        spinner_page.currency.select_option_by_index(1)
        assert spinner_page.selected_value == '30,00 €'


def test_spinner_widget(spinner_page):
    spinner_page.ss_button.click()

    with spinner_page.ss_iframe.switch_to_frame():
        assert spinner_page.up.exists and spinner_page.down.exists
        spinner_page.toggle_widget.click()
        assert not spinner_page.up.exists and not spinner_page.down.exists


def test_spinner_state(spinner_page):
    spinner_page.ss_button.click()

    with spinner_page.ss_iframe.switch_to_frame():
        assert spinner_page.up.is_clickable() and spinner_page.down.is_clickable()
        spinner_page.toggle_state.click()
        assert not spinner_page.up.is_clebickable() and not spinner_page.down.is_clickable()


def test_spinner_set_value(spinner_page):
    spinner_page.ss_button.click()

    with spinner_page.ss_iframe.switch_to_frame():
        spinner_page.up.click(23)
        assert spinner_page.selected_value == '23'
        spinner_page.default.click()
        assert spinner_page.selected_value == '5'


def test_spinner_get_value(spinner_page):
    spinner_page.ss_button.click()

    with spinner_page.ss_iframe.switch_to_frame():
        spinner_page.down.click(41)
        assert spinner_page.selected_value == '-41'
        spinner_page.get_value.click()

        with spinner_page.alert_box() as alert:
            assert alert.text == '-41'
            alert.accept()
