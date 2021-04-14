#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[2]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "02-Homework_04-Pandas_Instructions_HeroesOfPymoli_Resources_purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data_df = pd.read_csv(file_to_load)
purchase_data_df.head()


# ## Player Count

# * Display the total number of players
# 

# In[3]:


Total_Players = len(purchase_data_df["SN"].unique())
Total_Players_df = pd.DataFrame({"Total Players": [Total_Players]})
Total_Players_df


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[4]:


#calculate the number of unique items
Item_count = len(purchase_data_df["Item ID"].unique())

#calculate the average price
Average_price = round(purchase_data_df["Price"].mean(), 2)

#calculate Total Number of Purchases
Total_purchases = len(purchase_data_df["Purchase ID"])

#calculate Total Revenue
Total_revenue = sum(purchase_data_df["Price"])

#place into summary DataFrame
summary_df = pd.DataFrame({"Number of Unique Items": [Item_count],
                          "Average Price": Average_price,
                          "Number of Purchases": Total_purchases,
                          "Total Revenue": Total_revenue})

summary_df["Average Price"] = summary_df["Average Price"].map("${:.2f}".format)

summary_df["Total Revenue"] = summary_df["Total Revenue"].map("${:,.2f}".format)

summary_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[59]:


#Drop duplicate screenames
Clean_players = purchase_data_df.drop_duplicates(subset=["SN"])

#Basic Calculations
Total_players = Clean_players.count()[0]
Demographics = Clean_players["Gender"].value_counts()
Gender_percent = Demographics / Total_players 

#Convert to DataFrame
Summary_table = pd.DataFrame({"Total Count": Demographics,
                             "Percent Players": Gender_percent})

#Formatting
Summary_table["Percent Players"] = Summary_table["Percent Players"].map("{:.2%}".format)

Summary_table


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[58]:


#Group by gender + basic calculations
Total_purchase_value = purchase_data_df.groupby("Gender").sum()["Price"].rename("Total Purchase Value")
Purchase_count = purchase_data_df.groupby("Gender").count()["Price"].rename("Purchase Count")
Average_purchase_price = purchase_data_df.groupby("Gender").mean()["Price"].rename("Average Purchase Price")

#Convert to DataFrame
Summary_Table_03 = pd.DataFrame({"Purchase Count": Purchase_count,
                                "Average Purchase Price": Average_purchase_price,
                                "Total Purchase Value": Total_purchase_value,
                                "Avg Total Purchase per Person": Average_purchase_person})

#Formatting
Summary_Table_03["Total Purchase Value"] = Summary_Table_03["Total Purchase Value"].map("${:,.2f}".format)
Summary_Table_03["Avg Total Purchase per Person"] = Summary_Table_03["Avg Total Purchase per Person"].map("${:.2f}".format)
Summary_Table_03["Average Purchase Price"] = Summary_Table_03["Average Purchase Price"].map("${:.2f}".format)

Summary_Table_03


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[7]:


#Binning
Age_Demographics = [0,9.9,14.9,19.9,24.9,29.9,34.9,39.9,200]
Age_Labels = ["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]
Clean_players["Age Ranges"] = pd.cut(Clean_players["Age"], Age_Demographics, labels = Age_Labels)

#Basic Calculations 
Demographic_Total = Clean_players["Age Ranges"].value_counts()
Demographic_Percents = Demographic_Total / Total_players

#Convert to DataFrame
Summary_Table_04 = pd.DataFrame({"Total Count": Demographic_Total,
                                "Percentage of Players": Demographic_Percents,
                                })

#Sort Index
Summary_Table_04 = Summary_Table_04.sort_index()

#Formatting
Summary_Table_04["Percentage of Players"] = Summary_Table_04["Percentage of Players"].map("{:.2%}".format)

Summary_Table_04


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[12]:


#Binning
Age_Demographics = [0,9.9,14.9,19.9,24.9,29.9,34.9,39.9,2000]
Age_Labels = ["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]
purchase_data_df["Total Count"] = pd.cut(purchase_data_df["Age"], Age_Demographics, labels = Age_Labels)

#Group Data + Basic Calculations
Purchasing_data_grouped = purchase_data_df.groupby("Total Count")
Purchase_count = Purchasing_data_grouped["Total Count"].count()
Average_price = round(Purchasing_data_grouped["Price"].mean(),2)
Total_purchases = Purchasing_data_grouped["Price"].sum()
Average_pp = round(Total_purchases / Demographic_Total,2)

#Convert to DataFrame
Summary_Table_05 = pd.DataFrame({"Purchase Count": Purchase_count,
                                "Average Purchase Price": Average_price,
                                "Total Purchase Value": Total_purchases,
                                "Avg Total Purchase Per Person": Average_pp})
#Sort index
Summary_Table_05 = Summary_Table_05.sort_index()

#Formatting
Summary_Table_05 = Summary_Table_05.style.format({"Average Purchase Price":"${:.2f}",
                                                 "Total Purchase Value":"${:,.2f}",
                                                 "Avg Total Purchase Per Person":"${:.2f}"})

Summary_Table_05


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[56]:


# Basic Calculations
user_total = purchase_data_df.groupby(["SN"]).sum()["Price"].rename("Total Purchase Value")
user_average = purchase_data_df.groupby(["SN"]).mean()["Price"].rename("Average Purchase Price")
user_count = purchase_data_df.groupby(["SN"]).count()["Price"].rename("Purchase Count")

# Convert to DataFrame
top_spenders = pd.DataFrame({"Total Purchase Value": user_total, 
                          "Average Purchase Price": user_average, 
                          "Purchase Count": user_count})

# Display Table
top_spenders_sorted = top_spenders.sort_values("Total Purchase Value", ascending=False)

# Formatting 
top_spenders_sorted["Average Purchase Price"] = top_spenders_sorted["Average Purchase Price"].map("${:,.2f}".format)
top_spenders_sorted["Total Purchase Value"] = top_spenders_sorted["Total Purchase Value"].map("${:,.2f}".format)
top_spenders_sorted = top_spenders_sorted.loc[:,["Purchase Count", "Average Purchase Price", "Total Purchase Value"]]

# Display DataFrame
top_spenders_sorted.head(5)


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[68]:


# Basic Calculations + Group by Item ID & Name
purchase_counts = purchase_data_df.groupby(["Item ID","Item Name"]).count()["Price"].rename("Purchase Count")
price = purchase_data_df.groupby(["Item ID","Item Name"]).mean()["Price"].rename("Item Price")
purchases = purchase_data_df.groupby(["Item ID","Item Name"]).sum()["Price"].rename("Total Purchase Value")

#Convert to DataFrame
popular_sorted = pd.DataFrame({"Purchase Count": purchase_counts,
                               "Item Price": price,
                               "Total Purchase Value": purchases})

#Display Table
popular_sorted = popular_sorted.sort_values("Purchase Count", ascending=False)

#Formatting
popular_sorted["Item Price"] = popular_sorted["Item Price"].map("${:.2f}".format)
popular_sorted["Total Purchase Value"] = popular_sorted["Total Purchase Value"].map("${:.2f}".format)
popular_sorted = popular_sorted.loc[:,["Purchase Count", "Item Price", "Total Purchase Value"]]

popular_sorted.head(5)


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[70]:


# Basic Calculations + Group by Item ID & Name
purchase_counts = purchase_data_df.groupby(["Item ID","Item Name"]).count()["Price"].rename("Purchase Count")
price = purchase_data_df.groupby(["Item ID","Item Name"]).mean()["Price"].rename("Item Price")
purchases = purchase_data_df.groupby(["Item ID","Item Name"]).sum()["Price"].rename("Total Purchase Value")

#Convert to DataFrame
popular_sorted = pd.DataFrame({"Purchase Count": purchase_counts,
                               "Item Price": price,
                               "Total Purchase Value": purchases})

#Display Table
popular_sorted = popular_sorted.sort_values("Total Purchase Value", ascending=False)

#Formatting
popular_sorted["Item Price"] = popular_sorted["Item Price"].map("${:.2f}".format)
popular_sorted["Total Purchase Value"] = popular_sorted["Total Purchase Value"].map("${:.2f}".format)
popular_sorted = popular_sorted.loc[:,["Purchase Count", "Item Price", "Total Purchase Value"]]

popular_sorted.head(5)


# In[ ]:




