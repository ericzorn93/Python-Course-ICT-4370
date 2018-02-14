
# if you add a this __iter__ method to your StockData class
class StockData(object):
    def __iter__(self):
        # yields class attributes in desired order
        for field in [self.id, self,symbol, self.shares_owned,
                self.purchase_price, self.current_price, self.purchase_date]:
            yield field


# you can replace this code from line 328
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