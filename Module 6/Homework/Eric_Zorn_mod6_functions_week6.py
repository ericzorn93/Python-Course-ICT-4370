"""
    Eric Zorn - ICT 4370: Module 6 Classes in Python - 1/29/2018

    In this assignment, we have created a program that runs off of object-oriented code. I have included a number of
    different classes in an external Python Module within the same root folder. Those classes, including all of their
    attributes and methods are imported as well into the code_run() function that is in this module of the code.
    I have assigned an instance of the investor class to the variable user_bob. Then, I assigned an instance of the
    bond class to the variable bob_smith_bond, which inherits from the StockData class.

    All of the code is called and run from the code_run function. Then, the code_run function is called within the
    main() function. When the program evaluates if __name__ == "__main__", the main function will be called and
    will finally execute all of the necessary code.

    This Build upon the last assignment with CSV data instead of hard-coded data
"""

# Import All (*) from Other Module
from Eric_Zorn_mod6_classes_week6 import *
import csv

def code_run():
    # Assigns Investor Class Inheritance for the User Bob Smith
    user_bob = Investor("Bob", "Smith", "123 Main Street", "212-503-9046")

    # Assigns User Bonds for Bob Smith
    bob_smith_bond = Bonds("GT2:GOV", 100.02, 100.05, 200, 1.38, 1.35)

    # Working With Opening Files
    with open('Lesson6_Data_Stocks.csv', 'r') as stock_data_file:
        reader = csv.reader(stock_data_file)
        rows = []
        for row in reader:
           rows.append(row)

        titles = rows[0]

        print(titles, end=' | ')

        stock_data_file.close()



    # Assigning Variables to inherit from the Stock Data Class
    goog = StockData("GOOG", 125, 772.88, 941.53)
    msft = StockData("MSFT", 85, 56.60, 73.04)
    rds_a = StockData("RDS-A", 400, 49.58, 55.74)
    aig = StockData("AIG", 235, 54.21, 65.27)
    fb = StockData("FB", 150, 124.31, 172.45)
    m = StockData("m", 425, 30.30, 23.98)
    f = StockData("f", 85, 12.58, 10.95)
    ibm = StockData("IBM", 80, 150.37, 145.30)

    # Dictionary Declaration
    stocks_dict = {}

    # Stock Dict Assignments with Stock Values
    stocks_dict["goog"] = {
        "symbol": goog.symbol,
        "shares": goog.shares_owned,
        "purchase_price": goog.purchase_price,
        "current_price": goog.current_price,
        "purchase_date": goog.purchase_date,
        "current_date": goog.currentDate(),
        "earn_loss": round(goog.earnLossConversion(goog.shares_owned, goog.current_price, goog.purchase_price), 2),
        "yearly_yield": round(goog.newYearlyCalc(goog.current_price, goog.purchase_price), 2),
        "id": goog.id
    }

    stocks_dict["msft"] = {
        "symbol": msft.symbol,
        "shares": msft.shares_owned,
        "purchase_price": msft.purchase_price,
        "current_price": msft.current_price,
        "purchase_date": msft.purchase_date,
        "current_date": msft.currentDate(),
        "earn_loss": round(msft.earnLossConversion(msft.shares_owned, msft.current_price, msft.purchase_price), 2),
        "yearly_yield": round(msft.newYearlyCalc(msft.current_price, msft.purchase_price), 2),
        "id": msft.id
    }


    stocks_dict["rds-a"] = {
        "symbol": rds_a.symbol,
        "shares": rds_a.shares_owned,
        "purchase_price": rds_a.purchase_price,
        "current_price": rds_a.current_price,
        "purchase_date": rds_a.purchase_date,
        "current_date": rds_a.currentDate(),
        "earn_loss": round(rds_a.earnLossConversion(rds_a.shares_owned, rds_a.current_price, rds_a.purchase_price), 2),
        "yearly_yield": round(rds_a.newYearlyCalc(rds_a.current_price, rds_a.purchase_price), 2),
        "id": rds_a.id
    }

    stocks_dict["aig"] = {
        "symbol": aig.symbol,
        "shares": aig.shares_owned,
        "purchase_price": aig.purchase_price,
        "current_price": aig.current_price,
        "purchase_date": aig.purchase_date,
        "current_date": aig.currentDate(),
        "earn_loss": round(aig.earnLossConversion(aig.shares_owned, aig.current_price, aig.purchase_price), 2),
        "yearly_yield": round(aig.newYearlyCalc(aig.current_price, aig.purchase_price), 2),
        "id": aig.id
    }

    stocks_dict["fb"] = {
        "symbol": fb.symbol,
        "shares": fb.shares_owned,
        "purchase_price": fb.purchase_price,
        "current_price": fb.current_price,
        "purchase_date": fb.purchase_date,
        "current_date": fb.currentDate(),
        "earn_loss": round(fb.earnLossConversion(fb.shares_owned, fb.current_price, fb.purchase_price), 2),
        "yearly_yield": round(fb.newYearlyCalc(fb.current_price, fb.purchase_price), 2),
        "id": fb.id
    }

    stocks_dict["m"] = {
        "symbol": m.symbol,
        "shares": m.shares_owned,
        "purchase_price": m.purchase_price,
        "current_price": m.current_price,
        "purchase_date": m.purchase_date,
        "current_date": m.currentDate(),
        "earn_loss": round(m.earnLossConversion(m.shares_owned, m.current_price, m.purchase_price), 2),
        "yearly_yield": round(m.newYearlyCalc(m.current_price, m.purchase_price), 2),
        "id": m.id
    }

    stocks_dict["f"] = {
        "symbol": f.symbol,
        "shares": f.shares_owned,
        "purchase_price": f.purchase_price,
        "current_price": f.current_price,
        "purchase_date": f.purchase_date,
        "current_date": f.currentDate(),
        "earn_loss": round(f.earnLossConversion(f.shares_owned, f.current_price, f.purchase_price), 2),
        "yearly_yield": round(f.newYearlyCalc(f.current_price, f.purchase_price), 2),
        "id": f.id
    }

    stocks_dict["ibm"] = {
        "symbol": ibm.symbol,
        "shares": ibm.shares_owned,
        "purchase_price": ibm.purchase_price,
        "current_price": ibm.current_price,
        "purchase_date": ibm.purchase_date,
        "current_date": ibm.currentDate(),
        "earn_loss": round(ibm.earnLossConversion(ibm.shares_owned, ibm.current_price, ibm.purchase_price), 2),
        "yearly_yield": round(ibm.newYearlyCalc(ibm.current_price, ibm.purchase_price), 2),
        "id": ibm.id
    }

    # Outputs a new Line to the console to separate the bash command.
    print("\n")

    # Prints out User information stored in the Bob Variable and calling the Full name attribute
    # Uses String format concatenation
    print("Stock information for {0}".format(user_bob.full_name))

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


    # Some Error Handling
    for key in stocks_dict:
        try:
            stocks_dict[key]
        except KeyError as err:
            print('KeyError: stocks_dict has no key', err)



    # Print Bond Information for Bob Smith
    print("\n\nBond Information for {0}\n-------------------------------".format(user_bob.full_name))

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
    for val in bob_smith_bond_info:
        if val not in bob_smith_bond_info:
            exit()
        else:
            pass

    # print("ID: {0}".format(bob_smith_bond.id))
    # print("Symbol: {0}".format(bob_smith_bond.symbol))
    # print("Purchase Price: ${0}".format(bob_smith_bond.purchase_price))
    # print("Current Price: ${0}".format(bob_smith_bond.current_price))
    # print("Quantity: {0}".format(bob_smith_bond.quantity))
    # print("Coupon: {0}".format(bob_smith_bond.coupon))
    # print("Yield: {0}%".format(bob_smith_bond.yield_amt_pct))
    # print("Purchase Date: {0}".format(bob_smith_bond.purchase_date))



# Main Function
def main():
    code_run()




# Main Function Call
if __name__ == '__main__':
    main()