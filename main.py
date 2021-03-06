import cx_Oracle
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import chart_studio
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dashboard
import re


username = 'MYONLINEEDU'
password = 'njvf24'
databaseName = 'localhost/xe'
chart_studio.tools.set_credentials_file(username='t.prykhodko', api_key='5QCDRot27p6rJ3XQjSs4')
connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()


def get_id(url):
    return re.findall("[0-9]+", url)[0]


query1 = """SELECT Count(store_number) As Count_Country,country_name AS Country
From store_country
GROUP BY country_name
"""
cursor.execute(query1)

c_contry = list()
country = list()

for Count_Country, Country in cursor:
    c_contry.append(Count_Country)
    country.append(Country)
    
print("QUERY N1")
print(c_contry)
print(country)



query2 = '''SELECT Count(store_number) As Count_Ownership,ownership_owner_ship AS Ownership
From store_country
GROUP BY ownership_owner_ship'''
cursor.execute(query2)
c_o = list()
ownersh = list()

for Count_Ownership, Ownership in cursor:
    c_o.append(Count_Ownership)
    ownersh.append(Ownership)
    
print('QUERY N2')
print(c_o)
print(ownersh)



query3 = '''SELECT Count(brand_brand_name) As Count_Brand,brand_brand_name AS Brand
From store_country
GROUP BY brand_brand_name
'''

cursor.execute(query3)
c_b= list()
brands = list()

for Brand, Count_Brand in cursor:
    brands.append(Brand)
    c_b.append(Count_Brand)
    
    
print('QUERY 3')
print(c_b)
print(brands)

bar = go.Bar(
    x=country,y=c_contry)
gr_q1 = py.plot([bar], auto_open=False, filename='task N1')

pie = go.Pie(
    labels=ownersh,values=c_o)
gr_q2 = py.plot([pie], auto_open=False, filename='task N2')

scatter = go.Scatter(x=c_b,y=brands)
gr_q3 = py.plot([scatter], auto_open=False, filename='task N3')

my_board = dashboard.Dashboard()
box_n_one = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': 't.prykhodko:' + get_id(gr_q1),
    'title': '1 запит-кількість філіалів  в 3 країнах з найбільшої кількістю закладів '
}


box_n_two = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': 't.prykhodko:' + get_id(gr_q2),
    'title': '2 запит-форми власності та відсоток закладів з такою формою власності',

}


box_n_three = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': 't.prykhodko:' + get_id(gr_q3),
    'title': '3 запит-кількість філіалів у кожного бренду'
}

my_board.insert(box_n_one)
my_board.insert(box_n_two, 'below', 1)
my_board.insert(box_n_three, 'right', 2)

py.dashboard_ops.upload(my_board, 'Prykhodko')

cursor.close()
connection.close()
