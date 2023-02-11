# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:47:26 2023

@author: hp
"""
import pandas as pd;
import json;
import numpy as np;
import matplotlib.pyplot as plt;


# read json data

data_list = json.load(open('loan_data_json.json'))
data = pd.DataFrame(data_list);

#finding unique values for the purpose column
data['purpose'].unique()

#describing the data

data.describe()

#finding income
data['annualincome'] = np.exp(data['log.annual.inc']);


category = [];

for x in range(0,len(data)):
    fico = data['fico'][x]
    try:
        if fico >= 300 and fico < 400:
            ficocat = 'Very Poor'
        elif fico >=400 and fico < 600:
            ficocat = 'Poor'
        elif fico >=601 and fico < 660:
            ficocat = 'Fair'
        elif fico >=660 and fico < 700:
            ficocat = 'Good'
        elif fico >= 700:
            ficocat = 'Excellent'
        else:
            ficocat = 'Unknown'
    except:
        ficocat='unknown';
    category.append(ficocat);

category = pd.Series(category);
data['ficocat'] = category;

data.loc[data['int.rate']  > 0.12 , 'int.rate.type'] = 'High'
data.loc[data['int.rate']  <= 0.12 , 'int.rate.type'] = 'Low'




# category wise fico


people_by_fico_category = data.groupby(['ficocat']).size();
people_by_purpose_category = data.groupby(['purpose']).size();
# people_by_fico_category = data.groupby(['annualincome']).size();
# people_by_fico_category = data.groupby(['int.rate.type']).size();

people_by_fico_category.plot.bar()
plt.show()
people_by_purpose_category.plot.bar(color = 'green')

plt.scatter(data['dti'] , data['annualincome'])
 




#export

data.to_csv('bank_final.csv' , index = True)











