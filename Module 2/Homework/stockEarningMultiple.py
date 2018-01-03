# Imports
import sys

titles = ["Stock", "Share", "Earning/Loss"]


# Take Name for Final Print Statement
name = input("What is your name? ")


# Variable Declarations for Stocks and Add to the List
stocks = []

stock1 = input("Enter First Stock Symbol: ")
stock2 = input("Enter Second Stock Symbol: ")
stock3 = input("Enter Third Stock Symbol: ")
stock4 = input("Enter Fourth Stock Symbol: ")
stock5 = input("Enter Fifth Stock Symbol: ")

stocks.append(stock1)
stocks.append(stock2)
stocks.append(stock3)
stocks.append(stock4)
stocks.append(stock5)



# Variable Declaration for Number of Shares
number_shares = []

stock1_shares = input("How Many Shares do you have in " + format(stock1) + "? ")
stock2_shares = input("How Many Shares do you have in " + format(stock2) + "? ")
stock3_shares = input("How Many Shares do you have in " + format(stock3) + "? ")
stock4_shares = input("How Many Shares do you have in " + format(stock4) + "? ")
stock5_shares = input("How Many Shares do you have in " + format(stock5) + "? ")

number_shares.extend([stock1_shares, stock2_shares, stock3_shares, stock4_shares, stock5_shares]) # Extends the array and appends all Share Amounts


# Take User Stock Purchase Price with Input
stock_purchase_prices = []

stock1_purchase = input(format(stocks[0]) + "'s purchase price: ")
stock2_purchase = input(format(stocks[1]) + "'s purchase price: ")
stock3_purchase = input(format(stocks[2]) + "'s purchase price: ")
stock4_purchase = input(format(stocks[3]) + "'s purchase price: ")
stock5_purchase = input(format(stocks[4]) + "'s purchase price: ")

stock_purchase_prices.extend([stock1_purchase, stock2_purchase, stock3_purchase, stock4_purchase, stock5_purchase])



# Print Titles for the table
print(titles[0] + " | " + titles[1] + " | " + titles[2])

# Print Seperator
print("-----------------------------")

# Print Stock Symbols
for stock_symbol in stocks:
    print(format(stock_symbol))


# Print Shares Owned
for share in number_shares:
    print(format(share))


# Print Stock Purchase Price Values
for purchase_price in stock_purchase_prices:
    print(format(purchase_price))