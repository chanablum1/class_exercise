#  print("1 - Get all cars")
#         print("2 - Add car")
#         print("3 - delete car")
#         print("4 - Search the car list for a car")
#         print("4 - edit car")
#         print("5 - save car")
#         print("6 - exit")


from cars_package.actions import add_car, delete_car, get_list, search_car
# from json.loed_json import save_json


def menu(my_car_list, choice):
    if choice == "1":
       return get_list(my_car_list)
    elif choice == "2":
        return add_car(my_car_list)
    elif choice == "3":
        return delete_car(my_car_list)
    elif choice == "4":
        return search_car(my_car_list)
    # elif choice == "6":
    #     return "!!!!!!!!!!!!!!!!!!" , save_json(my_car_list)
    elif choice == "7":
        exit()

