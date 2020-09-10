import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = self.validate(brand)
        self.photo_file_name = self.validate_photo(photo_file_name)
        self.carrying = float(self.validate(carrying))

    def validate_photo(self, name):
        for i in ('.jpg', '.jpeg', '.png', '.gif'):
            if name.endswith(i) and len(name) > len(i):
                return name
        raise ValueError

    def validate(self, data):
        if len(data) < 1:
            raise ValueError
        return data

    def get_photo_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)
        if type(ext[1]) is not str:
            return ''
        return ext[1]

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(self.validate(passenger_seats_count))


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_length, self.body_width, \
            self.body_height = self.get_body_whls(body_whl)

    def get_body_volume(self):
        return self.body_height * self.body_length * self.body_width

    def get_body_whls(self, body_whl):
        buff = body_whl.split('x')
        if len(buff) == 3:
            try:
                return [float(x) for x in buff]
            except ValueError:
                pass
        return [0.0] * 3


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = self.validate(extra)


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            cls_obj = None
            try:
                if len(row) == 7:
                    car_type = row[0]
                    if car_type == 'car':
                        cls_obj = Car(brand=row[1],
                                      passenger_seats_count=row[2],
                                      photo_file_name=row[3],
                                      carrying=row[5])
                    elif car_type == 'truck':
                        cls_obj = Truck(brand=row[1],
                                        photo_file_name=row[3],
                                        body_whl=row[4],
                                        carrying=row[5])
                    elif car_type == 'spec_machine':
                        cls_obj = SpecMachine(brand=row[1],
                                              photo_file_name=row[3],
                                              carrying=row[5],
                                              extra=row[6])
                if cls_obj is not None:
                    car_list.append(cls_obj)
            except Exception:
                pass
    return car_list

