"""

Benjamin Blanchard
Budgeting App

"""
# DECLARATIONS
import pickle
with open("serial_bills.pickle", "rb") as startDict:
    view_all_bills = pickle.load(startDict)
    bills = view_all_bills
    # print(bills)
current_balance = int(input("How much money is in your account right now?\n"))


# I cannot add a bill, but it does rewrite whats in the dictionary
def add(add_bill, cost):
    bills.update({add_bill: cost})
    file_name = "serial_bills.pickle"
    with open(file_name, "wb") as bills2pay:
        pickle.dump(bills, bills2pay)
        print("These are your bills: ", bills)


# works unless it uses the pay method, it encounters a runtime error due
# to the dictionary changing size during an iteration
def delete(ans):
    del bills[ans]
    file_name = "serial_bills.pickle"
    with open(file_name, "wb") as bills2pay:
        pickle.dump(bills, bills2pay)
        print("These are your bills: ", bills)


# see delete() comment
def pay(ans, current_balance):
    try:
        for item in bills:
            if ans == item:
                cost_of_bill = bills[ans]
                print("Your bill costs: $%.2f" % cost_of_bill)
                current_balance -= cost_of_bill
                print(current_balance)
            else:
                for item2 in bills:
                    if ans == item2:
                        cost_of_bill2 = bills[ans]
                        if cost_of_bill2 >= 0:
                            delete(ans)
                            # add here print(cost_of_bill2)
    except FileNotFoundError:
        print("FileNotFoundError!")

# reference for original structure
# def pay(ans, current_balance):
#     try:
#         # # old code
#         #
#         # with open("serial_bills.pickle", "rb") as about2pay:
#         #     bothFromDict = pickle.load(about2pay)
#         #     print(bothFromDict)
#         #     keyMaster = bothFromDict.keys()
#         # # keyMaster is bills
#             for item in bills:
#                 if ans == item:
#                     cost_of_bill = bills[ans]
#                     print("Your bill costs: $%.2f" % cost_of_bill)
#                     # make this a nested function (rm bill():?) #
#                     # ans2 = float(input("How much can you pay?\n"))
#                     # paid_bill = cost_of_bill - ans2
#                     current_balance -= 50
#                     # what to do if neg num?
#                     if current_balance <= 0:
#                         # good effect but did not work
#                         delete(ans)
#                         # encounters runtime error due to dictionary change in size
#                         # # bills was bothFromDict
#                         # bills.pop(ans)
#                     elif current_balance >= 0:
#                         print(current_balance)
#                 else:
#                     print('this')
#     except FileNotFoundError:
#         print("whoops")


def view():
    try:
        print(bills)
    except FileNotFoundError:
        return {}


def start_over():
    cont = input("Start over?\n")
    if cont.lower() == 'y':
        main()
    else:
        print("Have a great day!")


def main():
    # print("This is your current balance: $%.2f" % currentBalance)
    teller = input("Would you like to add a new bill, pay an existing, delete, or view your bills?\n")
    if teller.upper() == "A":
        add_bill = input("What bill do you need to add?\n")
        cost = float(input("How much is due?\n"))
        add(add_bill, cost)
        start_over()
    elif teller.upper() == "P":
        ans = input("What bill do you want to pay?\n")
        pay(ans, current_balance)
        start_over()
    elif teller.upper() == "D":
        ans = input("What bill do you want to delete?\n")
        delete(ans)
        start_over()
    else:
        print("This is your current balance: $%.2f" % current_balance)
        print("And these are your bills:")
        view()
        start_over()


main()

"""
<MAJOR ISSUES>
# delete() works unless it uses the pay() first, it encounters a runtime error due...
# ...to the dictionary changing size during an iteration
# TODO: figure out how to pay bills in dict w/out errors

<SHORT TERM GOALS>
# TODO: make program subtract all dict values from current_balance at once to predict finances for the month

<LONG TERM GOALS>
# TODO: possibly add a dictionary for paid_bills = {}?
# TODO: find a way to visualize the data with charts
# TODO: make this easy to swap between users and their bills
# TODO: incorporate a calendar

<BUGS>
# If someone doesn't enter info to add a bill, handle the ValueError
# If someone doesn't enter a bill to delete, handle the KeyError...
# ...(Pay seems to have no effect when field is empty)
# Need to run tests with negative values, strings, and float values
# TODO: handle exceptions caused by tests ^
"""
