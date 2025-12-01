from car import Car
from parking_spot import ParkingSpot
from driver import Driver
import datetime


class Parking:
    def __init__(self, spot_count):
        self.spots = [ParkingSpot(i+1) for i in range(spot_count)]
        
    def load_data(self, num, model, driver_name):
        car = Car(model, Driver(driver_name))
        self.spots[num - 1].car = car
        
    def save_data(self):
        with open("parking_data.txt", "w") as f:
            for spot in self.spots:
                if spot.car:
                    line = f"{spot.number},{spot.car.model},{spot.car.driver}\n"
                    f.write(line) 
                    
    def log_action(self, action_str):
        with open("parking_log.txt", "a", encoding="utf-8") as f:
            time_str = datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S")
            f.write(f"{time_str} - {action_str}\n")
            
    def park_car(self, car):
        for spot in self.spots: 
            if spot.is_empty_spot() is True:
                spot.car = car 
                self.save_data()
                self.log_action(f"Въезд: {car} на место {spot.number}")
                print(f"Автомобиль припаркован на место {spot.number}")
                return
        raise Exception("Нет свободных мест!")
    
    def unpark_car(self, spot_number):
        if spot_number < 1 or spot_number > len(self.spots):
            raise Exception("Некорректный номер места!")
        spot = self.spots[spot_number - 1]
        if spot.car:
            car = spot.car
            spot.car = None
            self.save_data()
            self.log_action(f"Выезд: {car} с места {spot.number}")
            print(f"Автомобиль с места {spot.number} выехал")
        else:
            raise Exception("Это место уже свободно!")

    def print_status(self):
        print("Статус парковки:")
        for spot in self.spots:
            if spot.car:
                print(f"Место {spot.number}: {spot.car}")
            else:
                print(f"Место {spot.number}: свободно")
