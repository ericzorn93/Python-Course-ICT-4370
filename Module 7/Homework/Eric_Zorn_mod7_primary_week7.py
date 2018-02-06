"""
    Eric Zorn - ICT 4370: Module 7 Databases in Python - 2/5/2018

"""

# Import All from Other Module
from Eric_Zorn_mod7_classes_week7 import Investor, Bonds, StockData, buildTable
from Eric_Zorn_mod7_dbconnect_week7 import create_connection, create_db_table, insert_db_data

# ID Header
print("Class Instance IDs\n------------------")

def code_run():
    # Assigns Investor Class Inheritance for the User Bob Smith
    user_bob = Investor("Bob", "Smith", "123 Main Street", "212-342-9046")
    steve_jobs = Investor("Steve", "Jobs", "1 Infinite Loop", "800-692-7753")

    # Assigns User Bonds for Bob Smith
    bob_smith_bond = Bonds("GT2:GOV", 100.02, 100.05, 200, 1.38, 1.35)

    # Table Titles
    titles = (
        "ID",
        "Symbol",
        "# Shares",
        "Purchase",
        "Current",
        "Earn/Loss",
        "Purchase Date",
        "Yearly Earning/Loss",
        "Purchase Date"
    )

    # Assigning Variables to inherit from the Stock Data Class
    goog = StockData("GOOG", 125, 772.88, 941.53)
    msft = StockData("MSFT", 85, 56.60, 73.04)
    rds_a = StockData("RDS-A", 400, 49.58, 55.74)
    aig = StockData("AIG", 235, 54.21, 65.27)
    fb = StockData("FB", 150, 124.31, 172.45)
    m = StockData("m", 425, 30.30, 23.98)
    f = StockData("f", 85, 12.58, 10.95)
    ibm = StockData("IBM", 80, 150.37, 145.30)
    appl = StockData("APPL", 1000, 145000.0, 1170.91)

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

    apple_dict = {}

    apple_dict["appl"] = {
        "symbol": appl.symbol,
        "shares": appl.shares_owned,
        "purchase_price": appl.purchase_price,
        "current_price": appl.current_price,
        "purchase_date": appl.purchase_date,
        "current_date": appl.currentDate(),
        "earn_loss": round(appl.earnLossConversion(appl.shares_owned, appl.current_price, appl.purchase_price), 2),
        "yearly_yield": round(appl.newYearlyCalc(appl.current_price, appl.purchase_price), 2),
        "id": appl.id
    }

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
            steve_jobs.full_name, steve_jobs.phone_number, steve_jobs.address)
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





    # Connect to Database
    database = "stock_info.db"
    create_investor_table = """
       CREATE TABLE
       IF NOT EXISTS investors (
          id integer PRIMARY KEY,
          first_name TEXT NOT NULL,
          last_name TEXT NOT NULL,
          full_name TEXT NOT NULL,
          address TEXT NOT NULL,
          phone_number TEXT NOT NULL
);
    """

    create_stock_table = """
           CREATE TABLE
           IF NOT EXISTS stocks (
              id integer PRIMARY KEY,
              symbol TEXT NOT NULL,
              shares INTEGER NOT NULL,
              purchase REAL NOT NULL,
              current REAL NOT NULL,
              purchase_date TEXT NOT NULL
    );
        """

    create_bond_table = """
               CREATE TABLE
               IF NOT EXISTS bonds (
                  id integer PRIMARY KEY,
                  quantity INTEGER NOT NULL,
                  shares INTEGER NOT NULL,
                  coupon REAL NOT NULL,
                  yield REAL NOT NULL
        );
            """



    # Create the Database Connection and Three Database Tables
    conn = create_connection(database)
    create_db_table(conn, create_investor_table)
    create_db_table(conn, create_stock_table)
    create_db_table(conn, create_bond_table)

    # Insert user 1
    user_bob_db_insert = "INSERT INTO investors VALUES({0}, {1}, {2}, {3}, {4}, {5})".format(
        user_bob.id,
        user_bob.first_name,
        user_bob.last_name,
        user_bob.full_name,
        user_bob.address,
        user_bob.phone_number
    )

    insert_db_data(conn, user_bob_db_insert)


# Main Function
def main():
    code_run()




# Main Function Call
if __name__ == '__main__':
    main()