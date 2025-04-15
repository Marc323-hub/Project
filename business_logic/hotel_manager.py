class Hotel:
    def __init__(self, name, address, stars):
        self.__name = name
        self.__address = address
        self.__stars = stars
        self.__rooms = []

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    @property
    def stars(self):
        return self.__stars
