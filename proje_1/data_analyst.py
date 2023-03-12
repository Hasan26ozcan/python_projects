from pizza_full_database import receipt_pizza_addmade_database
import pandas as pd
import matplotlib
import seaborn
pd.DataFrame

data_all=receipt_pizza_addmade_database()
data1=data_all.all_receipt_pizza()
database_dictionary={}
pizza_database_name_addmade_price=[]
for i in data1:
    for j in(i[0].split("\n")):
        pizza_database_name_addmade_price.append(j)
database_dictionary["pizza_database_name_addmade_price"]=pizza_database_name_addmade_price
print(database_dictionary)

data2=data_all.all_receipt_pizza_addmade()
print(data2)









