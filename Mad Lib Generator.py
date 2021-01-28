#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Import module
import tkinter


# In[5]:


from tkinter import *


# In[6]:


#Create Display Window
root = Tk()
root.geometry('400x400')
root.title("Mad Lib Generator")
Label(root,text='Mad Lib Generator\n Have fun!',font='arial 20 bold').pack()
Label(root,text='Click any one :',font = 'arail 15 bold').place(x=40,y=80)


# In[8]:


#Define Function
def madlib1():
    animals = input("Enter the name of an animal:")
    profession = input("Enter a profession name:")
    cloth = input("Enter a name of cloth:")
    things = input("Enter a thing:")
    name = input("Enter a name:")
    place = input("Enter a place name:")
    verb = input("Enter a verb in ing form:")
    food = input("Enter a food item name:")
    print("Say",food,", the photographer said as the camera flashed!",name,"and I had gone to",place,"to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as",animals,"pretending to be a",profession,". When we saw the second photo, it was exactly what I wanted. We both looked like",things,"wearing",cloth,"and",verb,"--exactly what I had in mind")
    


# In[9]:


Button(root,text="The Photographer",font="arial 15",command=madlib1,bg='ghost white').place(x=60,y=120)


# In[10]:


root.mainloop()


# In[ ]:




