from src.item import Item


class MixinLang:

    lang = 'EN'

    def __init__(self):
        self.__language = self.lang

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        if self.__language == 'RU':
            self.__language = "EN"
            return self


class Keyboard(Item, MixinLang):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        