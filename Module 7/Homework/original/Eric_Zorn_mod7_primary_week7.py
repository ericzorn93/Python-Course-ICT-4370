"""
    Eric Zorn - ICT 4370: Module 7 Databases in Python - 2/5/2018

"""

# Import All from Other Module
import sqlite3
import csv
from Eric_Zorn_mod7_classes_week7 import Investor, Bonds, StockData, buildTable
from Eric_Zorn_mod7_dbconnect_week7 import create_connection, create_db_table, insert_db_data, query_data_db

# ID Header
print("Class Instance IDs\n------------------")

def code_run():
    # Assigns Investor Class Inheritance for the User Bob Smith
    user_bob = Investor("Bob", "Smith", "123 Main Street", "212-342-9046")
    user_steve = Investor("Steve", "Jobs", "1 Infinite Loop", "800-692-7753")

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


    with open('Lesson7_Data_Bonds.csv', 'r') as file:
        info = csv.reader(file)


    # stocks_list = []
    # """
    # stocks_list.append(goog)
    # stocks_list.append(msft)
    # stocks_list.append(rds_a)
    # stocks_list.append(aig)
    # stocks_list.append(fb)
    # stocks_list.append(m)
    # stocks_list.append(f)
    # stocks_list.append(ibm)
    # stocks_list.append(appl)
    # """
    #
    #
    # #################################
    #
    # # Outputs a new Line to the console to separate the bash command.
    # print("\n")
    #
    # # Prints out User information stored in the Bob Variable and calling the Full name attribute
    # # Uses String format concatenation
    # print(
    #     "\n\nBond Information for {0}.\nBob's phone number is {1} and his address is {2}\n-----------------------------"
    #         .format(
    #         user_bob.full_name, user_bob.phone_number, user_bob.address)
    # )
    #
    # # Loop Through titles variable and print out the table headers
    # for title in titles:
    #     print(title, end=' | ')
    #
    # # Print New Line
    # print("\n")
    #
    # # Loop Through Entire Dictionary
    # for key, val in stocks_dict.items():
    #     # print(key.upper())
    #     # Assigns Iterated Values to each new variable declaration for every iteration
    #     symbol = val["symbol"]
    #     shares = val["shares"]
    #     purchase = val["purchase_price"]
    #     current = val["current_price"]
    #     earn_loss = round(val["earn_loss"], 2)
    #     yearly_yield = val["yearly_yield"]
    #     id = val["id"]
    #     purchase_date = "8/1/2018"
    #     final_print = "{0:2d} | {1:6s} | {2:8d} | ${3:<7.2f} | ${4:<6.2f} | ${5:<8.2f} | {6:13s} | {7:18.2f}% | {8:13s} | ".format(
    #         id,
    #         symbol.upper(),
    #         shares,
    #         purchase,
    #         current,
    #         earn_loss,
    #         purchase_date,
    #         yearly_yield,
    #         purchase_date
    #     )
    #
    #     buildTable(final_print)
    #
    # # Print Steve Jobs Stock Information
    # print(
    #     "\n\nStock Information for {0}.\nHis phone number is {1} and his address is {2}\n-----------------------------"
    #         .format(
    #         user_steve.full_name, user_steve.phone_number, user_steve.address)
    # )
    #
    # # Loop Through titles variable and print out the table headers
    # print("{0} | {1} | {2} |".format(titles[1], titles[2], titles[6]))
    # print("{0:6} | {1:8} | {2:13} |".format(apple_dict['appl']["symbol"], apple_dict['appl']["shares"], apple_dict['appl']["purchase_date"]))
    #
    #
    # # Some Error Handling in Stocks Dictionary
    # for key in stocks_dict:
    #     try:
    #         stocks_dict[key]
    #     except KeyError as err:
    #         print('KeyError: stocks_dict has no key', err)
    #
    #
    #
    # # Print Bond Information for Bob Smith
    # print("\n\nBond Information for {0}.\nBob's phone number is {1} and his address is {2}\n---------------------------"
    #     .format(
    #     user_bob.full_name, user_bob.phone_number, user_bob.address)
    # )
    #
    # # List of Bob Smith's Bond Information (Ordered)
    # bob_smith_bond_info = [
    #     bob_smith_bond.symbol,
    #     bob_smith_bond.purchase_price,
    #     bob_smith_bond.current_price,
    #     bob_smith_bond.quantity,
    #     bob_smith_bond.coupon,
    #     bob_smith_bond.yield_amt_pct,
    #     bob_smith_bond.purchase_date
    # ]
    #
    # # Simple Error Checking for Bob_Smith_Bond_Info List
    # try:
    #     for val in bob_smith_bond_info:
    #         if val not in bob_smith_bond_info:
    #             raise ValueError("Value is not in Bob Smith's Stock Information")
    #         else:
    #             pass
    # except ValueError:
    #     print("Value is not in Bob Smith's Stock Information")
    #
    # # Print Bonds Table
    # print("ID: {0}".format(bob_smith_bond.id))
    # print("Symbol: {0}".format(bob_smith_bond.symbol))
    # print("Purchase Price: ${0}".format(bob_smith_bond.purchase_price))
    # print("Current Price: ${0}".format(bob_smith_bond.current_price))
    # print("Quantity: {0}".format(bob_smith_bond.quantity))
    # print("Coupon: {0}".format(bob_smith_bond.coupon))
    # print("Yield: {0}%".format(bob_smith_bond.yield_amt_pct))
    # print("Purchase Date: {0}".format(bob_smith_bond.purchase_date))
    # bob_smith_bond.readValues()
    #
    #
    # print("\n")










    """ Database Connections Using SQLite3"""

    # Connect to Database and Create Tables
    databaseConn = "stock_info.db"
    conn = create_connection(databaseConn)


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



    """
    create_db_table(conn, create_investor_table)
    create_db_table(conn, create_stock_table)
    create_db_table(conn, create_bond_table)
    """

    """
    # Insert User 1
    user_bob_db_insert = "INSERT INTO investors VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
        user_bob.id,
        user_bob.first_name,
        user_bob.last_name,
        user_bob.full_name,
        user_bob.address,
        user_bob.phone_number
    )

    # Insert User 2
    user_steve_db_insert = "INSERT INTO investors VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
        user_steve.id,
        user_steve.first_name,
        user_steve.last_name,
        user_steve.full_name,
        user_steve.address,
        user_steve.phone_number
    )

    conn = sqlite3.connect(databaseConn)
    cursor = conn.cursor()
    
    """

    """
    # Database Execution for Investors
    # cursor.execute(user_bob_db_insert)
    # cursor.execute(user_steve_db_insert)
    """


    # Database Insertion for Bonds from User Bob Smith
    # user_steve__bonds__insert = "INSERT INTO bonds VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(
    #     bob_smith_bond.id,
    #     bob_smith_bond.quantity,
    #     bob_smith_bond.shares_owned,
    #     bob_smith_bond.coupon,
    #     bob_smith_bond.yield_amt_pct
    # )

    # Insert Bonds Data
    # insert_db_data(conn, user_steve__bonds__insert)


    # Stock Inserts
    # goog_insert = "INSERT INTO stocks VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
    #     goog.id,
    #     goog.symbol,
    #     goog.shares_owned,
    #     goog.purchase_price,
    #     goog.current_price,
    #     goog.purchase_date
    # )
    #
    # msft_insert = "INSERT INTO stocks VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
    #     msft.id,
    #     msft.symbol,
    #     msft.shares_owned,
    #     msft.purchase_price,
    #     msft.current_price,
    #     msft.purchase_date
    # )
    #
    # rds_a_insert = "INSERT INTO stocks VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
    #     rds_a.id,
    #     rds_a.symbol,
    #     rds_a.shares_owned,
    #     rds_a.purchase_price,
    #     rds_a.current_price,
    #     rds_a.purchase_date
    # )
    #
    # aig_insert = "INSERT INTO stocks VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
    #     aig.id,
    #     aig.symbol,
    #     aig.shares_owned,
    #     aig.purchase_price,
    #     aig.current_price,
    #     aig.purchase_date
    # )
    #
    # fb_insert = "INSERT INTO stocks VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
    #     fb.id,
    #     fb.symbol,
    #     fb.shares_owned,
    #     fb.purchase_price,
    #     fb.current_price,
    #     fb.purchase_date
    # )
    #
    # m_insert = "INSERT INTO stocks VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
    #     m.id,
    #     m.symbol,
    #     m.shares_owned,
    #     m.purchase_price,
    #     m.current_price,
    #     m.purchase_date
    # )

    # Insert Stock Data
    """
    for val in stocks_list:
        try:
            insert_data = "INSERT INTO stocks VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
                val.id,
                val.symbol,
                val.shares_owned,
                val.purchase_price,
                val.current_price,
                val.purchase_date
            )
            insert_db_data(conn, insert_data)
        except IndexError:
            pass # Simple Error Handling
    """



    file_name = 'stocks_information.txt'
    with open(file_name, 'w') as file:
        # Assigns Investor Class Inheritance for the User Bob Smith
        user_bob = Investor("Bob", "Smith", "123 Main Street", "212-342-9046")
        user_steve = Investor("Steve", "Jobs", "1 Infinite Loop", "800-692-7753")

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

        # Stock Query
        query_stocks = "SELECT * FROM stocks"
        stocks_data = query_data_db(conn, query_stocks)

        goog = StockData(stocks_data[0][1], stocks_data[0][2], stocks_data[0][3], stocks_data[0][4])
        msft = StockData(stocks_data[1][1], stocks_data[1][2], stocks_data[1][3], stocks_data[1][4])
        rds_a = StockData(stocks_data[2][1], stocks_data[2][2], stocks_data[2][3], stocks_data[2][4])
        aig = StockData(stocks_data[3][1], stocks_data[3][2], stocks_data[3][3], stocks_data[3][4])
        fb = StockData(stocks_data[4][1], stocks_data[4][2], stocks_data[4][3], stocks_data[4][4])
        m = StockData(stocks_data[5][1], stocks_data[5][2], stocks_data[5][3], stocks_data[5][4])
        f = StockData(stocks_data[6][1], stocks_data[6][2], stocks_data[6][3], stocks_data[6][4])
        ibm = StockData(stocks_data[7][1], stocks_data[7][2], stocks_data[7][3], stocks_data[7][4])
        appl = StockData(stocks_data[8][1], stocks_data[8][2], stocks_data[8][3], stocks_data[8][4])

        stocks = [goog, msft, rds_a, aig, fb, m, f, ibm, appl]

        conn = sqlite3.connect('stock_info.db')
        cursor = conn.cursor()

        """
        for stock in stocks:
            query = "INSERT INTO stocks VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
                stock.id,
                stock.symbol,
                stock.shares_owned,
                stock.purchase_price,
                stock.current_price,
                stock.purchase_date
            )
            # Error Handling
            try:
                cursor.execute(query)
                conn.commit()
            except sqlite3.OperationalError:
                print("This query has already been completed")
        """


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
                "earn_loss": round(goog.earnLossConversion(goog.shares_owned, goog.current_price, goog.purchase_price),
                                   2),
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
                "earn_loss": round(msft.earnLossConversion(msft.shares_owned, msft.current_price, msft.purchase_price),
                                   2),
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
                "earn_loss": round(
                    rds_a.earnLossConversion(rds_a.shares_owned, rds_a.current_price, rds_a.purchase_price), 2),
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

        # Declaring Apple Dictionary
        apple_dict = {}

        apple_dict["appl"] = {
                "symbol": appl.symbol,
                "shares": appl.shares_owned,
                "purchase_price": appl.purchase_price,
                "current_price": appl.current_price,
                "purchase_date": appl.purchase_date,
                "current_date": appl.currentDate(),
                "earn_loss": round(appl.earnLossConversion(appl.shares_owned, appl.current_price, appl.purchase_price),
                                   2),
                "yearly_yield": round(appl.newYearlyCalc(appl.current_price, appl.purchase_price), 2),
                "id": appl.id
            }


        retrieve_query = "SELECT * FROM stocks"
        retrieval = cursor.execute(retrieve_query)
        final_list = retrieval.fetchall()

        # Build Table from Database Retrieval
        file.write("Stock Information for {0}\n------------------\n\n".format(user_bob.full_name))
        # Print Titles
        for title in titles:
            file.write("{0:12} | ".format(title))

        file.write("\n\n")

        # Attempt to Print Table
        for val in stocks_dict.values():
            try:
                final_print = "{0:2d} | {1:6s} | {2:8d} | ${3:<7.2f} | ${4:<6.2f} | ${5:<8.2f} | {6:13s} | {7:18.2f}% | {8:13s} | ".format(
                        val["id"],
                        val["symbol"],
                        val["shares"],
                        val["purchase_price"],
                        val["current_price"],
                        val["purchase_date"],
                        val["current_date"],
                        val["earn_loss"],
                        val["yearly_yield"]
                    )

                file.write(final_print)
            except ValueError:
                print("Unknown format of value to be written to stocks_information.txt file")







# Main Function
def main():
    code_run()




# Main Function Call
if __name__ == '__main__':
    main()