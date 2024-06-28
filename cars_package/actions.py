# get ilst
# add car
# delet car
# search Cor
# (edit car)
# exit

from problems_package.problem_menu import input_problems
from problems_package.problems import calculate_total_price


def get_list(my_car_list):
    for car in my_car_list:
        print(f"Car Number: {car['Car Number']}")
        print(f"Problems: {car['Problems']}")
        print(f"Total Cost: {calculate_total_price(car['Problems'])} NIS")


def add_car(my_car_list):
    print("I am hear !!!!!!!!!!!!!!!!")
    new_car_namber = input("Enter car number: ")
    a_problems = input_problems()
    total_price = calculate_total_price(a_problems)
    print(
        f"The price of this fix is: {total_price} NIS. Do you wish to proceed? yes/no"
    )
    choice = input("Your choice yas or no?: ")
    if choice.lower() == "yes":
        new_car = {"Car Number": new_car_namber,
                    "Problems": a_problems
                    }
        my_car_list.append(new_car)
        print("the Car added !!!!!!!!!!! .")
        print(
            "The vehicle is being serviced at the garage, we will update you after the service is completed"
        )
    else:
        print(
            "The vehicle has not been serviced in the garage, we will be happy to assist you at any time"
        )
        exit()


def delete_car(my_car_list):
    print("i am in delete")
    car_number = int(input("Enter the vehicle number you wish to delete: "))
    car_to_delete = search_car(my_car_list)
    if car_to_delete:
        confirm_delete = input(f"Are you sure you want to delete the vehicle number? {car_number}? (yes/no): ")
        if confirm_delete.lower() == 'yes':
            my_car_list.remove(car_to_delete)
            print(f"car_namber  {car_number}  delete!!! .")
        else:
            print("Cancellation of vehicle deletion.") 



def search_car(my_car_list):
    print("search!!!!!!!!!!!!!!!!!")
    search_car_nam = input("Please enter the vehicle number to search")
    found = False
    for car in my_car_list:
        if car["Car Number"] == search_car_nam:
            print(f"Car Number: {car['Car Number']}")
            print(f"Problems: {car['Problems']}")
            print(f"Total Cost: {calculate_total_price(car['Problems'])} NIS")
            return




def total_cers(my_car_list):
    return len(my_car_list)


def total_profit(car_list):
    return sum(calculate_total_price(car["Problems"]) for car in car_list)
