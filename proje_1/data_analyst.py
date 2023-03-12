from pizza_full_database import receipt_pizza_addmade_database
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbr

data_all=receipt_pizza_addmade_database()
data1=data_all.all_receipt_pizza()
database_dictionary={}
pizza_database_name_addmade_price=[]
for i in data1:
    for j in(i[0].split("\n")):
        if(j!=""):
            pizza_database_name_addmade_price.append(j)
database_dictionary["pizza_database_name_addmade_price"]=pizza_database_name_addmade_price
print("**************")
print(database_dictionary)
print("**************")




data2=data_all.all_receipt_pizza_addmade()
print(data2)
pizza_database_addmade=[]
all_addmade_list=[]
for i in data2:
    for j in(i[0].split("\n")):
        for t in(j.split(" ")):
            if (t!=""):
                all_addmade_list.append(t)
        if(j!=""):
            pizza_database_addmade.append(j)
print(pizza_database_addmade)
print(all_addmade_list)
database_dictionary["all_preferred_together_addmade"]=pizza_database_addmade

#database_dictionary["all_addmade"]=all_addmade_list
print("**************")
print(database_dictionary)
print("**************")

data3=data_all.all_receipt_pizza_name()
print(data3)
pizza_database_name=[]
for i in data3:
    for j in(i[0].split("\n")):
        if(j!=""):
            pizza_database_name.append(j)
print(pizza_database_name)
database_dictionary["all_pizza_name"]=pizza_database_name

print("**************")
print(database_dictionary)
print("**************")


data4=data_all.all_receipt_pizza_total()
print(data4)
pizza_database_total=[]
for i in data4:
    for j in(i[0].split("\n")):
        print(j)
        if(j!=""):
            pizza_database_total.append(j)
print(pizza_database_total)
database_dictionary["all_pizza_total"]=pizza_database_name
print("****************")
#print(database_dictionary["all_addmade"])
#print(len(database_dictionary["all_addmade"]))
print(len(database_dictionary["all_pizza_name"]))
print(len(database_dictionary["all_pizza_total"]))
print(len(database_dictionary["all_preferred_together_addmade"]))
print(len(database_dictionary["pizza_database_name_addmade_price"]))


data_frame=(pd.DataFrame.from_dict(database_dictionary))
# creating the dataframe ending
# dataframe and data analysisy started
def pizza_database_name_addmade_func(data_frame):
    data_frame_pizza_database_name_addmade_price=data_frame.iloc[:,0]
    print(data_frame_pizza_database_name_addmade_price)
    counterlist=[]
    set_data_frame_pizza_database_name_addmade_price=list(set(data_frame_pizza_database_name_addmade_price))
    for i in set_data_frame_pizza_database_name_addmade_price:
        counterlist.append(list(data_frame_pizza_database_name_addmade_price).count(i))

    #data_frame.plot.bar(x='lifespan', rot=0)
    print(set_data_frame_pizza_database_name_addmade_price)
    print(counterlist)
    plt.figure().set_figwidth(20)
    plt.subplots_adjust(left=0.3)
    plt.title("graph of all pizzas by sale")
    plt.barh(set_data_frame_pizza_database_name_addmade_price,counterlist)
    plt.show()

#pizza_database_name_addmade_func(data_frame)
def pizza_database_together_addmade_func(dataframe):
    all_addmade=data_frame.iloc[:,1]
    all_addmade=(list(all_addmade))
    print(all_addmade)
    all_addmade_list=[]
    for i in all_addmade:
        for j in (i.split(" ")):
            if(j!=""):
                all_addmade_list.append(j)

    set_allmade_list=list(set(all_addmade))
    allmade_list_count=[]
    for i in set_allmade_list:
        allmade_list_count.append(all_addmade.count(i))
    print(set_allmade_list)
    print(allmade_list_count)
    plt.figure().set_figwidth(20)
    plt.subplots_adjust(left=0.3)
    plt.title("proportion of additional materials used together")
    plt.barh(set_allmade_list,allmade_list_count)
    plt.show()

b=data_frame.iloc[:,2]
print(b)

