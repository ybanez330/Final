#!/usr/bin/env python
# coding: utf-8

# In[23]:


from qiskit import *


# In[24]:


import random


# In[25]:


qr = QuantumRegister(3)
cr = ClassicalRegister(3)


# In[26]:


qc = QuantumCircuit(qr, cr)


# In[27]:


for i in range(3):
    qc.h(qr[i])


# In[28]:


qc.measure(qr, cr)


# In[29]:


IBMQ.load_account()


# In[30]:


provider = IBMQ.get_provider('ibm-q')


# In[31]:


qcomp = provider.get_backend('ibmq_quito')


# In[32]:


job = execute(qc, backend = qcomp)


# In[33]:


result = job.result()


# In[34]:


measurement = int(list(result.get_counts().keys())[0], 2)


# In[35]:


number = measurement + 1


# In[36]:


dice_roll = random.randint(1, 6)


# In[37]:


if number == dice_roll:
    print("You guessed the number!")
else:
    print("The number was", dice_roll)

print("You chose", number)


# In[ ]:




