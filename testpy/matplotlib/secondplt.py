"""
Eric Zorn - ICT 4370 - Using Matplotlib and Pyplot to create a Graph - 2/6/18
"""

# Imports
from matplotlib import pyplot as plt
import datetime
import sqlite3


# Data to be Plotted onto the graph
open_price  = [145.0, 144.43, 145.12, 145.0, 144.81, 145.0, 146.27, 146.57, 147.0, 147.59, 147.53, 150.02, 152.36,
               153.59, 154.01, 153.7, 153.48, 153.26, 152.91, 152.62, 153.36, 155.77, 153.58, 154.28, 155.35, 155.15,
               155.0, 154.71,154.34, 154.55, 155.79, 154.48, 155.51, 154.23, 153.29, 153.97, 155.44, 154.19, 152.0,
               151.0, 153.05, 152.0, 151.82, 153.07, 152.8, 152.03, 151.95, 152.85, 153.25, 152.21, 152.57, 152.1,
               151.01, 150.86, 153.3, 151.66, 150.62, 150.3]


close_price = [145.16, 144.94, 144.45, 145.3, 144.29, 145.07, 145.36, 146.19, 145.99, 147.08, 147.66, 147.53,
               154.0, 153.01, 154.24, 153.63, 153.7, 153.19, 153.42, 152.94, 152.36, 153.67, 155.58, 153.83,
               154.13, 155.32, 154.75, 155.23, 154.11, 154.4, 153.79, 154.95, 154.84, 155.38, 154.22, 153.81,
               154.25, 155.18, 154.1, 152.1, 150.98, 152.37, 152.41, 152.05, 152.67, 152.63, 151.73, 152.49, 153.2,
               152.51, 152.03, 152.64, 151.98, 150.78, 150.93, 153.68, 151.51, 150.37]

date_list = [datetime.date(2017, 8, 4), datetime.date(2017, 8, 3), datetime.date(2017, 8, 2), datetime.date(2017, 8, 1),
             datetime.date(2017, 7, 28), datetime.date(2017, 7, 27), datetime.date(2017, 7, 26),
             datetime.date(2017, 7, 25), datetime.date(2017, 7, 24), datetime.date(2017, 7, 21),
             datetime.date(2017, 7, 20), datetime.date(2017, 7, 19), datetime.date(2017, 7, 18),
             datetime.date(2017, 7, 17), datetime.date(2017, 7, 14), datetime.date(2017, 7, 13),
             datetime.date(2017, 7, 12), datetime.date(2017, 7, 11), datetime.date(2017, 7, 10),
             datetime.date(2017, 7, 7), datetime.date(2017, 7, 6), datetime.date(2017, 7, 5),
             datetime.date(2017, 7, 3), datetime.date(2017, 6, 30), datetime.date(2017, 6, 29),
             datetime.date(2017, 6, 28), datetime.date(2017, 6, 27), datetime.date(2017, 6, 26),
             datetime.date(2017, 6, 23), datetime.date(2017, 6, 22), datetime.date(2017, 6, 21),
             datetime.date(2017, 6, 20), datetime.date(2017, 6, 19), datetime.date(2017, 6, 16),
             datetime.date(2017, 6, 15), datetime.date(2017, 6, 14), datetime.date(2017, 6, 13),
             datetime.date(2017, 6, 12), datetime.date(2017, 6, 9), datetime.date(2017, 6, 8),
             datetime.date(2017, 6, 7), datetime.date(2017, 6, 6), datetime.date(2017, 6, 5),
             datetime.date(2017, 6, 2), datetime.date(2017, 6, 1), datetime.date(2017, 5, 31),
             datetime.date(2017, 5, 30), datetime.date(2017, 5, 26), datetime.date(2017, 5, 25),
             datetime.date(2017, 5, 24), datetime.date(2017, 5, 23), datetime.date(2017, 5, 22),
             datetime.date(2017, 5, 19), datetime.date(2017, 5, 18), datetime.date(2017, 5, 17),
             datetime.date(2017, 5, 16), datetime.date(2017, 5, 15), datetime.date(2017, 5, 12)]

# Sort Dates in Order
date_list.sort()


# Plot Data Using Pyplot
plt.title("Stock Market Prices")
plt.xlabel("Date")
plt.ylabel("Price")


# Sets Data, Colors, Axis and Labels for Legend
ax = plt.gca() # grab the current axis
ax.set_xticklabels(date_list) # set the labels to display at those ticks
plt.plot(open_price, label='Open Prices', color="red")
plt.plot(close_price, label='Closed Prices', color="blue")

# Legend Location
plt.legend(loc='upper right')

# Write Graph to file
plt.savefig('2.6.18 StockDataWrittenFile.png')

# Display Graph Data
plt.show()