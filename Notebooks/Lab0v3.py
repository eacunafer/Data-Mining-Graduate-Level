#!/usr/bin/env python
# coding: utf-8

# # Primer Notebook
# ## ESMA 3016
# ## Edgar Acuna
# ## Agosto 20, 2019

# In[1]:


x=[3,4,5]


# In[2]:


print(type(x))


# In[1]:


# Una operacion basica elemental
z=(3+5*6)/12
print(z)
print(type(z))


# In[12]:


# Entrando el dato con el teclado
age = input("How old are you? ")


# In[13]:


print(type(age))


# In[5]:


print("Your age is", age)


# In[8]:


print("You have", 65-int(age), "years until retirement")


# In[14]:


name = "Edgar Acuna Fernandez"
length = len(name)


# In[15]:


#imprimiendo en Mayuscula e imprimiendo la longitud
big_name = str.upper(name)
print(big_name, "tiene", length, "caracteres")


# In[16]:


names = ["Ana", "Rosa", "Julia"]


# In[17]:


names[0]


# In[11]:


names[-3]


# In[18]:


#uso del condicional If
gpa = 3.4
if gpa > 2.0:
    print("Su solicitud de admision es aceptada.")


# In[13]:


# Uso  de if/else
gpa = 1.4
if gpa >= 2.5:
    print("Bienvenido al Colegio de Mayaguez!")
else:
    print("Su solicitud de admision ha sido denegada.")


# In[19]:


#Ejemplo con operadores logicos
Ana=3
Rosa=25
if (Ana <= 5 and Rosa >= 10):
    print("Ana and Rosa")


# In[15]:


if (Rosa == 500 or Ana != 5):
     print("Otra vez Ana y Rosa")


# In[20]:


range(5,10)


# In[21]:


list(range(5,10))


# In[18]:


#Ejemplo de loop
for x in range(1, 4):
    print(x, "squared is", x * x)


# In[19]:


# Otro ejemplo de loop
names = ["Ana", "Rosa", "Julia"]
for name in names:
    print(name)


# In[20]:


# Ejemplo de break y continue
for value in [3, 1, 4, 1, 5, 9, 2]:
    print("Checking", value)
    if value > 8:
        print("Exiting for loop")
        break
    elif value < 3:
        print("Ignoring")
        continue
    print("The square is", value**2)


# In[21]:


#Ejemplo de while
number = 1
while number < 200:
    print(number), 
    number = number * 2


# In[23]:


#Sumando una constante 10 a una lista
vec1=[3,4,5]
[x +10 for x   in vec1]


# In[30]:


#summando dos vectores componente a componente
vec2=[9,10,11]
for a,b in zip(vec1,vec2):
    print(a+b)


# In[31]:


#usando el modulo matematico math
import math
math.pi


# In[32]:


#usando el modulo matematico math con el alias m
import math as m
m.pi


# In[33]:


#importando solamente la funcion pi del modulo math
from math import pi
pi


# In[27]:


cos(sqrt(pi))


# In[28]:


#Leyendo un archivo de datos de la internet
import pandas as pd
df=pd.read_csv("http://academic.uprm.edu/eacuna/Animals2.csv")
df.info()


# In[30]:


df.head()


# In[31]:


df.tail(10)


# In[28]:


#Leyendo un archivo de dato almacenado en mi PC
#df=pd.read_csv("c:\esma3016\Animals2.csv")


# In[32]:


for e in __builtins__.__dict__:
    print(e)


# In[ ]:


import math 
help(math.sin)


# In[ ]:




