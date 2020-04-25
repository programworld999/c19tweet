#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import requests
from bs4 import BeautifulSoup
import json
import datetime
import time
import c19tweet


# In[3]:


url = "https://api.covid19india.org/data.json"
c19_data = requests.get(url)
c19_data = json.loads(c19_data.content)
todayData = (len(c19_data["cases_time_series"])-1)


# In[4]:


c19_data = c19_data["cases_time_series"][todayData]


# In[5]:


def tweetNow(content):
#     tweetData = "Covid19India Update "+content["date"]+" \n Total:\n  Confirmed: "+content["totalconfirmed"]+"\n  Active: "+str(int(content["totalconfirmed"])-int(content["totalrecovered"])-int(content["totaldeceased"]))+"\n  Recovered: "+content["totalrecovered"]+"\n  Death: "+content["totaldeceased"]+""
    tweetData = r"Covid19India Update "+content["date"]+" \n    Total:\n        Confirmed: "+content["totalconfirmed"]+"\n        Active: "+str(int(content["totalconfirmed"])-int(content["totalrecovered"])-int(content["totaldeceased"]))+"\n        Recovered: "+content["totalrecovered"]+"\n        Death: "+content["totaldeceased"]+"\n    Daily Data:\n        Confirm: "+content["dailyconfirmed"]+"\n        Recovered: "+content["dailyrecovered"]+"\n        Death: "+content["dailydeceased"]+"\n#COVID19 #IndiaFightsCorona"

    c19tweet.Tweet(tweetData)


# In[6]:


x = datetime.datetime.now()
run = 1
while(run):
    if(c19_data["date"]==x.strftime("%d %B ")):
        tweetNow(c19_data)
        run = 0


# In[ ]:




