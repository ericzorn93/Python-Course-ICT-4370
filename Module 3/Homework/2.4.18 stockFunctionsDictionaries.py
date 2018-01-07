"""
    Eric Zorn 12/30/17 Stock Earnings Summary: ICT 4370 Winter 2018 Module 2

    This script has built upon the first script that we had written with building a table of stock earnings.
    We have now made the list dynamic and begun to build a table of information. I wrote many functions getting the
    stock symbols, names, share numbers, purchase price, and current stock price.

    I then appended all of the values to the different variable lists and built a table from those values using loops through the data.
"""


# Variable Declarations
titles = ["Stock", "Shares", "Purchase Price", "Current Price", "Earning/Loss"]
names = []
stock_symbols = []
number_shares = []
purchase_prices = []
current_prices = []
earnings_losses = []

def getName():
    name = input("What is your full name? ")
    names.append(name)
    return names


def getStockSymbol():
    stock_symbol = input("Enter Stock Symbol: ")
    stock_symbols.append(stock_symbol.upper())
    return stock_symbol

def getNumberShares():
    share_number = input("How many shares do you currently own? ")
    number_shares.append(share_number)
    return share_number

def getPurchasePrice():
    purchase_price = input("What was the stock purchase price? ")
    purchase_prices.append(float(purchase_price))
    return purchase_price

def getCurrentPrice():
    current_price = input("What is the current stock price? ")
    current_prices.append(float(current_price))
    return current_price


if names == []:
    getName()

if stock_symbols == []:
    while True:
        getStockSymbol()
        if len(stock_symbols) >= 5:
            break

if number_shares == []:
    while True:
        getNumberShares()
        if len(number_shares) >= 5:
           # print(number_shares)
            break

if purchase_prices == []:
    while True:
        getPurchasePrice()
        if len(purchase_prices) >= 5:
           # print(purchase_prices)
            break

if current_prices == []:
    while True:
        getCurrentPrice()
        if len(current_prices) >= 5:
           # print(current_prices)
            break



""" Start Loading Data into the Earning and Losses List """


# The formula is (Shares own * current price) - (shares own * bought price)
def earningLossCalc(owned_share, current_price, bought_price):
    earning_loss_calc = (float(owned_share) * float(current_price)) - (float(owned_share) * float(bought_price))
    earnings_losses.append(earning_loss_calc)
    return earning_loss_calc

if earnings_losses == []:
    earningLossCalc(number_shares[0], current_prices[0], purchase_prices[0])
    earningLossCalc(number_shares[1], current_prices[1], purchase_prices[1])
    earningLossCalc(number_shares[2], current_prices[2], purchase_prices[3])
    earningLossCalc(number_shares[3], current_prices[3], purchase_prices[3])
    earningLossCalc(number_shares[4], current_prices[4], purchase_prices[4])
    # print(earnings_losses)



""" BUILD TABLE OF DATE """

# PRINT TITLES
print("\n\n")


# Nest all titles, symbols, shares, prices, and earnings/losses into a nested list
stock_list = [
    titles,
    stock_symbols,
    number_shares,
    purchase_prices,
    current_prices,
    earnings_losses
]

"""Print Title of Table"""
print("Stock Ownership Portfolio for {0}".format(names[0]) + "\n")

print(titles[0] + "\t" + titles[1] + "\t" + titles[2] + "\t" + titles[3] + "\t" + titles[4])
print("------------------------------------------------------------------------------------")
print(str(stock_list[1][0]), "\t", str(stock_list[2][0]), "\t\t", str(stock_list[3][0]), "\t\t", str(stock_list[4][0]), "\t\t", str(stock_list[5][0]))
print(str(stock_list[1][1]), "\t", str(stock_list[2][1]), "\t\t", str(stock_list[3][1]), "\t\t", str(stock_list[4][1]), "\t\t", str(stock_list[5][1]))
print(str(stock_list[1][2]), "\t", str(stock_list[2][2]), "\t\t", str(stock_list[3][2]), "\t\t", str(stock_list[4][2]), "\t\t", str(stock_list[5][2]))
print(str(stock_list[1][3]), "\t", str(stock_list[2][3]), "\t\t", str(stock_list[3][3]), "\t\t", str(stock_list[4][3]), "\t\t", str(stock_list[5][3]))
print(str(stock_list[1][4]), "\t", str(stock_list[2][4]), "\t\t", str(stock_list[3][4]), "\t\t", str(stock_list[4][4]), "\t\t", str(stock_list[5][4]))






""" Alternate Table Print """
# print(titles[0])
# print(str(titles[0]) + ": " + str(stock_symbols[0]))
# print(str(titles[1]) + ": " + str(number_shares[0]))
# print(str(titles[2]) + ": " + str(current_prices[0]))
# print(str(titles[3]) + ": " + str(purchase_prices[0]))
# print(str(titles[4]) + ": $" + str(earnings_losses[0]))
#
# # Line Break
# print("\n", "--------------------")
#
# # print(titles[1])
# print(str(titles[0]) + ": " + str(stock_symbols[1]))
# print(str(titles[1]) + ": " + str(number_shares[1]))
# print(str(titles[2]) + ": " + str(current_prices[1]))
# print(str(titles[3]) + ": " + str(purchase_prices[1]))
# print(str(titles[4]) + ": $" + str(earnings_losses[1]))
#
# # Line Break
# print("\n", "--------------------")
#
# # print(titles[2])
# print(str(titles[0]) + ": " + str(stock_symbols[2]))
# print(str(titles[1]) + ": " + str(number_shares[2]))
# print(str(titles[2]) + ": " + str(current_prices[2]))
# print(str(titles[3]) + ": " + str(purchase_prices[2]))
# print(str(titles[4]) + ": $" + str(earnings_losses[2]))
#
# # Line break
# print("\n", "--------------------")
#
# # print(titles[3])
# print(str(titles[0]) + ": " + str(stock_symbols[3]))
# print(str(titles[1]) + ": " + str(number_shares[3]))
# print(str(titles[2]) + ": " + str(current_prices[3]))
# print(str(titles[3]) + ": " + str(purchase_prices[3]))
# print(str(titles[4]) + ": $" + str(earnings_losses[3]))
#
# # Line Break
# print("\n", "--------------------")
#
# # print(titles[4])
# print(str(titles[0]) + ": " + str(stock_symbols[4]))
# print(str(titles[1]) + ": " + str(number_shares[4]))
# print(str(titles[2]) + ": " + str(current_prices[4]))
# print(str(titles[3]) + ": " + str(purchase_prices[4]))
# print(str(titles[4]) + ": $" + str(earnings_losses[4]))


# Quit out of the program
exit()
