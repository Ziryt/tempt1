

def test_multiple_selection(select_page):
    with select_page.ms_iframe.switch_to_frame():
        select_page.select_from_to(1, 3)
        assert len(select_page.selected_list.elements) == 3
        select_page.deselect_all()
        assert not select_page.selected_list.elements
        select_page.chane_non_adjacent(2, 7)
        assert len(select_page.selected_list.elements) == 2


def test_confirmation_selection(select_page):
    pass


def test_serialize(select_page):
    pass
