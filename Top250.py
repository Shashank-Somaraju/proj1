import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os
matplotlib.use('Agg')

data=pd.read_csv("data/Top250.csv")
data.head()
data.columns
data.Restaurant
data.Restaurant.isnull().sum()
data.isnull().sum()
data.Segment_Category.unique()
data["Casual_Dining"]=data['Segment_Category'].str.contains("Casual Dining")
data.head()
def p2f(x):
    return float(x.strip('%'))/100
data['YOY_Sales']=data.YOY_Sales.apply(p2f)
data['YOY_Units']=data.YOY_Units.apply(p2f)
data.head()
if os.path.exists("proj1/static/images/image4.png"):
        os.remove("proj1/static/images/image4.png")
def bargraph(x,y,sample_size):
    plt.bar(data[x][:sample_size],data[y][:sample_size],color=["red","green"])
    if(sample_size>=20):
        if x=="Restaurant" :
            plt.xticks(range(0,len(data[x][:sample_size]),2),rotation= 90)
        else:
            plt.xticks(range(0,len(data[x][:sample_size]),2),rotation= 0)
    else:
        if x=="Restaurant" :
            plt.xticks(range(0,len(data[x][:sample_size]),2),rotation= 90)
    plt.savefig("proj1/static/images/image4.png",dpi=300, bbox_inches='tight')


def plot(x,y,sample_size):
    plt.plot(data[x][:sample_size],data[y][:sample_size])
    if(sample_size>=20):
        if x=="Restaurant" :
            plt.xticks(range(0,len(data[x][:sample_size]),2),rotation= 90)
        else:
            plt.xticks(range(0,len(data[x][:sample_size]),2),rotation= 0)
    else:
        if x=="Restaurant" :
            plt.xticks(range(0,len(data[x][:sample_size]),2),rotation= 90)
    plt.savefig("proj1/static/images/image4.png",dpi=300, bbox_inches='tight')


def scatter(x,y,sample_size):
    plt.scatter(data[x][:sample_size],data[y][:sample_size])
    if(sample_size>=20):
        if x=="Restaurant" :
            plt.xticks(range(0,len(data[x][:sample_size]),2),rotation= 90)
        else:
            plt.xticks(range(0,len(data[x][:sample_size]),2),rotation= 0)
    else:
        if x=="Restaurant" :
            plt.xticks(range(0,len(data[x][:sample_size]),20),rotation= 90)
    plt.savefig("proj1/static/images/image4.png",dpi=300, bbox_inches='tight')

