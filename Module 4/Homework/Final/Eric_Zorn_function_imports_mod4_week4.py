"""
    Functions for Module 4 to Import into Eric_Zorn_functions_mod4_week4.py

    Main Functions are defined and called on the other document.

    These functions are used to calculate the earns or losses of the current stock for the user's portfoilio.
    The second is to calculate the yearly yield percentage for the user. Lastly, the buildTable() function is used
    to take in any number of formatted strings of information. It then loops through the string and builds a table.
    This would be useful if the programmer had many tables of different information to build.
"""


# The formula is (Shares own * current price) - (shares own * bought price)
def earnLossConversion(owned_shares, current_price, purchase_price):
    """
        This function simply takes in three parameters for the amount of shares owned, the current price and the purchase
         price. The function then uses each of the values entered into the parameters and calculates the earnings or losses
         for each stock. At the end of the function, it assigns the calculation to a variable known as earn_loss and then
         returns the variable. This earn_loss variable can then be used outside of the function scope and in other scopes
         within the program.
    """
    earn_loss = (owned_shares * current_price) - (owned_shares * purchase_price)
    return earn_loss

def newYearlyCalc(current_price, purchase_price):
    """
        This function takes in the current price and the purchase price of a stock. It then calculates the
        yearly yield percent by subtracting the purchase price from the current price, dividing that value by
        the purchase price and then multiplying by one-hundred for a percent
    """
    yearly_return_rate = ((current_price - purchase_price) / (purchase_price) * 100)
    return yearly_return_rate


def buildTable(*form_string):
    """
    Simply takes in a single variable argument and prints out the formatted string that is taken into the function.
    The function will return the variable as well.
    """
    for i in form_string:
        print(i)
        return i