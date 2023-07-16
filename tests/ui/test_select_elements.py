

def test_multiple_selection(select_page):
    with select_page.ms_iframe.switch_to_frame():
        select_page.select_from_to(1, 3)
        assert len(select_page.selected_list.elements) == 3
        select_page.deselect_all()
        assert not select_page.selected_list.elements
        select_page.chane(2, 7)
        assert len(select_page.selected_list.elements) == 2


def test_grid_selection(select_page):
    values = [1, 2, 3, 4, 6, 8]
    select_page.gs_button.click()
    with select_page.gs_iframe.switch_to_frame():
        select_page.select_from_to(6, 11)
        assert len(select_page.selected_list.elements) == 4
        select_page.deselect_all()
        select_page.chane(*values)
        assert values == [int(i.text) for i in select_page.selected_list.elements]


def test_serialize(select_page):
    pass
