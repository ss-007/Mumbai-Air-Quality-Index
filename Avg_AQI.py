#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from glob import glob


# In[4]:


###This function is used to calculate avg. of single year
def avg_data_2013():
    temp = 0
    average = []
    for rows in pd.read_csv('C:/Users/Stavan/Desktop/Projects/AQI/Data/AQI/aqi2013.csv', chunksize=24):
        add_var = 0
        avg = 0.0
        data= []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'InVld' and i != '---' and i != 'PwrFail':
                    temporal = float(i)
                    add_var += temporal
                    
        avg = add_var/24

        average.append(avg)
    return(average)



def avg_data_2014():
    temp = 0
    average = []
    for rows in pd.read_csv('C:/Users/Stavan/Desktop/Projects/AQI/Data/AQI/aqi2014.csv', chunksize=24):
        add_var = 0
        avg = 0.0
        data= []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'InVld' and i != '---' and i != 'PwrFail':
                    temporal = float(i)
                    add_var += temporal
                    
        avg = add_var/24

        average.append(avg)
    return(average)



def avg_data_2015():
    temp = 0
    average = []
    for rows in pd.read_csv('C:/Users/Stavan/Desktop/Projects/AQI/Data/AQI/aqi2015.csv', chunksize=24):
        add_var = 0
        avg = 0.0
        data= []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'InVld' and i != '---' and i != 'PwrFail':
                    temporal = float(i)
                    add_var += temporal
                    
        avg = add_var/24

        average.append(avg)
    return(average)



def avg_data_2016():
    temp = 0
    average = []
    for rows in pd.read_csv('C:/Users/Stavan/Desktop/Projects/AQI/Data/AQI/aqi2016.csv', chunksize=24):
        add_var = 0
        avg = 0.0
        data= []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'InVld' and i != '---' and i != 'PwrFail':
                    temporal = float(i)
                    add_var += temporal
                    
        avg = add_var/24

        average.append(avg)
    return(average)



def avg_data_2017():
    temp = 0
    average = []
    for rows in pd.read_csv('C:/Users/Stavan/Desktop/Projects/AQI/Data/AQI/aqi2017.csv', chunksize=24):
        add_var = 0
        avg = 0.0
        data= []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'InVld' and i != '---' and i != 'PwrFail':
                    temporal = float(i)
                    add_var += temporal
                    
        avg = add_var/24

        average.append(avg)
    return(average)



def avg_data_2018():
    temp = 0
    average = []
    for rows in pd.read_csv('C:/Users/Stavan/Desktop/Projects/AQI/Data/AQI/aqi2018.csv', chunksize=24):
        add_var = 0
        avg = 0.0
        data= []
        df = pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'InVld' and i != '---' and i != 'PwrFail':
                    temporal = float(i)
                    add_var += temporal
                    
        avg = add_var/24

        average.append(avg)
    return(average)


# In[10]:


if __name__ == "__main__":
    
    lst2013=avg_data_2013()
    lst2014=avg_data_2014()
    lst2015=avg_data_2015()
    lst2016=avg_data_2016()
    lst2017=avg_data_2017()
    lst2018=avg_data_2018()
    
    plt.plot(range(0,365),lst2013,label="2013 data")
    plt.plot(range(0,364),lst2014,label="2014 data")
    plt.plot(range(0,365),lst2015,label="2015 data")
    plt.plot(range(0,365),lst2016,label="2016 data")
    plt.xlabel('Days')
    plt.ylabel('PM2.5')
    plt.legend()
    plt.show()


# In[33]:


###This is used for calculating all the years

#def avg_data_allyear():
#    file_names = glob('C:/Users/Stavan/Desktop/Projects/Data/AQI/*.csv')
#    df = [f for f in file_names]
#    avg_all_years = []
    
#    for f in file_names:
#        temp = 0
#        average = []
#        for rows in pd.read_csv(f, chunksize=24):
#            add_var = 0
#            avg = 0.0
#            data= []
#            df0 = pd.DataFrame(data=rows)
#            for index,row in df0.iterrows():
#                data.append(row['PM2.5'])
            
#            for i in data:
#                if type(i) is float or type(i) is int:
#                    add_var += i
#                elif type(i) is str:
#                    if i != 'NoData' and i != 'InVld' and i != '---' and i != 'PwrFail':
#                        temporal = float(i)
#                        add_var += temporal
                    
#                avg = add_var/24

#            average.append(avg)
#        avg_all_years.append(average)
#    return(avg_all_years)

