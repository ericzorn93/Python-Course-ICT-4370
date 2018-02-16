from django.shortcuts import render, HttpResponse
from django.views.generic import RedirectView
from stock.models import Stock
import sqlite3


# Create your views here.
def Home(request):
    title = "ICT 4370 Stock Information"
    investor_query = "SELECT full_name FROM investors"
    stock_query = "SELECT * FROM stocks"

    conn = sqlite3.connect('stock_info.db')
    cursor = conn.cursor()

    cursor.execute(investor_query)
    return_data_investor = cursor.fetchall()

    cursor.execute(stock_query)
    return_data_stock = cursor.fetchall()

    context = {
        "investor_one": return_data_investor[0][0],
        "investor_two": return_data_investor[1][0],
        "google_stock": return_data_stock[0],
        "msft_stock": return_data_stock[1],
        "rds_a_stock": return_data_stock[2],
        "aig_stock": return_data_stock[3],
        "fb_stock": return_data_stock[4],
        "m_stock": return_data_stock[5],
        "f_stock": return_data_stock[6],
        "ibm_stock": return_data_stock[7],
        "appl_stock": return_data_stock[8],
        "title": title,
    }

    conn.close()

    return render(request, 'stock/index.html', context)


# Bonds View
def Bonds(request):
    title = "ICT 4370 Stock Information"
    investor_query = "SELECT full_name FROM investors"
    bond_query = "SELECT * FROM bonds"

    conn = sqlite3.connect('stock_info.db')
    cursor = conn.cursor()

    cursor.execute(investor_query)
    return_data_investor = cursor.fetchall()

    cursor.execute(bond_query)
    return_data_bond = cursor.fetchall()

    context = {
        "investor_one": return_data_investor[0][0],
        "investor_two": return_data_investor[1][0],
        "bond_one": return_data_bond[0],
        "bond_one_purchase_date": "8/1/2017",
        "bond_one_purchase_price": 100.02,
        "bond_one_current_price": 100.05,
        "title": title,
        "home_page": "http://127.0.0.1:8000/",
        "bonds_page": "http://127.0.0.1:8000/bonds",
        "investors_page": "http://127.0.0.1:8000/investors",
    }

    conn.close()

    return render(request, 'bonds/bonds.html', context)


# Investors View
def Investors(request):
    title = "ICT 4370 Stock Information"
    investor_query = "SELECT * FROM investors"

    conn = sqlite3.connect('stock_info.db')
    cursor = conn.cursor()

    cursor.execute(investor_query)
    return_data_investor = cursor.fetchall()

    context = {
       "investor_one": return_data_investor[0],
       "investor_two": return_data_investor[1],
       "home_page": "http://127.0.0.1:8000/",
       "bonds_page": "http://127.0.0.1:8000/bonds",
       "investors_page": "http://127.0.0.1:8000/investors",
    }

    conn.close()

    return render(request, 'investors/investors.html', context)