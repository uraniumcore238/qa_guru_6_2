from pathlib import Path

from selene.core.entity import Element

import tests


class FileActions:

    @staticmethod
    def attach_file(self, el: Element, file_path):
        file: str = Path(tests.__file__).parent.parent.joinpath(file_path)
        el.type(file)
