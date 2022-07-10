from selene.core.entity import Element
from selene.support.conditions import have


class TableChecking:

    @staticmethod
    def asserts_exact_text(el: Element, text: str):
        el.should(have.exact_text(text))

    @staticmethod
    def asserts_texts_in_rows(els: all, expeted_text):
        for el in els:
            row_text = el.text
            assert row_text in expeted_text, f'Actual text{row_text} but expected is {expeted_text}'
