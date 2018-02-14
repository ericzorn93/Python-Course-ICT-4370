# This can be added on line 38 to
stocks_list = []
"""
stocks_list.append(goog)
stocks_list.append(msft)
stocks_list.append(rds_a)
stocks_list.append(aig)
stocks_list.append(fb)
stocks_list.append(m)
stocks_list.append(f)
stocks_list.append(ibm)
stocks_list.append(appl)
"""


#################################

# Outputs a new Line to the console to separate the bash command.
print("\n")

# Prints out User information stored in the Bob Variable and calling the Full name attribute
# Uses String format concatenation
print(
    "\n\nBond Information for {0}.\nBob's phone number is {1} and his address is {2}\n-----------------------------"
        .format(
        user_bob.full_name, user_bob.phone_number, user_bob.address)
)

# Loop Through titles variable and print out the table headers
for title in titles:
    print(title, end=' | ')

# Print New Line
print("\n")

# Loop Through Entire Dictionary
for key, val in stocks_dict.items():
    # print(key.upper())
    # Assigns Iterated Values to each new variable declaration for every iteration
    symbol = val["symbol"]
    shares = val["shares"]
    purchase = val["purchase_price"]
    current = val["current_price"]
    earn_loss = round(val["earn_loss"], 2)
    yearly_yield = val["yearly_yield"]
    id = val["id"]
    purchase_date = "8/1/2018"
    final_print = "{0:2d} | {1:6s} | {2:8d} | ${3:<7.2f} | ${4:<6.2f} | ${5:<8.2f} | {6:13s} | {7:18.2f}% | {8:13s} | ".format(
        id,
        symbol.upper(),
        shares,
        purchase,
        current,
        earn_loss,
        purchase_date,
        yearly_yield,
        purchase_date
    )

    buildTable(final_print)

# Print Steve Jobs Stock Information
print(
    "\n\nStock Information for {0}.\nHis phone number is {1} and his address is {2}\n-----------------------------"
        .format(
        user_steve.full_name, user_steve.phone_number, user_steve.address)
)

# Loop Through titles variable and print out the table headers
print("{0} | {1} | {2} |".format(titles[1], titles[2], titles[6]))
print("{0:6} | {1:8} | {2:13} |".format(apple_dict['appl']["symbol"], apple_dict['appl']["shares"], apple_dict['appl']["purchase_date"]))


# Some Error Handling in Stocks Dictionary
for key in stocks_dict:
    try:
        stocks_dict[key]
    except KeyError as err:
        print('KeyError: stocks_dict has no key', err)



# Print Bond Information for Bob Smith
print("\n\nBond Information for {0}.\nBob's phone number is {1} and his address is {2}\n---------------------------"
    .format(
    user_bob.full_name, user_bob.phone_number, user_bob.address)
)

# List of Bob Smith's Bond Information (Ordered)
bob_smith_bond_info = [
    bob_smith_bond.symbol,
    bob_smith_bond.purchase_price,
    bob_smith_bond.current_price,
    bob_smith_bond.quantity,
    bob_smith_bond.coupon,
    bob_smith_bond.yield_amt_pct,
    bob_smith_bond.purchase_date
]

# Simple Error Checking for Bob_Smith_Bond_Info List
try:
    for val in bob_smith_bond_info:
        if val not in bob_smith_bond_info:
            raise ValueError("Value is not in Bob Smith's Stock Information")
        else:
            pass
except ValueError:
    print("Value is not in Bob Smith's Stock Information")

# Print Bonds Table
print("ID: {0}".format(bob_smith_bond.id))
print("Symbol: {0}".format(bob_smith_bond.symbol))
print("Purchase Price: ${0}".format(bob_smith_bond.purchase_price))
print("Current Price: ${0}".format(bob_smith_bond.current_price))
print("Quantity: {0}".format(bob_smith_bond.quantity))
print("Coupon: {0}".format(bob_smith_bond.coupon))
print("Yield: {0}%".format(bob_smith_bond.yield_amt_pct))
print("Purchase Date: {0}".format(bob_smith_bond.purchase_date))
bob_smith_bond.readValues()


print("\n")