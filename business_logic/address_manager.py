class Address:
    def __init__(self, street, city, country):
        self.__street = street
        self.__city = city
        self.__country = country

    @property
    def street(self):
        return self.__street

    @property
    def city(self):
        return self.__city

    @property
    def country(self):
        return self.__country
