from selene.support.conditions import have


class CheckboxActions:

    @staticmethod
    def choose_checkbox_by_value(els: all, checkbox_name: str):
        els.element_by(have.text(f'{checkbox_name}')).click()
