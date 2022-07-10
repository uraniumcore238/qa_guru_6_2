from selene.core import command
from selene.core.entity import Element
from selene.support.conditions import have
# from selene.support.shared.jquery_style import ss, s


class FeelValue:

    @staticmethod
    def type_data_in_input_field(el: Element, text: str):
        el.perform(command.js.scroll_into_view).type(text).press_tab()

    @staticmethod
    def choose_data_in_selector(container: Element, els: all, text: str):
        container.perform(command.js.scroll_into_view).click()
        els.element_by(have.text(f'{text}')).click()
