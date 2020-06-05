#!/usr/bin/env python
# coding: utf-8

# In[25]:


dict={'keys':["shanghai", "istanbul", "karachi", "mumbai"],'Values':["17.8", "13.3", "13.0", "12.5"]}
dist=pd.DataFrame(dict)


# In[34]:


a=10
q=int(input('enter a number'))
if a>q:
    print('your number greater')
elif a<q:
    print('your number less')
else:
    print('your nunbers are equal')


# In[48]:


y=[0,1,2,3,4,5,6]
for i in y:
    x=i*5
    print(x)
print('succesfully done')


# In[50]:


limit = 15
num = 0 
while (num +1)**2 < limit:
    num += 1
nearest_square = (num)**2
print(nearest_square)

