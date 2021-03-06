"""Beginning of the Program"""

# Imports from other Modules
from StockClasses import Investor, StockData, Bonds

def main():

    # Assigns Investor Class Inheritance for the User Bob Smith
    user_bob = Investor("Bob", "Smith", "123 Main Street", "212-503-9046")
    E = Investor("Bob", "Smith", "123 Main Street", "212-503-9046")

    # Table Titles
    titles = [
        "Symbol",
        "# Shares",
        "Purchase",
        "Current",
        "Earn/Loss",
        "Purchase Date",
        "Yearly Earning/Loss"
    ]

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
        "coupon": Bonds(goog.symbol, goog.shares_owned, goog.purchase_price, goog.current_price, goog.shares_owned,
                        10, 23)
    }

    stocks_dict["msft"] = {
        "symbol": msft.symbol,
        "shares": msft.shares_owned,
        "purchase_price": msft.purchase_price,
        "current_price": msft.current_price,
        "purchase_date": msft.purchase_date,
        "current_date": msft.currentDate(),
        "earn_loss": round(msft.earnLossConversion(msft.shares_owned, msft.current_price, msft.purchase_price), 2),
        "yearly_yield": round(msft.newYearlyCalc(msft.current_price, msft.purchase_price), 2)
    }

    stocks_dict["rds-a"] = {
        "symbol": rds_a.symbol,
        "shares": rds_a.shares_owned,
        "purchase_price": rds_a.purchase_price,
        "current_price": rds_a.current_price,
        "purchase_date": rds_a.purchase_date,
        "current_date": rds_a.currentDate(),
        "earn_loss": round(rds_a.earnLossConversion(rds_a.shares_owned, rds_a.current_price, rds_a.purchase_price), 2),
        "yearly_yield": round(rds_a.newYearlyCalc(rds_a.current_price, rds_a.purchase_price), 2)
    }

    stocks_dict["aig"] = {
        "symbol": aig.symbol,
        "shares": aig.shares_owned,
        "purchase_price": aig.purchase_price,
        "current_price": aig.current_price,
        "purchase_date": aig.purchase_date,
        "current_date": aig.currentDate(),
        "earn_loss": round(aig.earnLossConversion(aig.shares_owned, aig.current_price, aig.purchase_price), 2),
        "yearly_yield": round(aig.newYearlyCalc(aig.current_price, aig.purchase_price), 2)
    }

    stocks_dict["fb"] = {
        "symbol": fb.symbol,
        "shares": fb.shares_owned,
        "purchase_price": fb.purchase_price,
        "current_price": fb.current_price,
        "purchase_date": fb.purchase_date,
        "current_date": fb.currentDate(),
        "earn_loss": round(fb.earnLossConversion(fb.shares_owned, fb.current_price, fb.purchase_price), 2),
        "yearly_yield": round(fb.newYearlyCalc(fb.current_price, fb.purchase_price), 2)
    }

    stocks_dict["m"] = {
        "symbol": m.symbol,
        "shares": m.shares_owned,
        "purchase_price": m.purchase_price,
        "current_price": m.current_price,
        "purchase_date": m.purchase_date,
        "current_date": m.currentDate(),
        "earn_loss": round(m.earnLossConversion(m.shares_owned, m.current_price, m.purchase_price), 2),
        "yearly_yield": round(m.newYearlyCalc(m.current_price, m.purchase_price), 2)
    }

    stocks_dict["f"] = {
        "symbol": f.symbol,
        "shares": f.shares_owned,
        "purchase_price": f.purchase_price,
        "current_price": f.current_price,
        "purchase_date": f.purchase_date,
        "current_date": f.currentDate(),
        "earn_loss": round(f.earnLossConversion(f.shares_owned, f.current_price, f.purchase_price), 2),
        "yearly_yield": round(f.newYearlyCalc(f.current_price, f.purchase_price), 2)
    }

    stocks_dict["ibm"] = {
        "symbol": ibm.symbol,
        "shares": ibm.shares_owned,
        "purchase_price": ibm.purchase_price,
        "current_price": ibm.current_price,
        "purchase_date": ibm.purchase_date,
        "current_date": ibm.currentDate(),
        "earn_loss": round(ibm.earnLossConversion(ibm.shares_owned, ibm.current_price, ibm.purchase_price), 2),
        "yearly_yield": round(ibm.newYearlyCalc(ibm.current_price, ibm.purchase_price), 2)
    }

    # symbol, shares_owned, purchase_price, current_price, quantity, coupon, yield_amt_pct


    # Outputs a new Line to the console to separate the bash command.
    print("\n\n")

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
        print(key.upper())






    # Testing Space
    """
    # Testing to see if the Bonds Subclass works
    test_bond = Bonds("GT2:GOV", 34, 100.02, 100.05, 200, 1.38, 32)
    print(test_bond.calcCoupon())


    # Testing to make sure Uuid Unique IDs are being used
    print("Bob's User ID is " + user_bob.id)
    print("Eric's User ID is " + E.id)
    """


# Main Function Call
if __name__ == '__main__':
    main()