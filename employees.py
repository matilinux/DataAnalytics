import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('excel/employee.csv')
traveller = df[(df['BusinessTravel']=='Travel_Frequently')]
traveller

females = df[(df['BusinessTravel']=='Travel_Frequently') & (df['Gender']=='Female')] 
females['Gender'].head()

#Can't figure out the "or" condition
#single = df[(df['BusinessTravel']=='Travel_Frequently') & (df['MaritalStatus']=={'Single'} | {'Divorced'})]
#single

single = traveller[(traveller['MaritalStatus']!='Married')]
single[['BusinessTravel','MaritalStatus']].shape
