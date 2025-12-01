from parking import Parking
from car import Car
from driver import Driver


def main():
    parking = Parking(3)

    while True:
        print("\nВыберите действие:")
        print("1 - Въезд автомобиля")
        print("2 - Выезд автомобиля")
        print("3 - Статус парковки")
        print("0 - Выход")
        choice = input("Введите номер действия: ")

        if choice == '1':
            model = input("Введите модель автомобиля: ")
            driver_name = input("Введите имя водителя: ")
            car = Car(model, Driver(driver_name))
            try:
                parking.park_car(car)
            except Exception as e:
                print("Ошибка:", e)

        elif choice == '2':
            try:
                spot_number = int(input("Введите номер места для выезда: "))
                parking.unpark_car(spot_number)
            except Exception as e:
                print("Ошибка:", e)

        elif choice == '3':
            parking.print_status()

        elif choice == '0':
            print("Завершение программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()