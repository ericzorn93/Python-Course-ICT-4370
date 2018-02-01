"""
    Eric Zorn - ICT 4370: Module 6 Classes CSV in Python - 1/29/2018

    This module is the main class module and  contains all of the classes, attributes and methods that are initiated
    and assigned in the other Python Module. This is building upon the data from last week.
"""

import datetime as dt


# Standard Function
def buildTable(*form_string):
    """
    Simply takes in a single variable argument and prints out the formatted string that is taken into the function.
    The function will return the variable as well.
    """
    for i in form_string:
        print(i)
        return i


class ID_counter():
    """
    The ID counter class is used to initiate a counter for different IDs that are found within each of the classes.
    This class and its methods can be used in the Investor Class and the Stock Data Class. Every time a new instance
    of those classes are created, it creates the ability to increment the class ID and store this information into
    a database.
    """
    id_count_investor = 0

    @classmethod
    def get_new_investor_id(cls):
        ID_counter.id_count_investor += 1
        return ID_counter.id_count_investor

    id_count_stock = 0

    @classmethod
    def get_new_stock_id(cls):
        ID_counter.id_count_stock += 1
        return ID_counter.id_count_stock


# Investor Class
class Investor(object):
    """
    The Investor class incorporates any information about a possible Investor. This includes the investor's first name,
    last name, address, and phone number. It then creates a property known as full_name, which concatenates both the
    investor's first and last name. With every instance of the Investor class, there is an initiative of the ID counter.
    """

    def __init__(self, first_name, last_name, address, phone_number):
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.full_name = "{0} {1}".format(self.first_name, self.last_name).title()
        self.address = address
        self.phone_number = phone_number
        self.id = ID_counter.get_new_investor_id()
        print('Investor ID =', self.id, '  for first_name', first_name)


# Stock Data Class
class StockData(object):
    """
    The stock data class takes in a symbol, number of shares owned, purchase_price, and current_price as its incoming
    class parameters. It assigns these parameters as different attributes of the class. The only difference with this
    class is that the purchase date attribute uses a pre-determined date of August 1, 2017 and formats the string with
    the datetime module in Python.
    """

    def __init__(self, symbol, shares_owned, purchase_price, current_price):
        self.symbol = symbol.upper()
        self.shares_owned = int(shares_owned)
        self.purchase_price = purchase_price
        self.current_price = current_price
        self.purchase_date = dt.date(2017, 8, 1).strftime("%m/%d/%Y")
        self.id = ID_counter.get_new_stock_id()
        print('Stock ID =', self.id, '  for symbol', symbol)

    def currentDate(self):
        """
        This function calculates the current date using the date time module and reformats a string of the current date.
        :return: current_date formatted variable
        """
        now = dt.datetime.now()
        current_date = now.strftime('%m/%d/%Y').strip()
        return current_date

    # The formula is (Shares own * current price) - (shares own * bought price)
    def earnLossConversion(self, owned_shares, current_price, purchase_price):
        """
            This function simply takes in three parameters for the amount of shares owned, the current price and the purchase
             price. The function then uses each of the values entered into the parameters and calculates the earnings or losses
             for each stock. At the end of the function, it assigns the calculation to a variable known as earn_loss and then
             returns the variable. This earn_loss variable can then be used outside of the function scope and in other scopes
             within the program.
        """
        earn_loss = (owned_shares * current_price) - (owned_shares * purchase_price)
        return earn_loss

    def newYearlyCalc(self, current_price, purchase_price):
        """
            This function takes in the current price and the purchase price of a stock. It then calculates the
            yearly yield percent by subtracting the purchase price from the current price, dividing that value by
            the purchase price and then multiplying by one-hundred for a percent
        """
        yearly_return_rate = ((current_price - purchase_price) / (purchase_price) * 100)
        return yearly_return_rate


# Calculate Bonds for Different Stocks
class Bonds(StockData):
    """
    Lastly, the Bonds class is inheriting from the StockData class. It inherits all of the same attributes from the
    StockData class, however, it takes in a few parameters of its own. It takes in the Bond symbol, the purchase price,
    and the current price. It also uses some of its own attributes like the quantity, coupon and yield_amt_pct. There is
    a simple method as well which prints the coupon and yield amount in a formatted string.
    """

    def __init__(self, symbol, purchase_price, current_price, quantity, coupon, yield_amt_pct):
        super().__init__(symbol, 0, purchase_price, current_price)
        self.quantity = quantity
        self.coupon = coupon
        self.yield_amt_pct = yield_amt_pct

    def readValues(self):
        print("The coupon value is {0} and the yield amount is {1}%".format(self.coupon, self.yield_amt_pct))

    def buildTable(self, doc, id, symbol, purchase, current, quantity, coupon, yield_amt, purchase_date):
        """
        Builds Bonds Table
        :param doc: Document to write information to
        :param id: Bond ID
        :param symbol: Bond Symbol
        :param purchase: Bond Purchase Price
        :param current: Bond Current Price
        :param quantity: Bond Quantity Amount
        :param coupon: Bond Coupon
        :param yield_amt: Bond Yield Percentage
        :param purchase_date: Bond Purchase Date
        :return: Builds True
        """
        doc.write("\nID: {0}".format(id))
        doc.write("\nSymbol: {0}".format(symbol))
        doc.write("\nPurchase Price: ${0}".format(purchase))
        doc.write("\nCurrent Price: ${0}".format(current))
        doc.write("\nQuantity: {0}".format(quantity))
        doc.write("\nCoupon: {0}".format(coupon))
        doc.write("\nYield: {0}%".format(yield_amt))
        doc.write("\nPurchase Date: {0}".format(purchase_date))
        return True