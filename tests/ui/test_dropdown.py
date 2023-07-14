

def test_tip(dropdown_page):
    assert dropdown_page.text.text == 'Select country from below drop down list:'
    dropdown_page.close_button.click()
    assert dropdown_page.text.invisibility


def test_dropdown(dropdown_page):
    assert dropdown_page.dropdown.selected_value == 'Afghanistan'
    dropdown_page.dropdown.select_option_by_value('BRA')
    assert dropdown_page.dropdown.selected_value == 'Brazil'
    dropdown_page.dropdown.select_option_by_index(34)
    assert dropdown_page.dropdown.selected_value != 'Brazil'
    dropdown_page.dropdown.select_option_by_visible_text('Germany')
    assert dropdown_page.dropdown.selected_value == 'Germany'


