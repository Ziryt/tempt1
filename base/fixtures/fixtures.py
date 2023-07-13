import pytest
from base.browser.Wrapper import Browser
from poms.gsqa.AlertBoxPage import AlertBoxPage
from poms.gsqa.AutocompletePage import AutocompletePage
from poms.gsqa.DatePickerPage import DatePickerPage
from poms.gsqa.DialogPage import DialogPage
from poms.gsqa.DragNDropPage import DragNDropPage
from poms.gsqa.DraggableBoxesPage import DraggableBoxesPage
from poms.gsqa.DropdownPage import DropdownPage
from poms.gsqa.FramesPage import FramesPage
from poms.gsqa.ProgressBarPage import ProgressBarPage
from poms.gsqa.SelectPage import SelectPage
from poms.gsqa.SliderPage import SliderPage
from poms.gsqa.SortablePage import SortablePage
from poms.gsqa.SpinnerPage import SpinnerPage
from poms.gsqa.TabsPage import TabsPage
from poms.gsqa.ToolbarPage import ToolbarPage
from poms.gsqa.TooltipPage import TooltipPage


@pytest.fixture
def driver():
    driver = Browser.create_instance()
    driver.set_window_position(-1000, 0)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def alert_box_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/alertbox/')
    return AlertBoxPage()


@pytest.fixture
def autocomplete_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/auto-complete/')
    return AutocompletePage()


@pytest.fixture
def date_picker_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/datepicker/')
    return DatePickerPage()


@pytest.fixture
def dialog_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/dialog-boxes/')
    return DialogPage()


@pytest.fixture
def drag_and_drop_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/draganddrop/')
    return DraggableBoxesPage()


@pytest.fixture
def draggable_boxes_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/draggableboxes/')
    return DragNDropPage()


@pytest.fixture
def dropdown_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/select-dropdown-menu/')
    return DropdownPage()


@pytest.fixture
def frames_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/frames-and-windows/')
    return FramesPage()


@pytest.fixture
def progress_bar_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/progress-bar/')
    return ProgressBarPage()


@pytest.fixture
def select_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/select-elements/')
    return SelectPage()


@pytest.fixture
def slider_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/sliders/')
    return SliderPage()


@pytest.fixture
def sortable_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/sorting/')
    return SortablePage()


@pytest.fixture
def spinner_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/spinner/')
    return SpinnerPage()


@pytest.fixture
def tabs_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/accordion-and-tabs/')
    return TabsPage()


@pytest.fixture
def toolbar_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/toolbar/')
    return ToolbarPage()


@pytest.fixture
def tooltips_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/tooltip/')
    return TooltipPage()

