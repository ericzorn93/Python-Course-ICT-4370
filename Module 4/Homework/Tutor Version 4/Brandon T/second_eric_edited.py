"""
    Eric Zorn - 1/19/2018 - ICT 4370: Professor Kaim

    In this assignment, we have built upon our last assignment. We were able to build a table in Python with outputting
    data after certain calculations have been performed. In the last assignment, we learned how the data type of lists
    had been used. We were then able to store the proper table data of stock information, including titles and values
    into those lists. I also had built an list to store the earns and losses for each stock. I was then able to append
    the list information values into the earns_losses variable. This had created a dynamic list, which is quite useful
    when programming in many different languages.

    After learning about lists, we then have learned about a new datatype which is also very popular. This week, we have
     learned about the dictionary datatype. After understanding how dictionaries have worked, I was then able to change
     the stock assignment to properly utilize this datatype. I have reassigned the lists to key value pairs with dictionaries
     in this assignment. Each variable was properly named and each of the keys is easily identifieable to the values.
     The function earnLossConversion takes in a number of parameters and calculates the earns or losses, depending on
     the incoming stock information. This information has also been imported to a dynamic dictionary, called earns_losses.
     Instead of using the Python append() function to be able to dynmiacally add data, I was able to use the update()
     function. The difference between these two built in functions is that one argument requires the dictionary key and
     the other requires the value.

    At the end of the program, I was able to build a formatted table with the proper strings of data that each stock has
    required.

"""

from datetime import date

# All Variable and Value Declarations


# The formula is (Shares own * current price) - (shares own * bought price)
def earnLossConversion(owned_shares, current_price, purchase_price):
    """
        This function simply takes in three parameters for the amount of shares owned, the current price and the purchase
         price. The function then uses each of the values entered into the parameters and calculates the earnings or losses
         for each stock. At the end of the function, it assigns the calculation to a variable known as earn_loss and then
         returns the variable. This earn_loss variable can then be used outside of the function scope and in other scopes
         within the program.
    """
    earn_loss = (owned_shares * current_price) - (owned_shares * purchase_price)
    return round(earn_loss, 2)

def foo(stocks_dict):
    for stock in stocks_dict.values():
        stock["earn_loss"] = earnLossConversion(stock["shares"], stock["purchase_price"], stock["current_price"])
        #stock["yearly_earn_loss"] = yearlyEarnLoss(stock["current_prive"], stock["purchase_price"], stock["current_price"])

def yearlyEarnLoss(current_value , purchase_price, current_date):
    """
        This function calculates the final yearly return losses or earnings with the stocks that are within the stock
        list. The calculation is the current value minus the purchase price, divided by the purchase price, divided by
        the current dat minus the purchase the date. At the end of this calculation, the value is multiplied by
        one-hundred.
    """
    yearly_return = (current_value - purchase_price)/ purchase_price#)/(current_date - purchase_date))) * 100
    return round(yearly_return * 100, 2)

# titles = {
#     'sym_title': "Symbol",
#     'num_share_title': "# Shares",
#     'purchase_title': "Purchase",
#     'curent_val_title': "Current",
#     'earn_loss_title': "Earn/Loss",
#     'purchase_date': "Purchase Date",
#     "yearly_earn_loss": "Yearly Earning/Loss"
# }

stocks_dict = {}

stocks_dict["google"] = {
    "symbol": "GOOG",
    "shares": 125,
    "purchase_price": 772.88,
    "current_price": 941.53
}

stocks_dict["microsoft"] = {
    "symbol": "MSFT",
    "shares": 85,
    "purchase_price": 56.60,
    "current_price": 73.04
}

stocks_dict["rds-a"] = {
    "symbol": "RDS-A",
    "shares": 400,
    "purchase_price": 49.58,
    "current_price": 55.74
}

stocks_dict["aig"] = {
    "symbol": "AIG",
    "shares": 235,
    "purchase_price": 54.21,
    "current_price": 65.27
}

stocks_dict["fb"] = {
    "symbol": "FB",
    "shares": 150,
    "purchase_price": 124.31,
    "current_price": 172.45
}

stocks_dict["m"] = {
    "symbol": "m",
    "shares": 425,
    "purchase_price": 30.30,
    "current_price": 23.98
}

stocks_dict["f"] = {
    "symbol": "f",
    "shares": 85,
    "purchase_price": 12.58,
    "current_price": 10.95
}

stocks_dict["ibm"] = {
    "symbol": "ibm",
    "shares": 80,
    "purchase_price": 150.37,
    "current_price": 145.30
}

titles = [
    "Symbol",
    "# Shares",
    "Purchase",
    "Current",
    "Earn/Loss",
    "Purchase Date",
    "Yearly Earning/Loss"
]

stock_symbols = {
    "goog": "GOOGL",
    "msft": "MSFT",
    "rds": "RDS-A",
    "aig": "AIG",
    "fb": "FB",
    "m": "M",
    "f": "F",
    "ibm": "IBM"
}

number_shares = {
    "goog": 125,
    "msft": 85,
    "rds": 400,
    "aig": 235,
    "fb": 150,
    "m": 425,
    "f": 85,
    "ibm": 80
}

purchase_prices = {
    "goog": 772.88,
    "msft": 56.60,
    "rds": 49.58,
    "aig": 54.21,
    "fb": 124.31,
    "m": 30.30,
    "f": 12.58,
    "ibm": 150.37
}

current_prices = {
    "goog": 941.53,
    "msft": 73.04,
    "rds": 55.74,
    "aig": 65.27,
    "fb": 172.45,
    "m": 23.98,
    "f": 10.95,
    "ibm": 145.30
}

earns_losses = {}
yearly_earns_losses = {}
name = input("What is your full name? ")

# Purchase Date Variable Declaration
purchase_date = "8/1/2015"


full_dic = {
    "titles": titles,
    "stock_symbols": stock_symbols,
    "number_shares": number_shares,
    "current_price": current_prices,
    "purchase_prices": purchase_prices,
    "earns_losses": earns_losses
}


date1 = "2008 8 18"
date1_strings = date1.split() # -->  ['2008', '8', '18']
date1_parts = [int(x) for x in date1_strings]
d0 = date( date1_parts[0], date1_parts[1], date1_parts[2] )

"""
If you have two date objects, you can just subtract them.

from datetime import date

d0 = date(2008, 8, 18)
d1 = date(2008, 9, 26)
delta = d0 - d1
print delta.days
The relevant section of the docs: https://docs.python.org/library/datetime.html
"""

# Print Introduction to the Table
print("\n") #Line Break
print("Stock Portfolio Information for {0}".format(name.upper()))
print("-----------------------------------------") # Seperator between the table data

# Print All Titles Horizontally with pipe symbol separator
for name in titles:
    print(name, end=' | ')

for key in number_shares:
    #print(number_shares[key])
    earns_losses.update({
        key: earnLossConversion(number_shares[key], current_prices[key], purchase_prices[key])
    })

    yearly_earns_losses.update({
        key: yearlyEarnLoss( current_prices[key], purchase_prices[key], purchase_date)
    })

# Function Calculation and Appending/Updating Data to Earns_Losses Dictionary
# earns_losses.update({
#     "num_one": earnLossConversion(number_shares["num_one"], current_prices["num_one"], purchase_prices["num_one"])
# })


"""
# Calculate Earns and Losses
yearly_earns_losses.update({
    "num1": yearlyEarnLoss(current_prices[0], purchase_prices[0], datetime.today())
})
"""

print(yearly_earns_losses)

# Print Final Table of Stocks
print("\n")

for key in stock_symbols:
    print("{0}\t| {1} \t  | {2}   | {3}  | ${4} | {5}%".format(
      stock_symbols[key], 
      number_shares[key],
      purchase_prices[key], 
      current_prices[key],
      earns_losses[key],
      yearly_earns_losses[key])
    )


# New Looped in Dictionaries
print("\n\n\n\n")


# Final Version Appending and Print for the Table
titles = [i for i in full_dic["titles"]]
stock_symbols = [i for i in full_dic["stock_symbols"].values()]
number_shares = [i for i in full_dic["number_shares"].values()]
purchase_prices = [i for i in full_dic["purchase_prices"].values()]
current_prices = [i for i in full_dic["current_price"].values()]
earns_losses = [i for i in full_dic["earns_losses"].values()]
#YEARLY EARN LOSSES

# Create Neested Dictionary with Lists of all Values
full_dic = {
    "titles": titles,
    0: [stock_symbols[0], number_shares[0], purchase_prices[0], current_prices[0], earns_losses[0], purchase_date],
    1: [stock_symbols[1], number_shares[1], purchase_prices[1], current_prices[1], earns_losses[1], purchase_date],
    2: [stock_symbols[2], number_shares[2], purchase_prices[2], current_prices[2], earns_losses[2], purchase_date],
    3: [stock_symbols[3], number_shares[3], purchase_prices[3], current_prices[3], earns_losses[3], purchase_date],
    4: [stock_symbols[4], number_shares[4], purchase_prices[4], current_prices[4], earns_losses[4], purchase_date],
    5: [stock_symbols[5], number_shares[5], purchase_prices[5], current_prices[5], earns_losses[5], purchase_date],
    6: [stock_symbols[6], number_shares[6], purchase_prices[6], current_prices[6], earns_losses[6], purchase_date]
}

print("Second Table Stock Portfolio Information for {0} \n".format(name.upper()))
for title in full_dic["titles"]:
    print(title, end=' | ')
    
print("")

print("\n")

for key in full_dic.items():
    if key[0] == "titles":
        continue
    else:
        print("{0}   |   {1}   |    ${2}   |   ${3}   |  ${4}   |    {5}".format(
            key[1][0], key[1][1], key[1][2], key[1][3], key[1][4], key[1][5])
        )


print("\n", purchase_date)




# print("\n\n")
# print("Stock Portfolio Information for {0}".format(name.upper()))
#
# for symbol in stock_symbols.values():
#     print("{0} - {1}".format(titles["sym_title"], symbol), end=' | ')
#
# print("\n")
#
# for num in number_shares.values():
#     print("{0} - {1}".format(titles["num_share_title"], num), end=' | ')
#
# print("\n")
#
# for purchase in purchase_prices.values():
#     print("{0} - ${1}".format(titles["purchase_title"], purchase), end=' | ')
#
# print("\n")
#
# for current in current_prices.values():
#     print("{0} - ${1}".format(titles["curent_val_title"], current), end=' | ')
#
# print("\n")
#
# for earn_loss in earns_losses.values():
#     print("{0} - ${1}".format(titles["earn_loss_title"], earn_loss), end=' | ')
