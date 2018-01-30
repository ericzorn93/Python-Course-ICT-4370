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

    # Working With Opening Files and Writing Files
    with open('Lesson6_Data_Stocks.csv', 'r') as rf:
        reader = csv.reader(rf)
        rows = []
        titles = []


        for row in reader:
           rows.append(row)

        # Pulling in Values from CSV Document
        goog = StockData(rows[1][0], int(rows[1][1]), float(rows[1][2]), float(rows[1][3]))
        msft = StockData(rows[2][0], int(rows[2][1]), float(rows[2][2]), float(rows[2][3]))
        rds_a = StockData(rows[3][0], int(rows[3][1]), float(rows[3][2]), float(rows[3][3]))
        aig = StockData(rows[4][0], int(rows[4][1]), float(rows[4][2]), float(rows[4][3]))
        fb = StockData(rows[5][0], int(rows[5][1]), float(rows[5][2]), float(rows[5][3]))
        m = StockData(rows[6][0], int(rows[6][1]), float(rows[6][2]), float(rows[6][3]))
        f = StockData(rows[7][0], int(rows[7][1]), float(rows[7][2]), float(rows[7][3]))
        ibm = StockData(rows[8][0], int(rows[8][1]), float(rows[8][2]), float(rows[8][3]))

        # Appending to Titles List
        titles.append(rows[0])

        # Stocks Dict Declaration
        stocks_dict = {}

        # Stocks Dict Assignments
        stocks_dict["goog"] = {
            "symbol": goog.symbol,
            "shares": goog.shares_owned,
            "purchase": goog.purchase_price,
            "current": goog.current_price,
            "current_date": goog.currentDate(),
            "earn_loss": round(goog.earnLossConversion(goog.shares_owned, goog.current_price, goog.purchase_price), 2),
            "yearly_yield": round(goog.newYearlyCalc(goog.current_price, goog.purchase_price), 2)
        }

        stocks_dict["msft"] = {
            "symbol": msft.symbol,
            "shares": msft.shares_owned,
            "purchase": msft.purchase_price,
            "current": msft.current_price,
            "current_date": msft.currentDate(),
            "earn_loss": round(msft.earnLossConversion(msft.shares_owned, msft.current_price, msft.purchase_price), 2),
            "yearly_yield": round(msft.newYearlyCalc(msft.current_price, msft.purchase_price), 2)
        }

        stocks_dict["rds-a"] = {
            "symbol": rds_a.symbol,
            "shares": rds_a.shares_owned,
            "purchase": rds_a.purchase_price,
            "current": rds_a.current_price,
            "current_date": rds_a.currentDate(),
            "earn_loss": round(rds_a.earnLossConversion(rds_a.shares_owned, rds_a.current_price, rds_a.purchase_price), 2),
            "yearly_yield": round(rds_a.newYearlyCalc(rds_a.current_price, rds_a.purchase_price), 2)
        }

        stocks_dict["aig"] = {
            "symbol": aig.symbol,
            "shares": aig.shares_owned,
            "purchase": aig.purchase_price,
            "current": aig.current_price,
            "current_date": aig.currentDate(),
            "earn_loss": round(aig.earnLossConversion(aig.shares_owned, aig.current_price, aig.purchase_price), 2),
            "yearly_yield": round(aig.newYearlyCalc(aig.current_price, aig.purchase_price), 2)
        }

        stocks_dict["fb"] = {
            "symbol": fb.symbol,
            "shares": fb.shares_owned,
            "purchase": fb.purchase_price,
            "current": fb.current_price,
            "current_date": fb.currentDate(),
            "earn_loss": round(fb.earnLossConversion(fb.shares_owned, fb.current_price, fb.purchase_price), 2),
            "yearly_yield": round(fb.newYearlyCalc(fb.current_price, fb.purchase_price), 2)
        }

        stocks_dict["m"] = {
            "symbol": m.symbol,
            "shares": m.shares_owned,
            "purchase": m.purchase_price,
            "current": m.current_price,
            "current_date": m.currentDate(),
            "earn_loss": round(m.earnLossConversion(m.shares_owned, m.current_price, m.purchase_price), 2),
            "yearly_yield": round(m.newYearlyCalc(m.current_price, m.purchase_price), 2)
        }

        stocks_dict["f"] = {
            "symbol": f.symbol,
            "shares": f.shares_owned,
            "purchase": f.purchase_price,
            "current": f.current_price,
            "current_date": f.currentDate(),
            "earn_loss": round(f.earnLossConversion(f.shares_owned, f.current_price, f.purchase_price), 2),
            "yearly_yield": round(f.newYearlyCalc(f.current_price, f.purchase_price), 2)
        }

        stocks_dict["ibm"] = {
            "symbol": ibm.symbol,
            "shares": ibm.shares_owned,
            "purchase": ibm.purchase_price,
            "current": ibm.current_price,
            "current_date": ibm.currentDate(),
            "earn_loss": round(ibm.earnLossConversion(ibm.shares_owned, ibm.current_price, ibm.purchase_price), 2),
            "yearly_yield": round(ibm.newYearlyCalc(ibm.current_price, ibm.purchase_price), 2)
        }



        with open('mod6_output.txt', 'w') as wf:
            wf.write("Stock Portfolio Information for {0}\n-----------------------\n".format(user_bob.full_name))

            for title in titles[0]:
                wf.write("{0:5} | ".format(title))

            # Build Stock Tables
            wf.write("\n")
            for val in stocks_dict.values():
                wf.write("\n{0:5} |  {1:9} |  ${2:12} |  ${3:11} |  {4:12} |  ${5:14} |  {6:6} | ".format(
                    val["symbol"],
                    val["shares"],
                    val["purchase"],
                    val["current"],
                    val["current_date"],
                    val["earn_loss"],
                    val["yearly_yield"]
                ))




        # Close Reading File
        rf.close()


    # Bonds Read In Information
    with open('Lesson6_Data_Bonds.csv', 'r') as bond_rf:
        bond_reader = csv.reader(bond_rf)
        bond_info = []

        for line in bond_reader:
            bond_info.append(line)

        # Building Bob Smith Bond
        bob_smith_bond = Bonds(
            bond_info[1][0],
            float(bond_info[1][2]),
            float(bond_info[1][3]),
            int(bond_info[1][1]),
            float(bond_info[1][5]),
            float(bond_info[1][6]),
        )

        # Write Bonds Info
        with open("mod6_output.txt", "a") as bond_wf:
            bond_wf.write("\n\n\n\n")
            bond_wf.write("Bonds Information for {0}\n--------------------------".format(user_bob.full_name))
            bond_wf.write("\nID: {0}".format(bob_smith_bond.id))
            bond_wf.write("\nSymbol: {0}".format(bob_smith_bond.symbol))
            bond_wf.write("\nPurchase Price: ${0}".format(bob_smith_bond.purchase_price))
            bond_wf.write("\nCurrent Price: ${0}".format(bob_smith_bond.current_price))
            bond_wf.write("\nQuantity: {0}".format(bob_smith_bond.quantity))
            bond_wf.write("\nCoupon: {0}".format(bob_smith_bond.coupon))
            bond_wf.write("\nYield: {0}%".format(bob_smith_bond.yield_amt_pct))
            bond_wf.write("\nPurchase Date: {0}".format(bob_smith_bond.purchase_date))

        # Close Bond Reading File
        bond_rf.close()

# Main Function
def main():
    code_run()

# Main Function Call
if __name__ == '__main__':
    main()