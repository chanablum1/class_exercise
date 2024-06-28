from cars_package.actions import total_cers, total_profit
from cars_package.menu import menu
# from json.loed_json import read_json


my_car_list = []


def maim_menu(my_car_list):
    # read_json()
    while True:
        print(f"Currently there are {total_cers(my_car_list)} cars. The current profit is: {total_profit(my_car_list)} NIS")
        print("Hello, this is my garage")
        print("please choose an option:")
        print("1 - Get all cars")
        print("2 - Add car")
        print("3 - delete car")
        print("4 - Search the car list for a car")
        print("5 - edit car")
        print("6 - save all cars")
        print("7 - exit")
        choice = input("Your choice is: ")
        menu(my_car_list, choice)


if __name__ == "__main__":
    maim_menu(my_car_list)
