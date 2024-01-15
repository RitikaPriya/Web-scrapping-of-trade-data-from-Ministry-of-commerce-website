#!/usr/bin/env python
# coding: utf-8

# In[49]:


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


# In[50]:


def exportrs(year):
    # Specifying the chromedriver path
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    # Specifying the export Dataset Link
    driver.get("https://tradestat.commerce.gov.in/eidb/ecomcntq.asp")
    dropdwn = driver.find_element_by_name("yy1")
    dd = Select(dropdwn)
    

    # Select the year and press Submit
    dd.select_by_visible_text(year)
    
    write=driver.find_element_by_name("hscode")
    write.send_keys("90314100")
    driver.find_element_by_name("button1").click()

    time.sleep(1.5)
    # Convert HTML Table to Pandas Dataframe and remove index
    dfs = pd.read_html(driver.page_source)
    # Selecting 2nd and 5th columns from all rows
    selected_columns = dfs[1].iloc[:, [1, 3]]

    # Saving the selected data into a new DataFrame
    selected_dataframe = pd.DataFrame(selected_columns)
    selected_dataframe = selected_dataframe.astype(str)
    driver.close()

    return selected_columns
   


# In[ ]:





# In[52]:


required_years = ["2011-2012","2012-2013","2013-2014", "2014-2015", "2015-2016", "2016-2017", "2017-2018","2018-2019", "2019-2020", "2020-2021", 
                  "2021-2022","2022-2023", "2023-2024(Apr-Oct)"]# 

#required_years = ["2022-2023", "2023-2024(Apr-Oct)"]
rsdata = []

for data in required_years:
    abc = exportrs(data)
    rsdata.append(abc)
print(rsdata)

from functools import reduce


# In[53]:


# Assuming rsdata is your list of DataFrames

# Function to merge two DataFrames based on the 0th column
def merge_dataframes(df1, df2):
    return pd.merge(df1, df2, left_on=df1.columns[0], right_on=df2.columns[0], how='outer')

# Use reduce to iteratively merge all DataFrames in the list
combined_dataframe = reduce(merge_dataframes, rsdata)
combined_dataframe.to_csv('india_exports_Ritika.csv',index=False)

# Now, combined_dataframe contains the merged data based on the 0th column


# Quantity

# In[54]:


def exportrs(year):
    # Specifying the chromedriver path
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    # Specifying the export Dataset Link
    driver.get("https://tradestat.commerce.gov.in/eidb/ecomcntq.asp")
    dropdwn = driver.find_element_by_name("yy1")
    dd = Select(dropdwn)
    

    # Select the year and press Submit
    dd.select_by_visible_text(year)
    
    write=driver.find_element_by_name("hscode")
    write.send_keys("90314100")
    driver.find_element_by_name("button1").click()

    time.sleep(1.5)
    # Convert HTML Table to Pandas Dataframe and remove index
    dfs = pd.read_html(driver.page_source)
    # Selecting 2nd and 5th columns from all rows
    selected_columns = dfs[1].iloc[:, [1, 6]]

    # Saving the selected data into a new DataFrame
    selected_dataframe = pd.DataFrame(selected_columns)
    selected_dataframe = selected_dataframe.astype(str)
    driver.close()

    return selected_columns
   


# In[55]:


required_years = ["2011-2012","2012-2013","2013-2014", "2014-2015", "2015-2016", "2016-2017", "2017-2018","2018-2019", "2019-2020", "2020-2021", 
                  "2021-2022","2022-2023", "2023-2024(Apr-Oct)"]


#required_years = ["2022-2023", "2023-2024(Apr-Oct)"]
rsdata = []

for data in required_years:
    abc = exportrs(data)
    rsdata.append(abc)
print(rsdata)

from functools import reduce


# In[56]:


# Assuming rsdata is your list of DataFrames

# Function to merge two DataFrames based on the 0th column
def merge_dataframes(df1, df2):
    return pd.merge(df1, df2, left_on=df1.columns[0], right_on=df2.columns[0], how='outer')

# Use reduce to iteratively merge all DataFrames in the list
combined_dataframe = reduce(merge_dataframes, rsdata)
combined_dataframe.to_csv('india_exports_Ritika_qty.csv',index=False)

# Now, combined_dataframe contains the merged data based on the 0th column


# Quantity

# In[ ]:




