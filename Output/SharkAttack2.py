#!/usr/bin/env python
# coding: utf-8

# In[1]:




# In[2]:


#we import the dataset
sa = pd.read_csv("input/attacks.csv",encoding ="latin1")


# In[3]:


#we choose the interest columns, and we create a new dataset using only them
SA = sa[["Date","Year","Type","Country","Area","Location","Activity","Name","Sex ","Age","Injury","Fatal (Y/N)","Time","Species "]]


# In[4]:


#we print all the column names to see their exact name so we can operate with them
SA.columns


# In[5]:


#we eliminate the duplicates from them
SA = SA.drop_duplicates()


# In[6]:


#we print it to see how it looks
SA


# In[45]:


#we define an hour cleaner function
def cleaner(time):
    try :
        return re.findall(r"\d{2}h00",time)[0]
    except :
        return None


# In[46]:


#we use the created function with the time columns
SA["Clean_Time"] = SA["Time"].map(cleaner)


# In[47]:


#we create a column to compare the time and the fatality of the shark attack
SA_TF = SA[["Clean_Time", "Fatal (Y/N)"]]


# In[48]:


#we drop the rows with nule sets
SA_TFclean = SA_TF.dropna(thresh=SA_TF.shape[1]-0)


# In[59]:


#we print it to see how it looks with the clean hours only
SA_TFclean


# In[63]:


#we observe the number of atacks by hour distibution
SA_TFclean2["Clean_Time"].value_counts()


# In[64]:


#we represent the hour-attacking rate with a graphic, observing that:
#THE HOURS WITH MORE ATTACKS ARE DURING THE CHANGE FROM MORNING TO AFTERNOON, WITH 11:00 IN THE MORNING AS THE LEADER
SA_TFclean["Clean_Time"].value_counts().plot()


# In[ ]:





# In[ ]:




