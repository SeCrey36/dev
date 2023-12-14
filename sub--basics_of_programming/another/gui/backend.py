"""Practical 6"""
import json

class Main:
    """Class main: обёрточный класс для взаимодействия"""
    def __init__(self):
        self.airplanes = []
        self.airplane = None

    def select_airplane(self):
        """Func: select airplane from aiprlanes list"""
        try:
            for i, pl_class in enumerate(self.airplanes):
                print(i, pl_class.name)
            self.airplane = self.airplanes[int(input('Input number of plane: '))]
        except IndexError:
            print('Index Error / 0 airplanes')
        except ValueError:
            print('Input must be int')

    def add_airplane_object(self, info):
        """Func: add airplane to airplanes list"""
        airplane = Airplane(info[0])
        zone1 = Zone("Economy Class", "Low", info[1]*[0],
                      info[2])
        zone2 = Zone("Business Class", "Medium", info[3]*[0],
                     info[4])
        zone3 = Zone("First Class", "High", info[5]*[0],
                     info[6])
        airplane.zones = [zone1, zone2, zone3]
        self.airplanes.append(airplane)

    def del_airplane(self):
        """Func: delete airplane from airplanes list"""
        self.airplanes.remove(self.airplane)
        self.airplane = None

    def plane_info(self):
        """Func: print airplane info"""
        if self.airplane is not None:
            pl_name, zones = self.airplane.plane_info()
            print(f'Plane name: {pl_name}')
            for zone in zones:
                print(zone)
        else:
            print('Choose airplane!')

    def booking(self):
        """Func: booking"""
        if self.airplane is not None:
            inp_zone = int(input(f'What zone u want? '
                                    f'(1 - eco ({self.airplane.zones[0].price}), '
                                    f'2 - busi ({self.airplane.zones[1].price}), '
                                    f'3 - elite ({self.airplane.zones[2].price})): '))
            if inp_zone == 1:
                print(str(self.airplane.zones[0]))
                print(self.airplane.reserve_seat(self.airplane.zones[0],
                int(input('Number of seat: '))))
            elif inp_zone == 2:
                print(str(self.airplane.zones[1]))
                print(self.airplane.reserve_seat(self.airplane.zones[1],
                int(input('Number of seat: '))))
            elif inp_zone == 3:
                print(str(self.airplane.zones[2]))
                print(self.airplane.reserve_seat(self.airplane.zones[2],
                int(input('Number of seat: '))))
            else:
                print('Incorrect')
        else:
            print('Choose airplane!')

    def del_book(self):
        """Func: delete booking"""
        if self.airplane is not None:
            inp_zone = int(input('What zone u want del? (1 - eco, 2 - busi, 3 - elite): '))
            if inp_zone == 1:
                print(self.airplane.del_reserve(self.airplane.zones[0], int(input('What seat?: '))))
            elif inp_zone == 2:
                print(self.airplane.del_reserve(self.airplane.zones[1], int(input('What seat?: '))))
            elif inp_zone == 3:
                print(self.airplane.del_reserve(self.airplane.zones[2], int(input('What seat?: '))))
            else:
                print('Incorrect')
        else:
            print('Choose airplane!')

    def load_json(self):
        info = [name, e_seats, e_price, b_seats, b_price, f_seats, f_price]
        Main.add_airplane_object(info)

    def add_airplane(self, info):
        json_str = {'name': info[0],
                    'e_seats': info[1],
                    'e_price': info[2],
                    'b_seats': info[3],
                    'b_price': info[4],
                    'f_seats': info[5],
                    'f_price': info[6],
                    }
        with open('sub--basics_of_programming/another/gui/cfg/data.json', 'w', encoding="utf-8") as f:
            f.write(json.dumps(json_str))
        Main.add_airplane_object(self, 1)


class Airplane:
    """Class airplane: сущность самолета"""
    def __init__(self, name):
        self.name = name
        self.zones = []

    def plane_info(self):
        """Func: print airplane info"""
        temp = []
        for zone in self.zones:
            temp.append(f"- Zone: {zone.name}, Tariff: {zone.tariff}, Price: {zone.price},"
                        f" Available Seats: {zone.seats.count(0)}")
        return self.name, temp

    @staticmethod
    def reserve_seat(zone, seat_number):
        """Func: booking"""
        try:
            if zone.seats[seat_number-1] == 0:
                zone.seats[seat_number-1] = 1
                return f"Seat {seat_number} in {zone.name} reserved."
            return f"No available seats in {zone.name}."
        except IndexError:
            print('IndexError')
            return 'Error'

    @staticmethod
    def del_reserve(zone, seat_number):
        """Func: delete booking"""
        try:
            if zone.seats[seat_number-1] == 1:
                zone.seats[seat_number-1] = 0
                return f"Reservation for seat {seat_number} in {zone.name} canceled."
            return f"No reservation found for seat {seat_number} in {zone.name}."
        except IndexError:
            print('IndexError')
            return 'Error'


class Zone:
    """Class zone: сущность зоны (привязана к самолету)"""
    def __init__(self, name, tariff, seats, price):
        self.name = name
        self.tariff = tariff
        self.price = price
        self.seats = seats


    def __str__(self):
        res = ''
        for i, el in enumerate(self.seats):
            if el:
                res += f'Место № {i+1}, цена - {self.price}, занято \n'
            else:
                res += f'Место № {i+1}, цена - {self.price}, свободно \n'
        return res

class Booking:
    """Class booking: сущность записи на рейс"""
    def __init__(self):
        self.reserved_seats = []
