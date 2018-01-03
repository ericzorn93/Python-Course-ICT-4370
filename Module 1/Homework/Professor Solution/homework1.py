s"""Calculates how much money a person earns or loses
based on when the user buys a stock and the current price.
"""
import decimal 
decimal.Decimal(10.0)
# Define user provided inputs.
name = input("What is your name. ")
symbol = input("What is the stock symbol? ")
# While it is poosible to own partial shares this code only handles integers.
shares_own = input("How many shares do you own? ")
bought_price = input("Bought price? ")
current_price = input("Current price? ")
# Print user inputs.
print("Stock ownership for {0}".format(name))
print("----------------------------------------")
print("{0} : {1}".format(symbol, shares_own))
print("Current price per shares:{0}".format(current_price))

# Calucate the persons earning/lose from the stock.
# The forumla is (Shares own * current price) - (shares own * bought price)
earning = (int(shares_own) * float(current_price)) - (int(shares_own) * float(bought_price))
# This is also correct. 
earning2 = int(shares_own) * (float(current_price) - float(bought_price))
# Print the earning.
print("Total Earning:{0} ".format(earning))
print("Total Earning:{0} ".format(earning2))
 