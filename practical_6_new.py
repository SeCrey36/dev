class Main:
    def __init__(self):
        airplanes = []

    def add_airplane(self):
        pass

    def del_airplane(self):
        pass

    def plane_info(self):
        pass

    def booking(self):
        pass

    def del_book(self):
        pass


class Airplane:
    def __init__(self, name):
        self.name = name
        self.zones = []

    def plane_info(self):
        pass

    def reserve_seat(self):
        pass

    def del_reserve(self):
        pass


class Zone:
    def __init__(self, name, tariff, seats):
        self.name = name
        self.tariff = tariff
        self.seats = seats
        self.lock_seats = 0
        self.books = []

    def booking(self):
        pass

    def del_book(self):
        pass


class Booking:
    def __init__(self):
        reserved_seats = []
