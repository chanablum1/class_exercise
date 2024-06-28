from problems_package.problems import get_all_problems


# def get_all_problems():
#     return ["Engine", "Breaks", "5000 km treatment", "10,000 km treatment", "Filters + Oil", "Gear"]

def input_problems():
    problems = []
    all_problems = get_all_problems()
    while True:
        print("Select a problem to add and then write - Save - for the purpose of preparing the vehicle for the database: ")
        for problem in all_problems:
            print(problem)
        problem = input("Problem / save and axit: ")
        if problem == 'Save':
            break
        if problem in all_problems:
            problems.append(problem)
        else:
            print("Problem not found, please try again.")
    return problems



# def problems_prices(problems_prices):
#     print("Please enter the problem number in the vehicle according to the list")