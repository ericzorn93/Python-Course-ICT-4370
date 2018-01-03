"""
    Eric Zorn 12/27/17 Stock Earnings Summary: ICT 4370 Winter 2018 Module 1

    In this script, we have been able to take in the user's input for their name, a stock symbol, shares of the stock
    owned, the stock's purchase price, and the current price.

    We then were able to print out a table of information based on each of the variable's values. Not only were all of the
    variable's values printed, but the use of the concatenation of strings and the format function were also used.

    At the end of the table is the final calculation for the total earnings or losses from the original stock purchase.
"""

#Import Decimal and set decimal
import decimal
decimal.Decimal(10.0)



#Ask User for their name
name = input("What is your name? ")

#Ask User for Stock Symbol
stock_symbol = input("What is the stock symbol? ")

#Ask User for Amount of Shares Owned
shares_owned = input(name + ", how many shares of " + stock_symbol + " do you own? ")

#Ask User for Price of Shares When Purchased
purchase_price = input("What was " + stock_symbol + "'s purchase price? ")

#Ask User for Price of Current Shares
current_price = input("What is " + stock_symbol + "'s current price? ")

""" End of Variable Declarations """

# Print New Line
print("\n\n")

# Print Outcomes of User Input
print("Stock ownership for " + name) 
print("------------------------------")

print(stock_symbol +": "+ shares_owned + " shares")
print("Purchase Price: " + purchase_price)
print("Current price per share: " + current_price)

# Print final Earning/Loss to Date 
# The formula is (Shares own * current price) - (shares own * bought price)
total_earnLoss = (int(shares_owned) * float(current_price)) - (int(shares_owned) * float(purchase_price))
print("------------------------------")

# Print Final Earnings or Losses
print("Final Earnings/Losses to Date: " + "$" + "{0}".format(total_earnLoss))

# Print White Space
print("\n\n")

exit() # Exit the program after the program has run