"""
    Eric Zorn - ICT 4370 - 1/24/2018

    This assignment is from Module 4 and build upon the last assignment that we had completed from Module 3.
    We have taken the functions that we had written and exported them to an external module to then be able to import.
    Once the functions from the external module have been imported, I have built a table off of the proper information.
"""

# Imports from DateTime Module and External Custom Module of Functions
import datetime as dt
from Eric_Zorn_function_imports_mod4_week4 import earnLossConversion, newYearlyCalc, buildTable


# Defining Main Function
def main():
    # Purchase Date Variable Declaration
    purchase_date = "8/1/2015"

    # Current Date Variable Declaration and formatted properly to the current date variable
    now = dt.datetime.now()
    current_date = now.strftime('%m/%d/%Y').strip()



    # Declaring Stock Dict and then assigning keys and values (Nested Dictionary)
    stocks_dict = {}

    stocks_dict["google"] = {
        "symbol": "GOOG",
        "shares": 125,
        "purchase_price": 772.88,
        "current_price": 941.53,
        "purchase_date": purchase_date,
        "current_date": current_date,
    }

    stocks_dict["microsoft"] = {
        "symbol": "MSFT",
        "shares": 85,
        "purchase_price": 56.60,
        "current_price": 73.04,
        "purchase_date": purchase_date,
        "current_date": current_date
    }

    stocks_dict["rds-a"] = {
        "symbol": "RDS-A",
        "shares": 400,
        "purchase_price": 49.58,
        "current_price": 55.74,
        "purchase_date": purchase_date,
        "current_date": current_date
    }

    stocks_dict["aig"] = {
        "symbol": "AIG",
        "shares": 235,
        "purchase_price": 54.21,
        "current_price": 65.27,
        "purchase_date": purchase_date,
        "current_date": current_date
    }

    stocks_dict["fb"] = {
        "symbol": "FB",
        "shares": 150,
        "purchase_price": 124.31,
        "current_price": 172.45,
        "purchase_date": purchase_date,
        "current_date": current_date
    }

    stocks_dict["m"] = {
        "symbol": "m",
        "shares": 425,
        "purchase_price": 30.30,
        "current_price": 23.98,
        "purchase_date": purchase_date,
        "current_date": current_date
    }

    stocks_dict["f"] = {
        "symbol": "f",
        "shares": 85,
        "purchase_price": 12.58,
        "current_price": 10.95,
        "purchase_date": purchase_date,
        "current_date": current_date
    }

    stocks_dict["ibm"] = {
        "symbol": "ibm",
        "shares": 80,
        "purchase_price": 150.37,
        "current_price": 145.30,
        "purchase_date": purchase_date,
        "current_date": current_date
    }

    titles = [
        "Symbol",
        "# Shares",
        "Purchase",
        "Current",
        "Earn/Loss",
        "Purchase Date",
        "Yearly Yield"
    ]

    """
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
        "num_one": 125,
        "num_two": 85,
        "num_three": 400,
        "num_four": 235,
        "num_five": 150,
        "num_six": 425,
        "num_seven": 85,
        "num_eight": 80
    }

    purchase_prices = {
        "num_one": 772.88,
        "num_two": 56.60,
        "num_three": 49.58,
        "num_four": 54.21,
        "num_five": 124.31,
        "num_six": 30.30,
        "num_seven": 12.58,
        "num_eight": 150.37
    }

    current_prices = {
        "num_one": 941.53,
        "num_two": 73.04,
        "num_three": 55.74,
        "num_four": 65.27,
        "num_five": 172.45,
        "num_six": 23.98,
        "num_seven": 10.95,
        "num_eight": 145.30
    }
    """


    # Converting User Input for Name into title case. Stripped extra white space from both sides of the string
    ##name = input("What is your full name? ").title().strip()
    name = 'Bob Smith'


    # Print a formatted string for the full name from user input
    print("Stock Portfolio Information for {0}\n".format(name))

    # Loop through and print table titles (headers)
    for title in titles:
        #print("", end=' | ')
        print("{:13s}".format(title), end=' | ')
    

    # Print Blank Line Separator
    print("\n")

    # Iterate through stocks_dict items and assign new keys with the proper values
    for key, val in stocks_dict.items():
        # Assigns Earn Loss Values from calling the earnLossConversion Function
        val["earn_loss"] = earnLossConversion(
        stocks_dict[key]["shares"],
        stocks_dict[key]["current_price"],
        stocks_dict[key]["purchase_price"]
        )

        # Assigns the yearly_yield value with the newYearlyCalc() function and rounded 2 decimal places
        val["yearly_yield"] = round(newYearlyCalc(
            stocks_dict[key]["current_price"],
            stocks_dict[key]["purchase_price"]
        ), 2)

        # print(val)

        # Assigns Iterated Values to each new variable declaration for every iteration
        symbol = val["symbol"]
        shares = val["shares"]
        purchase = val["purchase_price"]
        current = val["current_price"]
        earn_loss = round(val["earn_loss"], 2)
        purchase_date = purchase_date
        yearly_yield = val["yearly_yield"]

        # print(symbol, " | ", shares, " | ", purchase, " | ", current)

        # Final Printed String using the format() method for each value
        final_print = "{0:13s} | {1:13d} | ${2:<12.2f} | ${3:<12.2f} | ${4:<12.2f} | {5:13s} | {6:12.2f}%".format(
            symbol.upper(),
            shares,
            purchase,
            current,
            earn_loss,
            purchase_date,
            yearly_yield
        )


        # Function Call to Build the Table with Variables in Formatted String
        buildTable(final_print)





# Main Function Call
if __name__ == '__main__':
    main()
