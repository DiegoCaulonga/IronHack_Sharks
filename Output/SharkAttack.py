#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:


#importamos nuestra tabla de datos
sa = pd.read_csv("input/attacks.csv",encoding ="latin1")


# In[3]:


#observamos la totalidad de las columnas para ver cuales nos interesan
sa.columns


# In[4]:


#creamos una tabla con display, de las columnas en la que estamos interesados
SA = sa[["Case Number","Date","Year","Type","Country","Area","Location","Name","Sex ","Age","Injury","Fatal (Y/N)","Time"]]


# In[5]:


#la imprimimos en pantalla para observar el tipo de datos que nos reportan
SA


# In[6]:


#creamos una tabla eliminando las filas duplicadas de nuestra tabla a analizar
SA1 = SA.drop_duplicates()


# In[7]:


SA1


# In[8]:


#eliminamos las filas con mas de 5 valores nulos ya que no nos interesan
SA_clean = SA1.dropna(thresh = SA1.shape[1]-5)


# In[9]:


SA_clean


# In[10]:


#analizamos las causas de los ataques de tiburones
SA_clean["Type"].value_counts()


# In[11]:


#importamos numpy como np
import numpy as np


# In[12]:


#hacemos una lista para unificar los casos de ataques no provocados
not_provoked = ["Unprovoked","Invalid","Sea Disaster","Boating","Boat","Boatomg"]


# In[13]:


#creamos un isin para poder posteriormente aplicar una formula de filtración
SA_clean.Type.isin(not_provoked)


# In[14]:


#insertamos una nueva columna, donde se concreta si el ataque fue provocado o no
SA_clean["Provoked"] = np.where(SA_clean.Type.isin(not_provoked),"Yes","No")


# In[15]:


#creamos una lista donde aparece la comparativa entre casos provocados, y el sexo de los atacados
hypothesis1 = SA_clean[SA_clean.Provoked =="Yes"][["Provoked","Sex "]]


# In[16]:


hypothesis1


# In[17]:


#analizamos la cantidas de casos de cada sexo
hypothesis1.value_counts()


# In[18]:


#mediante uno simples calculos, llegamos a la conclusion de que:
#MAS DEL 80% DE LOS CASOS DE ATAQUES DE TIBURONES EN LOS QUE HAY PROVOCACIÓN POR PARTE DE LA VÍCTIMA, SE ADJUDICAN A HOMBRES
def porcentaje(a,b,c):
    return (a*b)/c


# In[19]:


cantidad_hombres = 4589+2
porcentaje_hombres = porcentaje(cantidad_hombres,100,len(hypothesis1))


# In[20]:


print(porcentaje_hombres)


# In[21]:


hypothesis1.value_counts()


# In[34]:


hypothesis1.value_counts().plot()


# In[ ]:




