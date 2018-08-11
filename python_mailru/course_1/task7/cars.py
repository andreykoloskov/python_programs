import csv
import sys
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)


    def __str__(self):
        return f"{self.car_type} : {self.brand} : {self.photo_file_name} : " \
               f"{self.carrying} : {self.passenger_seats_count}"


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        whl_list = body_whl.split('x')
        self.body_length = float(whl_list[0]) if len(whl_list) >= 3 else 0.0
        self.body_width = float(whl_list[1]) if len(whl_list) >= 3 else 0.0
        self.body_height = float(whl_list[2]) if len(whl_list) >= 3 else 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

    def __str__(self):
        return f"{self.car_type} : {self.brand} : {self.photo_file_name} : " \
               f"{self.carrying} : {self.body_length} : {self.body_width} : " \
               f"{self.body_height}"


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra

    def __str__(self):
        return f"{self.car_type} : {self.brand} : {self.photo_file_name} : " \
               f"{self.carrying} : {self.extra}"


def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        for row in reader:
            if (len(row) < 7):
                continue

            if row[0] == 'car':
                car_list.append(Car(row[1], row[3], row[5], row[2]))
            elif row[0] == 'truck':
                car_list.append(Truck(row[1], row[3], row[5], row[4]))
            elif row[0] == 'spec_machine':
                car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))

    return car_list


if __name__ == '__main__':
    car_list = get_car_list(sys.argv[1])

    for car in car_list:
        print(car)
