"""
    Eric Zorn - ICT 4370: Module 7 Databases in Python - 2/5/2018

"""

# Import All from Other Module
import sqlite3
import csv
from Eric_Zorn_mod7_classes_week7 import Investor, Bonds, StockData
from Eric_Zorn_mod7_dbconnect_week7 import create_connection, create_db_table, insert_db_data, query_data_db

# ID Header
print("Class Instance IDs\n------------------")

def code_run():
    # Assigns Investor Class Inheritance for the User Bob Smith
    user_bob = Investor("Bob", "Smith", "123 Main Street", "212-342-9046")
    user_steve = Investor("Steve", "Jobs", "1 Infinite Loop", "800-692-7753")

    # Assigns User Bonds for Bob Smith
    bob_smith_bond = Bonds("GT2:GOV", 100.02, 100.05, 200, 1.38, 1.35)


    with open('Lesson7_Data_Bonds.csv', 'r') as file:
        info = csv.reader(file)

        # Code from Additional.py can be added here if needed

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

    # Database Connections
    try:
        create_db_table(conn, create_investor_table)
        create_db_table(conn, create_stock_table)
        create_db_table(conn, create_bond_table)


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
    except:
        print("Error with creating insert statements")

    # Attempt Database Investor Important
    try:
        # Database Execution for Investors
        conn = sqlite3.connect(databaseConn)
        insert_db_data(conn, user_bob_db_insert)
        insert_db_data(conn, user_steve_db_insert)
    except:
        print("Error inserting data into the database")



    # Database Insertion for Bonds from User Bob Smith
    try:
        user_steve__bonds__insert = "INSERT INTO bonds VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(
            bob_smith_bond.id,
            bob_smith_bond.quantity,
            bob_smith_bond.shares_owned,
            bob_smith_bond.coupon,
            bob_smith_bond.yield_amt_pct
        )

        # Insert Bonds Data
        insert_db_data(conn, user_steve__bonds__insert)
    except UnboundLocalError as err:
        print("125" + err)


    # Insert Stock Data
    try:
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
    except NameError as err:
        # print("{0} has already been defined".format(err))
        pass

    file_name = 'stocks_information.txt'
    with open(file_name, 'w') as file:
        # Assigns Investor Class Inheritance for the User Bob Smith
        user_bob = Investor("Bob", "Smith", "123 Main Street", "212-342-9046")
        user_steve = Investor("Steve", "Jobs", "1 Infinite Loop", "800-692-7753")

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
            "Annual Yield"
        )

        # Stock Query
        query_stocks = "SELECT * FROM stocks"
        conn = sqlite3.connect('stock_info.db')
        stocks_data = query_data_db(conn, query_stocks)

        goog = StockData(stocks_data[0][1], stocks_data[0][2], stocks_data[0][3], stocks_data[0][4], id=stocks_data[0][0])
        msft = StockData(stocks_data[1][1], stocks_data[1][2], stocks_data[1][3], stocks_data[1][4], id=stocks_data[1][0])
        rds_a = StockData(stocks_data[2][1], stocks_data[2][2], stocks_data[2][3], stocks_data[2][4], id=stocks_data[2][0])
        aig = StockData(stocks_data[3][1], stocks_data[3][2], stocks_data[3][3], stocks_data[3][4], id=stocks_data[3][0])
        fb = StockData(stocks_data[4][1], stocks_data[4][2], stocks_data[4][3], stocks_data[4][4], id=stocks_data[4][0])
        m = StockData(stocks_data[5][1], stocks_data[5][2], stocks_data[5][3], stocks_data[5][4], id=stocks_data[5][0])
        f = StockData(stocks_data[6][1], stocks_data[6][2], stocks_data[6][3], stocks_data[6][4], id=stocks_data[6][0])
        ibm = StockData(stocks_data[7][1], stocks_data[7][2], stocks_data[7][3], stocks_data[7][4], id=stocks_data[7][0])
        appl = StockData(stocks_data[8][1], stocks_data[8][2], stocks_data[8][3], stocks_data[8][4], id=stocks_data[8][0])

        stocks = [goog, msft, rds_a, aig, fb, m, f, ibm, appl]
        cursor = conn.cursor()

        # Error handling for Stock Query
        try:
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

        except sqlite3.IntegrityError as err:
            # print("210: The query has already been completed")
            pass



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


        # Build Table from Database Retrieval
        file.write("Stock Information for {0}\n------------------\n\n".format(user_bob.full_name))
        # Print Titles
        for title in titles:
            file.write("{0:12} | ".format(title))

        file.write("\n\n")

        # Attempt to Print Table
        for val in stocks_dict.values():
            try:
                final_print = "{0:12d} | {1:12s} | {2:12d} | ${3:<11.2f} | ${4:<11.2f} | ${5:11s} | {6:13s} | ${7:18.2f} | {8:11.2f}% | \n".format(
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



    # Assign Bond Information
    with open('Lesson7_Data_Bonds.csv', 'r') as bonds_file_csv:
        # Assigns User Bonds for Bob Smith
        reader = csv.reader(bonds_file_csv)
        bond_list = list(reader)
        bob_smith_bond = Bonds(bond_list[1][0], bond_list[1][2], bond_list[1][3], bond_list[1][4], bond_list[1][5], bond_list[1][6])

    with open('stocks_information.txt', 'a') as open_file:
        try:
            open_file.write("\n\n")
            open_file.write("{0}'s Bond Information\n----------------------\n".format(user_bob.full_name))
            open_file.write(
                "ID: {0}\nSymbol: {1}\nPurchase Price: ${2}\nCurrent Price: ${3}\nQuantity: {4}\nCoupon: {5}\nYield: {6}%\nPurchase Date: {7}".format(
                    bob_smith_bond.id,
                    bob_smith_bond.symbol,
                    bob_smith_bond.purchase_price,
                    bob_smith_bond.current_price,
                    bob_smith_bond.quantity,
                    bob_smith_bond.coupon,
                    bob_smith_bond.yield_amt_pct,
                    bob_smith_bond.purchase_date
                )
            )

            # Write New Line
            open_file.write("\n\n\n")

            open_file.write("Stock Information for {0}.\n---------------------\n\n".format(user_steve.full_name))

            # Print Titles Again
            for title in titles:
                open_file.write("{0:12} | ".format(title))

            # Write New Line
            open_file.write("\n\n")
            # Write Steve Jobs Stock Information
            open_file.write("{0:12d} | {1:12s} | {2:12d} | {3:1f} | {4:2f} | {5:2s} | {6:10s} | {7:24f} | {8}".format(
                apple_dict["appl"]["id"],
                apple_dict["appl"]["symbol"],
                apple_dict["appl"]["shares"],
                apple_dict["appl"]["purchase_price"],
                apple_dict["appl"]["current_price"],
                apple_dict["appl"]["purchase_date"],
                apple_dict["appl"]["current_date"],
                apple_dict["appl"]["earn_loss"],
                apple_dict["appl"]["earn_loss"],
                apple_dict["appl"]["yearly_yield"],
            ))
        except ValueError as err:
            print(err)


# Main Function
def main():
    code_run()


# Main Function Call
if __name__ == '__main__':
    main()