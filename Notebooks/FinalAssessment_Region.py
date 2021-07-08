# This file starts to answer the following questions:

"""
-----------Questions:-----------------
* Based on historical data, what is the predicted amount of total expenses in 2018?
* Is there a significant difference in the predicted and actual amounts of expenses?
* Is there a significant difference in the actual amount spent and the amount recieved by the government?
"""

#imports all libraries to make the study possible
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#puts the 2008-2018 Public Elementary-Secondary Education Finance Data files into a DataFrame
census2018=pd.read_excel('elsec18_sumtables.xls',sheet_name='1')
census2017=pd.read_excel('elsec17_sumtables.xls',sheet_name='1')
census2016=pd.read_excel('elsec16_sumtables.xls',sheet_name='1')
census2015=pd.read_excel('elsec15_sttables.xls',sheet_name='1')
census2014=pd.read_excel('elsec14_sttables.xls',sheet_name='1')
census2013=pd.read_excel('elsec13_sttables.xls',sheet_name='1')
census2012=pd.read_excel('elsec12_sttables.xls',sheet_name='1')
census2011=pd.read_excel('elsec11_sttables.xls',sheet_name='1')
census2010=pd.read_excel('elsec10_sttables.xls',sheet_name='1')
census2009=pd.read_excel('elsec09_sttables.xls',sheet_name='1')
census2008=pd.read_excel('elsec08_sttables.xls',sheet_name='1')

#studys one table to gain an understanding of them all as they are all made the same way
print(len(census2018))
print(census2018.head())
print(census2018.columns)
print(census2018.info())

#removes initial rows that don't make any sense
census2018.drop(index=census2018.index[:7],axis=0,inplace=True)
#looking at the original excel sheet, there is an excess amount of columns
#I believe that the column containing 0 entries was pandas way of making sense of there existing 2(?) tables
#we will drop it. It does not contain any information regardless
census2018.dropna(how='all',axis=1,inplace=True)
#rename columns
census2018.columns=['Name','Total Income','From federal','From state','From local','Total Spending','Operation Expense','Improvement Expense','Other Expenses','Outstanding Debt','Cash and Securities']
#remove rows with all values=NaN
census2018.dropna(axis=0,how='all',inplace=True)
#clear those '.' at the end of the state names and remove them from the dataframe, they make the table difficult to read
census2018[['Name','Remove']] = census2018['Name'].str.split(pat='.',n=1,expand=True)
census2018.drop(['Remove'],axis=1,inplace=True)
#replace strings in int columns to make their type int
census2018.replace(to_replace='(X)',value=0,inplace=True)
#change proper columns to float to allow for number queries
census2018.astype({'Total Income':'float'})
#resets index for optimal table use
census2018 = census2018.reset_index(drop=True)
#remove the United States as it is not a row in the other dataset
census2018 = census2018.iloc[1:]
#adds a year column to better map the datasets
census2018.insert(0,'Year',2018,allow_duplicates=True)    
#checking out process to tie up loose ends
print(census2018.columns)
print(census2018.info())
print(census2018.head())

#removes initial rows that don't make any sense
census2017.drop(index=census2017.index[:7],axis=0,inplace=True)
#looking at the original excel sheet, there is an excess amount of columns
#I believe that the column containing 0 entries was pandas way of making sense of there existing 2(?) tables
#we will drop it. It does not contain any information regardless
census2017.dropna(how='all',axis=1,inplace=True)
#rename columns
census2017.columns=['Name','Total Income','From federal','From state','From local','Total Spending','Operation Expense','Improvement Expense','Other Expenses','Outstanding Debt','Cash and Securities']
#remove rows with all values=NaN
census2017.dropna(axis=0,how='all',inplace=True)
#clear those '.' at the end of the state names and remove them from the dataframe, they make the table difficult to read
census2017[['Name','Remove']] = census2017['Name'].str.split(pat='.',n=1,expand=True)
census2017.drop(['Remove'],axis=1,inplace=True)
#replace strings in int columns to make their type int
census2017.replace(to_replace='(X)',value=0,inplace=True)
#change proper columns to float to allow for number queries
census2017.astype({'Total Income':'float'})
#resets index for optimal table use
census2017 = census2017.reset_index(drop=True)
#remove the United States as it is not a row in the other dataset
census2017 = census2017.iloc[1:]
#adds a year column to better map the datasets
census2017.insert(0,'Year',2017,allow_duplicates=True)    
#checking out process to tie up loose ends
print(census2017.columns)
print(census2017.info())
print(census2017.head())

#removes initial rows that don't make any sense
census2016.drop(index=census2016.index[:7],axis=0,inplace=True)
#looking at the original excel sheet, there is an excess amount of columns
#I believe that the column containing 0 entries was pandas way of making sense of there existing 2(?) tables
#we will drop it. It does not contain any information regardless
census2016.dropna(how='all',axis=1,inplace=True)
#rename columns
census2016.columns=['Name','Total Income','From federal','From state','From local','Total Spending','Operation Expense','Improvement Expense','Other Expenses','Outstanding Debt','Cash and Securities']
#remove rows with all values=NaN
census2016.dropna(axis=0,how='all',inplace=True)
#clear those '.' at the end of the state names and remove them from the dataframe, they make the table difficult to read
census2016[['Name','Remove']] = census2016['Name'].str.split(pat='.',n=1,expand=True)
census2016.drop(['Remove'],axis=1,inplace=True)
#replace strings in int columns to make their type int
census2016.replace(to_replace='(X)',value=0,inplace=True)
#change proper columns to float to allow for number queries
census2016.astype({'Total Income':'float'})
#resets index for optimal table use
census2016 = census2016.reset_index(drop=True)
#remove the United States as it is not a row in the other dataset
census2016 = census2016.iloc[1:]
#adds a year column to better map the datasets
census2016.insert(0,'Year',2016,allow_duplicates=True)    
#checking out process to tie up loose ends
print(census2016.columns)
print(census2016.info())
print(census2016.head())

#removes initial rows that don't make any sense
census2015.drop(index=census2015.index[:7],axis=0,inplace=True)
#looking at the original excel sheet, there is an excess amount of columns
#I believe that the column containing 0 entries was pandas way of making sense of there existing 2(?) tables
#we will drop it. It does not contain any information regardless
census2015.dropna(how='all',axis=1,inplace=True)
#rename columns
census2015.columns=['Name','Total Income','From federal','From state','From local','Total Spending','Operation Expense','Improvement Expense','Other Expenses','Outstanding Debt','Cash and Securities']
#remove rows with all values=NaN
census2015.dropna(axis=0,how='all',inplace=True)
#clear those '.' at the end of the state names and remove them from the dataframe, they make the table difficult to read
census2015[['Name','Remove']] = census2015['Name'].str.split(pat='.',n=1,expand=True)
census2015.drop(['Remove'],axis=1,inplace=True)
#replace strings in int columns to make their type int
census2015.replace(to_replace='(X)',value=0,inplace=True)
#change proper columns to float to allow for number queries
census2015.astype({'Total Income':'float'})
#resets index for optimal table use
census2015 = census2015.reset_index(drop=True)
#remove the United States as it is not a row in the other dataset
census2015 = census2015.iloc[1:]
#adds a year column to better map the datasets
census2015.insert(0,'Year',2015,allow_duplicates=True)    
#checking out process to tie up loose ends
print(census2015.columns)
print(census2015.info())
print(census2015.head())

#removes initial rows that don't make any sense
census2014.drop(index=census2014.index[:7],axis=0,inplace=True)
#looking at the original excel sheet, there is an excess amount of columns
#I believe that the column containing 0 entries was pandas way of making sense of there existing 2(?) tables
#we will drop it. It does not contain any information regardless
census2014.dropna(how='all',axis=1,inplace=True)
#rename columns
census2014.columns=['Name','Total Income','From federal','From state','From local','Total Spending','Operation Expense','Improvement Expense','Other Expenses','Outstanding Debt','Cash and Securities']
#remove rows with all values=NaN
census2014.dropna(axis=0,how='all',inplace=True)
#clear those '.' at the end of the state names and remove them from the dataframe, they make the table difficult to read
census2014[['Name','Remove']] = census2014['Name'].str.split(pat='.',n=1,expand=True)
census2014.drop(['Remove'],axis=1,inplace=True)
#replace strings in int columns to make their type int
census2014.replace(to_replace='(X)',value=0,inplace=True)
#change proper columns to float to allow for number queries
census2014.astype({'Total Income':'float'})
#resets index for optimal table use
census2014 = census2014.reset_index(drop=True)
#remove the United States as it is not a row in the other dataset
census2014 = census2014.iloc[1:]
#adds a year column to better map the datasets
census2014.insert(0,'Year',2014,allow_duplicates=True)    
#checking out process to tie up loose ends
print(census2014.columns)
print(census2014.info())
print(census2014.head())

#removes initial rows that don't make any sense
census2013.drop(index=census2013.index[:7],axis=0,inplace=True)
#looking at the original excel sheet, there is an excess amount of columns
#I believe that the column containing 0 entries was pandas way of making sense of there existing 2(?) tables
#we will drop it. It does not contain any information regardless
census2013.dropna(how='all',axis=1,inplace=True)
#rename columns
census2013.columns=['Name','Total Income','From federal','From state','From local','Total Spending','Operation Expense','Improvement Expense','Other Expenses','Outstanding Debt','Cash and Securities']
#remove rows with all values=NaN
census2013.dropna(axis=0,how='all',inplace=True)
#clear those '.' at the end of the state names and remove them from the dataframe, they make the table difficult to read
census2013[['Name','Remove']] = census2013['Name'].str.split(pat='.',n=1,expand=True)
census2013.drop(['Remove'],axis=1,inplace=True)
#replace strings in int columns to make their type int
census2013.replace(to_replace='(X)',value=0,inplace=True)
#change proper columns to float to allow for number queries
census2013.astype({'Total Income':'float'})
#resets index for optimal table use
census2013 = census2013.reset_index(drop=True)
#remove the United States as it is not a row in the other dataset
census2013 = census2013.iloc[1:]
#adds a year column to better map the datasets
census2013.insert(0,'Year',2013,allow_duplicates=True)    
#checking out process to tie up loose ends
print(census2013.columns)
print(census2013.info())
print(census2013.head())

#removes initial rows that don't make any sense
census2012.drop(index=census2012.index[:7],axis=0,inplace=True)
#looking at the original excel sheet, there is an excess amount of columns
#I believe that the column containing 0 entries was pandas way of making sense of there existing 2(?) tables
#we will drop it. It does not contain any information regardless
census2012.dropna(how='all',axis=1,inplace=True)
#rename columns
census2012.columns=['Name','Total Income','From federal','From state','From local','Total Spending','Operation Expense','Improvement Expense','Other Expenses','Outstanding Debt','Cash and Securities']
#remove rows with all values=NaN
census2012.dropna(axis=0,how='all',inplace=True)
#clear those '.' at the end of the state names and remove them from the dataframe, they make the table difficult to read
census2012[['Name','Remove']] = census2012['Name'].str.split(pat='.',n=1,expand=True)
census2012.drop(['Remove'],axis=1,inplace=True)
#replace strings in int columns to make their type int
census2012.replace(to_replace='(X)',value=0,inplace=True)
#change proper columns to float to allow for number queries
census2012.astype({'Total Income':'float'})
#resets index for optimal table use
census2012 = census2012.reset_index(drop=True)
#remove the United States as it is not a row in the other dataset
census2012 = census2012.iloc[1:]
#adds a year column to better map the datasets
census2012.insert(0,'Year',2012,allow_duplicates=True)    
#checking out process to tie up loose ends
print(census2012.columns)
print(census2012.info())
print(census2012.head())

#removes initial rows that don't make any sense
census2011.drop(index=census2011.index[:9],axis=0,inplace=True)
#looking at the original excel sheet, there is an excess amount of columns
#I believe that the column containing 0 entries was pandas way of making sense of there existing 2(?) tables
#we will drop it. It does not contain any information regardless
census2011.dropna(how='all',axis=1,inplace=True)
#rename columns
census2011.columns=['Name','Total Income','From federal','From state','From local','Total Spending','Operation Expense','Improvement Expense','Other Expenses','Outstanding Debt','Cash and Securities']
#remove rows with all values=NaN
census2011.dropna(axis=0,how='all',inplace=True)
#clear those '.' at the end of the state names and remove them from the dataframe, they make the table difficult to read
census2011[['Name','Remove']] = census2011['Name'].str.split(pat='.',n=1,expand=True)
census2011.drop(['Remove'],axis=1,inplace=True)
#replace strings in int columns to make their type int
census2011.replace(to_replace='(X)',value=0,inplace=True)
#change proper columns to float to allow for number queries
census2011.astype({'Total Income':'float'})
#resets index for optimal table use
census2011 = census2011.reset_index(drop=True)
#remove the United States as it is not a row in the other dataset
census2011 = census2011.iloc[1:]
#adds a year column to better map the datasets
census2011.insert(0,'Year',2011,allow_duplicates=True)    
#checking out process to tie up loose ends
print(census2011.columns)
print(census2011.info())
print(census2011.head())

#removes initial rows that don't make any sense
census2010.drop(index=census2010.index[:9],axis=0,inplace=True)
#looking at the original excel sheet, there is an excess amount of columns
#I believe that the column containing 0 entries was pandas way of making sense of there existing 2(?) tables
#we will drop it. It does not contain any information regardless
census2010.dropna(how='all',axis=1,inplace=True)
#rename columns
census2010.columns=['Name','Total Income','From federal','From state','From local','Total Spending','Operation Expense','Improvement Expense','Other Expenses','Outstanding Debt','Cash and Securities']
#remove rows with all values=NaN
census2010.dropna(axis=0,how='all',inplace=True)
#clear those '.' at the end of the state names and remove them from the dataframe, they make the table difficult to read
census2010[['Name','Remove']] = census2010['Name'].str.split(pat='.',n=1,expand=True)
census2010.drop(['Remove'],axis=1,inplace=True)
#replace strings in int columns to make their type int
census2010.replace(to_replace='(X)',value=0,inplace=True)
#change proper columns to float to allow for number queries
census2010.astype({'Total Income':'float'})
#resets index for optimal table use
census2010 = census2010.reset_index(drop=True)
#remove the United States as it is not a row in the other dataset
census2010 = census2010.iloc[1:]
#adds a year column to better map the datasets
census2010.insert(0,'Year',2010,allow_duplicates=True)    
#checking out process to tie up loose ends
print(census2010.columns)
print(census2010.info())
print(census2010.head())

#removes initial rows that don't make any sense
census2009.drop(index=census2009.index[:9],axis=0,inplace=True)
#looking at the original excel sheet, there is an excess amount of columns
#I believe that the column containing 0 entries was pandas way of making sense of there existing 2(?) tables
#we will drop it. It does not contain any information regardless
census2009.dropna(how='all',axis=1,inplace=True)
#rename columns
census2009.columns=['Name','Total Income','From federal','From state','From local','Total Spending','Operation Expense','Improvement Expense','Other Expenses','Outstanding Debt','Cash and Securities']
#remove rows with all values=NaN
census2009.dropna(axis=0,how='all',inplace=True)
#clear those '.' at the end of the state names and remove them from the dataframe, they make the table difficult to read
census2009[['Name','Remove']] = census2009['Name'].str.split(pat='.',n=1,expand=True)
census2009.drop(['Remove'],axis=1,inplace=True)
#replace strings in int columns to make their type int
census2009.replace(to_replace='(X)',value=0,inplace=True)
#change proper columns to float to allow for number queries
census2009.astype({'Total Income':'float'})
#resets index for optimal table use
census2009 = census2009.reset_index(drop=True)
#remove the United States as it is not a row in the other dataset
census2009 = census2009.iloc[1:]
#adds a year column to better map the datasets
census2009.insert(0,'Year',2009,allow_duplicates=True)    
#checking out process to tie up loose ends
print(census2009.columns)
print(census2009.info())
print(census2009.head())

#removes initial rows that don't make any sense
census2008.drop(index=census2008.index[:9],axis=0,inplace=True)
#looking at the original excel sheet, there is an excess amount of columns
#I believe that the column containing 0 entries was pandas way of making sense of there existing 2(?) tables
#we will drop it. It does not contain any information regardless
census2008.dropna(how='all',axis=1,inplace=True)
#rename columns
census2008.columns=['Name','Total Income','From federal','From state','From local','Total Spending','Operation Expense','Improvement Expense','Other Expenses','Outstanding Debt','Cash and Securities']
#remove rows with all values=NaN
census2008.dropna(axis=0,how='all',inplace=True)
#clear those '.' at the end of the state names and remove them from the dataframe, they make the table difficult to read
census2008[['Name','Remove']] = census2008['Name'].str.split(pat='.',n=1,expand=True)
census2008.drop(['Remove'],axis=1,inplace=True)
#replace strings in int columns to make their type int
census2008.replace(to_replace='(X)',value=0,inplace=True)
#change proper columns to float to allow for number queries
census2008.astype({'Total Income':'float'})
#resets index for optimal table use
census2008 = census2008.reset_index(drop=True)
#remove the United States as it is not a row in the other dataset
census2008 = census2008.iloc[1:]
#adds a year column to better map the datasets
census2008.insert(0,'Year',2008,allow_duplicates=True)    
#checking out process to tie up loose ends
print(census2008.columns)
print(census2008.info())
print(census2008.head())

#joins in the necessary tables
census = pd.concat([census2018,census2017,census2016,census2015,census2014,census2013,
census2012,census2011,census2010,census2009,census2008])
print(census)

census.to_csv('RegionalCensus.csv')

#starts to find the predicted and actual amounts of public school expenses.
#using this information, we can set up a hypothesis test
#hypothesis test: test for the alternative hypothesis, if the p-value does not favor the alternative hypothesis, we reject it in favor of the null hypothesis.
#let PredExpense = the predicted amount of expenses based on the trend line for 2014
#let ActExpense = the actual amount that the public spent for 2014
#this is the ActExpense
#ActExpense = census2018Keep[['Total Spending']]

#Null hypothesis = H0: P-value(|ActExpense - PredExpense| <= .05)
#Alternative hypothesis = HA: P-value(|ActExpense - PredExpense| > .05) 
#Is this difference significant?
#Yes, (accepting HA): then I can understand why the government does not pay for it all
#No, (accepting H0): then I do not understand why the government does not plan accordingly
#sets up a DataFrame with only total amounts

#from this information, find y where x = 2018. y = PredExpense
#now test if there is a significant difference between PredExpense and Revenue
#let Revenue = the total amount of revenue recieved by public schools 
#Null hypothesis = H0: P-value(|PredExpense - Revenue| <= .05)
#Alternative hypothesis = HA: P-value(|PredExpense - Revenue| > .05) 
#Is this difference significant?
#Yes, (accepting HA): now we will search for a reason for why they do not supply more money and who makes up the difference
#No, (accepting H0): now we will search for a reason for why there is not enough funding despite the government making a prediction and standing by it
