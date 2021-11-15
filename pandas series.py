#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


print(pd.Series())


# In[4]:


pd.Series(dtype='object')


# In[5]:


data=[10,20,30,40]


# In[8]:


pd.Series(data,index=[1,2,3,4],dtype='float64')


# In[10]:


pd.Series(data,dtype='object')


# In[17]:


ps = pd.Series(['juber','nawaj','nilesh','wasim','karan'],index=[10,20,30,40,50])


# In[18]:


ps.index


# In[25]:


ps.values[0] = 'nilesh'


# In[26]:


ps


# In[29]:


ps.values[-1]= 'ra,esh'


# In[30]:


ps


# In[31]:


s = pd.Series(['  alok','Pradnya **',' Aj$ ay'])


# In[32]:


s


# In[36]:


s.values[1] = 'pradnya'


# In[37]:


s.values[2] =' ajay'


# In[38]:


s


# In[39]:


s = pd.Series(['  alok','Pradnya **',' Aj$ ay'],name='s')


# In[40]:


s


# In[42]:


#pd.Series(data,index,dtypes,name)


# In[44]:


s = pd.Series(['ram','shym','karan','nihal','raj'],index=['A','B','C','D','E'])


# In[45]:


s


# In[46]:


s.index


# In[47]:


s.values


# In[49]:


s.describe()


# In[50]:


s.describe()


# In[55]:


s.dtype


# In[56]:


k=pd.Series([10,20,30,40,50],index=['A','B','C','D','E'])


# In[57]:


k


# In[58]:


k.index


# In[59]:


k.values


# In[60]:


k.dtype


# In[61]:


k.describe()


# In[64]:


d = pd.Series(np.arange(1,20),index=[np.arange(1,20)])


# In[65]:


d


# In[66]:


d.head()


# In[67]:


d.tail()


# In[68]:


d.nlargest()


# In[69]:


d.unique()


# In[70]:


d.nunique()


# In[82]:


s1 = pd.Series([1,2,3],index=[10,11,25])


# In[84]:


s2 = pd.Series([5,6,7,8],index=[20,52,65,81])


# In[85]:


s1


# In[86]:


s2


# In[88]:


s1


# In[89]:


s2


# In[90]:


s1+s2


# In[91]:


s1.append(s2,ignore_index=True)


# In[92]:


s1


# In[95]:


s


# In[96]:


d


# In[100]:


q=pd.Series([1,2,3])


# In[99]:


q


# In[101]:


q


# In[102]:


q.pop(0)


# In[103]:


q


# In[104]:


q.pop(1)


# In[105]:


q


# In[106]:


f = pd.Series([2,5,5,1,5,2,5])


# In[107]:


f


# In[109]:


f.nlargest()


# In[110]:


d=pd.Series([10,20,30,40,50,60])


# In[111]:


d


# In[112]:


d.nlargest()


# In[113]:


d.nlargest(keep='last')


# In[114]:


d.astype('float64')


# In[115]:


d.astype('object')


# In[116]:


d.ndim


# In[117]:


s


# In[118]:


s1 = pd.Series([1,2,3])
s2 = pd.Series([4,5,6,7])


# In[119]:


s1


# In[120]:


s2


# In[122]:


s1.corr(s2)


# In[123]:


s = s1.append(s2)


# In[124]:


s


# In[127]:


s.where(s>5,other=0)


# In[129]:


s.where(s<5,other=0,inplace=True)


# In[130]:


s


# In[132]:


# dealling wuth missing values
s = pd.Series([np.nan,10,np.nan,50,np.nan])


# In[133]:


s


# In[135]:


s.isna().sum()


# In[136]:


s.fillna('missing')


# In[137]:


s.mean()


# In[139]:


s.fillna(s.mean())


# In[140]:


s


# In[141]:


s.ffill()


# In[142]:


s.bfill()


# In[143]:


s.max()


# In[144]:


s.mean()


# In[145]:


s.median()


# In[146]:


s.min()


# In[ ]:




