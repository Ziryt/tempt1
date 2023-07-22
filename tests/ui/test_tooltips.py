

def test_image(tooltips_page):
    with tooltips_page.ib_iframe.switch_to_frame():
        tooltips_page.ib_first.hover()
        assert tooltips_page.ib_tooltip.attribute('alt') == tooltips_page.ib_first.text
        tooltips_page.ib_third.hover()
        tooltips_page.ib_second.hover()
        assert tooltips_page.ib_tooltip.attribute('alt') == tooltips_page.ib_second.text
        tooltips_page.ib_third.hover()
        assert tooltips_page.ib_tooltip.attribute('alt') == tooltips_page.ib_third.attribute('title')


def test_video(tooltips_page):
    tooltips_page.vb_button.click()
    with tooltips_page.vb_iframe.switch_to_frame():
        tooltips_page.vb_like.hover()
        assert tooltips_page.vb_tooltip.text == 'I like this'
        tooltips_page.vb_dislike.hover()
        assert tooltips_page.vb_tooltip.text == 'I dislike this'
        tooltips_page.vb_watch_later.hover()
        assert tooltips_page.vb_tooltip.text == 'Add to Watch Later'
        tooltips_page.vb_play_list.hover()
        assert tooltips_page.vb_tooltip.text == 'Add to favorites or playlist'
        tooltips_page.vb_share.hover()
        assert tooltips_page.vb_tooltip.text == 'Share this video'
        tooltips_page.vb_report.hover()
        assert tooltips_page.vb_tooltip.text == 'Flag as inappropriate'



def test_form(tooltips_page):
    pass
