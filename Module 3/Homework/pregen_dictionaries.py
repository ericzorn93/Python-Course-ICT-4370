"""
    Eric Zorn 1/8/2018 Stock Earnings Summary: ICT 4370 Winter 2018 Module 2

    In this project, I was able to build two different tables with prefilled user data. I was able to store all of the information
    into the appropriate variables as lists of information. I then was able to gain user input for the person's name. I then performed
    the logic of earnings or losses and built a new list with those given values by using the Python append() function.

    I imported a library known as texttable to build the first formatted table of information and have also built a custom table beneath it.
    I used a proper header with the name value and the format() functions for appending all of these values to a string of text.

    Attached to this submission as well is a table that is built completely off of user input. I wanted to give it a try with functions in Python.

"""

# Import Text Table Module/Library
import texttable

# Set
table = texttable.Texttable()

# Pre-defined variables of stock information
name = input("What is your full name? ")

titles = ["Stock Symbol", "NO Shares", "Purchase Price", "Current Value", "Earnings/Losses"]
stock_symbols = ["GOOGL", "MSFT", "RDS-A", "AIG", "FB"]
number_shares = [125, 85, 400, 235, 150]
purchase_prices = [772.88, 56.60, 49.58, 54.21, 124.31]
current_prices = [941.53, 73.04, 55.74, 65.27, 172.45]


earns_losses = []

full_list = []


# The formula is (Shares own * current price) - (shares own * bought price)
earn_loss_one = (number_shares[0] * current_prices[0]) - (number_shares[0] * purchase_prices[0])
earns_loss_two = (number_shares[1] * current_prices[1]) - (number_shares[1] * purchase_prices[1])
earns_loss_three = (number_shares[2] * current_prices[2]) - (number_shares[2] * purchase_prices[2])
earns_loss_four = (number_shares[3] * current_prices[3]) - (number_shares[3] * purchase_prices[3])
earns_loss_five = (number_shares[4] * current_prices[4]) - (number_shares[4] * purchase_prices[4])
earns_losses.append(earn_loss_one)
earns_losses.append(earns_loss_two)
earns_losses.append(earns_loss_three)
earns_losses.append(earns_loss_four)
earns_losses.append(earns_loss_five)


# Append and Print Nested List to full_list variable
full_list.append(titles)
full_list.append(stock_symbols)
full_list.append(number_shares)
full_list.append(purchase_prices)
full_list.append(current_prices)
full_list.append(earns_losses)




# print(full_list)

# Check for Floating Point Number Function
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

# Check to see if Name Variable is an Integer or a Float. If so, program will exit
if name.isdigit() or isFloat(name):
    exit()


# Create Table as long as all data is True and the correct data type
print("\n\n")
print("Stock Table Info for {0} (TextTable Library)".format(name.upper()))
print("---------------------------------------")
header = titles
table.header(header)
row = [stock_symbols[0], number_shares[0], purchase_prices[0], current_prices[0], earns_losses[0]]
table.add_row(row)
row = [stock_symbols[1], number_shares[1], purchase_prices[1], current_prices[1], earns_losses[1]]
table.add_row(row)
row = [stock_symbols[2], number_shares[2], purchase_prices[2], current_prices[2], earns_losses[2]]
table.add_row(row)
row = [stock_symbols[3], number_shares[3], purchase_prices[3], current_prices[3], earns_losses[3]]
table.add_row(row)
row = [stock_symbols[4], number_shares[4], purchase_prices[4], current_prices[4], earns_losses[4]]
table.add_row(row)


# Draw the Table
draw_table = table.draw()
print(draw_table)




print("\n\n\n")
print("Stock Table Info for {0} (Custom Table)".format(name.upper()))
print("---------------------------------------")
print("{0} | {1} | {2} | {3} | {4}".format(titles[0], titles[1], titles[2], titles[3], titles[4]))
print("{0}        | {1}       | {2}         | {3}        | ${4}".format(stock_symbols[0], number_shares[0], purchase_prices[0], current_prices[0], earns_losses[0]))
print("{0}         | {1}        | {2}           | {3}         | ${4}".format(stock_symbols[1], number_shares[1], purchase_prices[1], current_prices[1], earns_losses[1]))
print("{0}        | {1}       | {2}          | {3}         | ${4}".format(stock_symbols[2], number_shares[2], purchase_prices[2], current_prices[2], earns_losses[2]))
print("{0}          | {1}       | {2}          | {3}         | ${4}".format(stock_symbols[3], number_shares[3], purchase_prices[3], current_prices[3], earns_losses[3]))
print("{0}           | {1}       | {2}         | {3}        | ${4}".format(stock_symbols[4], number_shares[4], purchase_prices[4], current_prices[4], earns_losses[4]))