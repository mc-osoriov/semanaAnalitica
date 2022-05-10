
# In[1]:


#Ejercicio 1


# In[13]:


def primos(n):
  for i in range (2, n + 1): 
    for j in range (2, i):  
        if i % j == 0:  
            break  
    else:  
        print (i)

primos(23)


# In[1]:


#Ejercicio 2


# In[2]:


def cross(a,b):
  c=[]
  c.append(a[1]*b[2]-a[2]*b[1])
  c.append(a[2]*b[0]-a[0]*b[2])
  c.append(a[0]*b[1]-a[1]*b[0])
  return c

x = [1.2,3.7,-0.25]
y = [-0.44,-2.8,7]

cross(x,y)   


# In[3]:


#Ejercicio 3


# In[4]:


import csv 
filas = []
with open("vectors.csv",'r') as file:
    csvr = csv.reader(file)
    for row in csvr:
        filas.append(row)
print(filas)

a =  [float(filas[0][0]),float(filas[0][1]), float(filas[0][2])]
b =  [float(filas[1][0]),float(filas[1][1]), float(filas[1][2])]
cr = cross(a,b)
print("a= ",a)
print("b= ",b)
print("a x b= ", cr)




