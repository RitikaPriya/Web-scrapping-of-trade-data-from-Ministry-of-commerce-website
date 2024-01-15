#!/usr/bin/env python
# coding: utf-8

# In[69]:


# -*- coding: utf-8 -*-
"""
Created on Sat May  7 10:07:13 2022

@author: hrish
"""

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# In[70]:


def exportrs(year, month, driver):
    # No need to create a new driver instance in the function
    driver.get("https://tradestat.commerce.gov.in/meidb/comcntq.asp?ie=i")

    rsdata = []  # Create an empty list to store data for each combination

    for single_year in year:
        dropdwn1 = driver.find_element_by_name("yy1")
        dropdwn2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="select1"]')))
        dd1 = Select(dropdwn1)
        dd2 = Select(dropdwn2)

        dd1.select_by_visible_text(single_year)  # Select the year

        for single_month in month:
            dd2 = Select(WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="select1"]'))))
            dd2.select_by_visible_text(single_month)
            write = driver.find_element_by_name("hscode")
            write.send_keys("85414012")
            driver.find_element_by_name("button1").click()

            time.sleep(2)
            dfs = pd.read_html(driver.page_source)
            selected_columns = dfs[0].iloc[:, [1, 3]]
            selected_dataframe = pd.DataFrame(selected_columns)
            selected_dataframe = selected_dataframe.astype(str)

            # Append the data to rsdata for each combination
            rsdata.append(selected_dataframe)

            # After performing actions for the combination, navigate back to the initial page
            driver.back()

    return rsdata  # Return the collected data for all combinations

# Specific years and months you want to select
specific_years = ["2021"]
#specific_years = ["2018", "2019", "2020", "2021","2022","2023"]
required_months = [ "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC", ]#
#required_months = ["JAN", "FEB", "MAR"]

#required_months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC", ]#"JAN", "FEB", "MAR"]

# Create a WebDriver instance
driver = webdriver.Edge(EdgeChromiumDriverManager().install())

# Call the function with specific years, months, and the driver
rsdata = exportrs(specific_years, required_months, driver)

# Close the driver after collecting data
driver.close()

# Print or use the collected data as needed
print(rsdata)


# In[71]:


from functools import reduce
# Assuming rsdata is your list of DataFrames

# Function to merge two DataFrames based on the 0th column
def merge_dataframes(df1, df2):
    return pd.merge(df1, df2, left_on=df1.columns[0], right_on=df2.columns[0], how='outer')

# Use reduce to iteratively merge all DataFrames in the list
combined_dataframe = reduce(merge_dataframes, rsdata)
combined_dataframe.to_csv('india_imports_monthly.csv',index=False)

# Now, combined_dataframe contains the merged data based on the 0th column


# Quantity
# 

# In[72]:


def exportrs(year, month, driver):
    # No need to create a new driver instance in the function
    driver.get("https://tradestat.commerce.gov.in/meidb/comcntq.asp?ie=i")

    rsdata = []  # Create an empty list to store data for each combination
    radio = driver.find_elements_by_name("radioqty")
    
            # Check if there are any radio buttons found
    if radio:
           
        radio[0].click() # Select the first radio button (index 0) from the list
    
    for single_year in year:
        dropdwn1 = driver.find_element_by_name("yy1")
        dropdwn2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="select1"]')))
        dd1 = Select(dropdwn1)
        dd2 = Select(dropdwn2)

        dd1.select_by_visible_text(single_year)  # Select the year

        for single_month in month:
            dd2 = Select(WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="select1"]'))))
            dd2.select_by_visible_text(single_month)
            write = driver.find_element_by_name("hscode")
            write.send_keys("85414012")
            
            
            
            
            
            driver.find_element_by_name("button1").click()

            time.sleep(2)
            dfs = pd.read_html(driver.page_source)
            selected_columns = dfs[0].iloc[:, [1, 3]]
            selected_dataframe = pd.DataFrame(selected_columns)
            selected_dataframe = selected_dataframe.astype(str)

            # Append the data to rsdata for each combination
            rsdata.append(selected_dataframe)

            # After performing actions for the combination, navigate back to the initial page
            driver.back()

    return rsdata  # Return the collected data for all combinations

# Specific years and months you want to select
specific_years = ["2021"]
#required_month = ["JAN", "FEB", "MAR"]
#specific_years = ["2018", "2019", "2020", "2021","2022","2023"]
#required_months = [ "JAN", "FEB", "MAR","APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]#,
required_months = [ "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"] 
# Create a WebDriver instance
driver = webdriver.Edge(EdgeChromiumDriverManager().install())

# Call the function with specific years, months, and the driver
rsdata = exportrs(specific_years, required_months, driver)

# Close the driver after collecting data
driver.close()

# Print or use the collected data as needed
print(rsdata)


# In[73]:


from functools import reduce
# Assuming rsdata is your list of DataFrames

# Function to merge two DataFrames based on the 0th column
def merge_dataframes(df1, df2):
    return pd.merge(df1, df2, left_on=df1.columns[0], right_on=df2.columns[0], how='outer')

# Use reduce to iteratively merge all DataFrames in the list
combined_dataframe = reduce(merge_dataframes, rsdata)
combined_dataframe.to_csv('india_imports_monthly_qty.csv',index=False)

# Now, combined_dataframe contains the merged data based on the 0th column


# In[ ]:




