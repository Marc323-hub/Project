Class Services:
    def __init__(self, service_name, service_price):
        self.__service_name = service_name
        self.__service_price = service_price
       

    @property
    def service_name(self):
        return self.__service_name

    @property
    def service_price(self):
        return self.__service_price
