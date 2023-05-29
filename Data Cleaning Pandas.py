#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning in Pandas

# In[77]:


import pandas as pd


# In[143]:


df = pd.read_excel(r"C:\Users\alill\Downloads\Customer Call List.xlsx")
df


# In[144]:


df.drop(columns = 'Not_Useful_Column', inplace = True )
df


# In[145]:


df


# In[146]:


df["Last_Name"] = df["Last_Name"].str.strip('123./_')
df


# In[147]:


df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]', '')


# In[148]:


df


# In[149]:


#df["Phone_Number"].apply(lambda x: x[0:3] + '-'+ x[3:6] + '-'+ x[6:10] )

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))


# In[150]:


df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-'+ x[3:6] + '-'+ x[6:10])



# In[152]:


df["Phone_Number"] = df["Phone_Number"].str.replace('nan--', '')
#df["Phone_Number"] = df["Phone_Number"].str.replace('Na--', '')


# In[153]:


df


# In[154]:


df[['Street_Address', "State",'Zip_code']] = df['Address'].str.split(',',2, expand = True)
df


# In[155]:


df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No', 'N')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes', 'Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No', 'N')
df


# In[156]:


df =df.replace('N/a',"")

df=df.fillna('')
df


# In[157]:


for x in df.index:
       if df.loc[x, "Do_Not_Contact"] == 'Y':
           df.drop(x, inplace = True)
           
df


# In[158]:


for x in df.index:
       if df.loc[x, "Phone_Number"] == '':
           df.drop(x, inplace = True)


# In[159]:


df


# In[164]:


df = df.reset_index(drop = True)


# In[167]:


df= df.drop_duplicates()

df


# In[ ]:





# In[ ]:




