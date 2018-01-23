"""Beginning of the Program"""
import datetime as dt
from function_import_mod4 import earnLossConversion, newYearlyCalc, buildTable


def main():
    # Purchase Date Variable Declaration
    purchase_date = "8/1/2015"

    # Current Date Variable Declaration
    now = dt.datetime.now()
    current_date = now.strftime('%m/%d/%Y').strip()



    # Dictionary Definitions
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
        "Yearly Earning/Loss"
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

    # earns_losses = {}
    # yearly_earns_losses = {}
    name = input("What is your full name? ").title().strip()


    print("Stock Portfolio Information for {0}\n".format(name))

    for title in titles:
        print(title, end=' | ')

    print("\n")

    for key, val in stocks_dict.items():
        val["earn_loss"] = earnLossConversion(
        stocks_dict[key]["shares"],
        stocks_dict[key]["current_price"],
        stocks_dict[key]["purchase_price"]
        )

        val["yearly_yield"] = round(newYearlyCalc(
            stocks_dict[key]["current_price"],
            stocks_dict[key]["purchase_price"]
        ), 2)

        # print(val)

        symbol = val["symbol"]
        shares = val["shares"]
        purchase = val["purchase_price"]
        current = val["current_price"]
        earn_loss = val["earn_loss"]
        purchase_date = purchase_date
        yearly_yield = val["yearly_yield"]

        # print(symbol, " | ", shares, " | ", purchase, " | ", current)
        final_print = "{0} | {1} | ${2} | ${3} | ${4} | {5} | {6}%".format(
            symbol,
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
