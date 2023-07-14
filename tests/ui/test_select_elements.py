

def test_multiple_selection(select_page):
    with select_page.ms_iframe.switch_to_frame():
        select_page.select_from_to(2, 3)
        select_page.item_list.deselect_all()


def test_confirmation_selection(select_page):
    pass


def test_serialize(select_page):
    pass
