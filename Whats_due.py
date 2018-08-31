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


def save():
    file_name = "serial_bills.pickle"
    with open(file_name, "wb") as bills2pay:
        pickle.dump(bills, bills2pay)


def start_over():
    cont = input("Start over?\n")
    if cont.lower() == 'y':
        main()
    else:
        print("Have a great day!")


# I cannot add a bill, but it does rewrite whats in the dictionary
def add(add_bill, cost):
    bills.update({add_bill: cost})
    save()
    print("These are your bills: ", bills)


# see delete() comment
def pay(name_of_bill, current_balance):
    try:
        # for every dictionary pair in bills dictionary:
        for item in bills:
            # if the desired bill to pay is equal to the dictionary pair:
            if name_of_bill == item:
                # set c_o_b to equal the value of the desired bill
                cost_of_bill = bills[name_of_bill]
                # print the cost of the bill
                print("Your bill costs: $%.2f" % cost_of_bill)
                # subtract my current balance from what bill costs
                current_balance -= cost_of_bill
                # show me how much money I have left over
                print("You will have this much remaining: $%.2f" % current_balance)
                # if the cost is greater than or equal to 0
                # # I really should change this, but it works because I don't actually change the value of...
                # # ...cost_of_bill when I'm subtracting with it, so basically it finds the item in the dictionary...
                # # ...sees that the item is still holding a value >= 0, and it deletes it.
                if cost_of_bill >= 0:
                    # remove the bill to be paid!
                    delete(name_of_bill)
    except RuntimeError:
        print("Runtime error")  # A runtime error occurred.


def zero_out(current_balance):
    total = 0
    subtract_all_these = bills.values()
    for item in subtract_all_these:
        total += item
    current_balance -= total
    print("You will have $%.2f" % current_balance, "after all bills are paid.")
    start_over()


# works unless it uses the pay method, it encounters a runtime error due...
# ...to the dictionary changing size during an iteration
def delete(name_of_bill):
    try:
        del bills[name_of_bill]
        save()
        print("These are your remaining bills: ", bills)
    except KeyError:
        print("Check your spelling please, bill does not exist.")


def clear():
    bills.clear()
    save()
    print(bills)


def view():
    try:
        print(bills)
    except FileNotFoundError:
        return {}


def main():
    # print("This is your current balance: $%.2f" % currentBalance)
    teller = input("Would you like to add a new bill, pay one, zero-out, delete one, clear all, or view your bills?\n"
                   "(Type 'a' to add, 'p' to pay, 'z' to zero-out, 'd' to delete,"
                   " 'c' to clear or 'v' to view)\n")
    if teller.upper() == "A":
        add_bill = input("What bill do you need to add?\n")
        cost = float(input("How much is due?\n"))
        add(add_bill, cost)
        start_over()
    elif teller.upper() == "P":
        name_of_bill = input("What bill do you want to pay?\n")
        pay(name_of_bill, current_balance)
        start_over()
    elif teller.upper() == "D":
        name_of_bill = input("What bill do you want to delete?\n")
        delete(name_of_bill)
        start_over()
    elif teller.upper() == "Z":
        zero_out(current_balance)
    elif teller.upper() == "C":
        clear()
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
# TODO: fix start over so that I'm not constantly starting from the beginning of the program every time...
# ...just remember that you have a global variable that holds your "current balance"
# TODO: make a function that clears the dictionary all at once

<LONG TERM GOALS>
# TODO: possibly add a dictionary for paid_bills = {}?
# TODO: find a way to visualize the data with charts
# TODO: make this easy to swap between users and their bills
# TODO: incorporate a calendar

<BUGS>
# if I pay a bill, current_balance is a global variable, it does not carry the subtracted value over...
# ...if I choose to start_over(). (if you have $1000 and you pay a $200 bill, you have $800 left over...
# ...however choose to start_over() and you have $1000 all over again.)
# If someone doesn't enter info to add a bill, handle the ValueError
# If someone doesn't enter a bill to delete, handle the KeyError...
# ...(Pay seems to have no effect when field is empty)
# Need to run tests with negative values, strings, and float values
# TODO: handle exceptions caused by tests ^
"""
