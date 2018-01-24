import datetime as dt


# Investor Class
class Investor:
    def __init__(self, first_name, last_name, address, phone_number):
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.full_name = "{0} {1}".format(self.first_name, self.last_name).title()
        self.address = address
        self.phone_number = phone_number




# Stock Data Class
class StockData:
    def __init__(self, symbol, shares_owned, purchase_price, current_price):
        self.symbol = symbol
        self.shares_owned = int(shares_owned)
        self.purchase_price = purchase_price
        self.current_price = current_price
        self.purchase_date = "8/1/2015"

    def currentDate(self):
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
    def __init__(self, symbol, shares_owned, purchase_price, current_price, quantity, coupon, yield_amt_pct):
        super().__init__(symbol, shares_owned, purchase_price, current_price)
        self.quantity = quantity
        self.coupon = coupon
        self.yield_amt_pct = yield_amt_pct

    def calcCoupon(self):
        """
        Calculates the correct coupon percentage
        :return: coupon amount
        """
        return self.quantity