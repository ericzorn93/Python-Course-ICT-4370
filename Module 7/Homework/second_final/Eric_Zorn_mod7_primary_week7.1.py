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

def create_tables(conn):
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
    try:
        create_db_table(conn, create_investor_table)
        create_db_table(conn, create_stock_table)
        create_db_table(conn, create_bond_table)
    except Exception as err:
        print('55 ERROR during create_db_table:', err)
    
def insert_user(u, cursor):
    user_bob_db_insert = "INSERT INTO investors VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
        u.id,
        u.first_name,
        u.last_name,
        u.full_name,
        u.address,
        u.phone_number
        )
    cursor.execute(user_bob_db_insert)
    
def read_csv_to_classes():

    with open('Lesson7_Data_Stocks.csv', 'r') as rf:
        reader = csv.reader(rf)
        rows = []

        for row in reader:
           rows.append(row)
    
        # Pulling in Values from CSV Document
        # goog = StockData(rows[1][0], int(rows[1][1]), float(rows[1][2]), float(rows[1][3]))
        # msft = StockData(rows[2][0], int(rows[2][1]), float(rows[2][2]), float(rows[2][3]))
        # rds_a = StockData(rows[3][0], int(rows[3][1]), float(rows[3][2]), float(rows[3][3]))
        # aig = StockData(rows[4][0], int(rows[4][1]), float(rows[4][2]), float(rows[4][3]))
        # fb = StockData(rows[5][0], int(rows[5][1]), float(rows[5][2]), float(rows[5][3]))
        # m = StockData(rows[6][0], int(rows[6][1]), float(rows[6][2]), float(rows[6][3]))
        # f = StockData(rows[7][0], int(rows[7][1]), float(rows[7][2]), float(rows[7][3]))
        # ibm = StockData(rows[8][0], int(rows[8][1]), float(rows[8][2]), float(rows[8][3]))
        
    stock_classes = []
    for row in rows[1:]:
        stock = StockData(row[0], int(row[1]), float(row[2]), float(row[3]))
        stock_classes.append(stock)
    return stock_classes
    
        
def write_classes_to_db(stock_classes):
    # Assigns Investor Class Inheritance for the User Bob Smith
    user_bob = Investor("Bob", "Smith", "123 Main Street", "212-342-9046")
    user_steve = Investor("Steve", "Jobs", "1 Infinite Loop", "800-692-7753")
    
    # Connect to Database and Create Tables
    databaseConn = "stock_info_2.db"
    conn = create_connection(databaseConn)
    cursor = conn.cursor()

    # moved create tables lines
    create_tables(conn)
    
    try:
        # Insert User 1
        insert_user(user_bob, cursor)

        # Insert User 2
        insert_user(user_steve, cursor)
        
    except Exception as err:
        print('112  ERROR inserting user:', err)


    # Insert Stock Data
    try:
        for val in stock_classes:
            try:
                insert_data = "INSERT INTO stocks VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{5}')".format(
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
    except Exception as err:
        print("212  ERROR:  Stocks List has already been defined:", err)
    conn.close()

def code_run():
    # # Assigns Investor Class Inheritance for the User Bob Smith
    # user_bob = Investor("Bob", "Smith", "123 Main Street", "212-342-9046")
    # user_steve = Investor("Steve", "Jobs", "1 Infinite Loop", "800-692-7753")

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
        "Yearly Earning/Loss"
    )



        # Code from Additional.py can be added here if needed

    """ Database Connections Using SQLite3"""

    ##  moved to function
    # Connect to Database and Create Tables
    # databaseConn = "stock_info.db"
    # conn = create_connection(databaseConn)
    # cursor = conn.cursor()

    # # moved create tables lines
    # create_tables(conn)
    
    # try:
    #     # Insert User 1
    #     insert_user(user_bob, cursor)

    #     # Insert User 2
    #     insert_user(user_steve, cursor)
        
    # except Exception as err:
    #     print('112  ERROR inserting user:', err)

    # Attempt Database Investor Important
    # try:
    #     # Database Execution for Investors
    #     cursor.execute(user_bob_db_insert)
    #     cursor.execute(user_steve_db_insert)
    # except:
    #     pass



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


        # Stock Inserts
        # goog_insert = "INSERT INTO stocks VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
        #     goog.id,
        #     goog.symbol,
        #     goog.shares_owned,
        #     goog.purchase_price,
        #     goog.current_price,
        #     goog.purchase_date
        # )

        # msft_insert = "INSERT INTO stocks VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
        #     msft.id,
        #     msft.symbol,
        #     msft.shares_owned,
        #     msft.purchase_price,
        #     msft.current_price,
        #     msft.purchase_date
        # )

        # rds_a_insert = "INSERT INTO stocks VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
        #     rds_a.id,
        #     rds_a.symbol,
        #     rds_a.shares_owned,
        #     rds_a.purchase_price,
        #     rds_a.current_price,
        #     rds_a.purchase_date
        # )

        # aig_insert = "INSERT INTO stocks VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
        #     aig.id,
        #     aig.symbol,
        #     aig.shares_owned,
        #     aig.purchase_price,
        #     aig.current_price,
        #     aig.purchase_date
        # )

        # fb_insert = "INSERT INTO stocks VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
        #     fb.id,
        #     fb.symbol,
        #     fb.shares_owned,
        #     fb.purchase_price,
        #     fb.current_price,
        #     fb.purchase_date
        # )

        # m_insert = "INSERT INTO stocks VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
        #     m.id,
        #     m.symbol,
        #     m.shares_owned,
        #     m.purchase_price,
        #     m.current_price,
        #     m.purchase_date
        # )
    except UnboundLocalError as err:
        print("{0}".format(err))


    ##   moved to function
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
                conn = sqlite3.connect("stock_info_2_db")
                insert_db_data(conn, insert_data)
            except IndexError:
                pass # Simple Error Handling
    except Exception as err:
        print("212  ERROR:  Stocks List has already been defined:", err)



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
            "Annual Yield"
        )

        # Stock Query
        query_stocks = "SELECT * FROM stocks"
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

        # Stocks List
        stocks = [goog, msft, rds_a, aig, fb, m, f, ibm, appl]

        conn = sqlite3.connect('stock_info.db')
        cursor = conn.cursor()

        # Error handling for Stock Query
        try:
            # with this code which uses the __iter__ method in the stock class
            for stock in stocks:
                # the *stock term returns stock class fields using the StockData __iter__ method
                query = "INSERT INTO stocks VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(*stock)
                # Error Handling
                try:
                    cursor.execute(query)
                    conn.commit()
                except sqlite3.OperationalError:
                    print("This query has already been completed")
        except Error as err:
            print(err, "Unique Constraint has failed")



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
        conn.commit()
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
                apple_dict["appl"]["yearly_yield"],
            ))
        except ValueError as e:
            print(e)


# Main Function
def main():
    stock_classes = read_csv_to_classes()
    print('517  first stock class')
    print(stock_classes[0])
    
    write_classes_to_db(stock_classes)
    # code_run()


# Main Function Call
if __name__ == '__main__':
    main()