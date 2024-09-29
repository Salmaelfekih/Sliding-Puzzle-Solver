from numpy import array
import numpy as np
from PIL import Image,ImageTk
from tkinter import *


def menu(arr):
    empty=True 
    lis=[] 
    for i in range(3):
        for j in range(3): 
            if empty and i==2 and j==2:
                arr[i,j]=-1 
                continue
            elif empty : 
                print("Is this the empty place ?") 
                answer=input("(Y/N) : ")
                if answer.upper()=="Y":
                    empty=False
                    arr[i,j]=-1
                    continue 
            while True:
                arr[i,j]=int(input("arr["+str(i)+","+str(j)+"] = "))
                #small verfication
                if arr[i,j] not in lis and arr[i,j] in range(1,9):
                    lis.append(arr[i,j])
                    break
    
      
arr = array([[0,0,0], [0,0,0], [0,0,0]])
menu(arr)

def search(arr): # search for empty box
    for i in range(3):
        for j in range(3):
            if(arr[i,j]==-1):
                return i,j

    
def exist(arr,l):
    for i in l:
        if np.array_equal(np.array(i), np.array(arr)):
            return True
    return False

def up(arr,a,b) : # condition a!=0
    new_t = np.copy(arr)
    aux=new_t[a,b]
    new_t[a,b]=new_t[a-1,b]
    new_t[a-1,b]=aux
    a=a-1
    return new_t

def down(arr,a,b) : # condition a!=2
    new_t = np.copy(arr)
    aux=new_t[a,b]
    new_t[a,b]=new_t[a+1,b]
    new_t[a+1,b]=aux
    a=a+1
    return new_t

def left(arr,a,b) : #condition b!=0
    new_t = np.copy(arr)
    aux=new_t[a,b]
    new_t[a,b]=new_t[a,b-1]
    new_t[a,b-1]=aux
    b=b-1
    return new_t
        
def right(arr,a,b) : #condition b!=2
    new_t = np.copy(arr)
    aux=new_t[a,b]
    new_t[a,b]=new_t[a,b+1]
    new_t[a,b+1]=aux
    b=b+1
    return new_t


def Final_State(arr):
    a=array([[1,2,3],[8,-1,4],[7,6,5]])
    for i in range(3):
        for j in range(3):
            if a[i,j]!=arr[i,j]:
                return False
    return True

def fill(l,a,b):
    if(a!=2):
        l.append('D')
    if(a!=0):
        l.append('U')
    if(b!=2):
        l.append('R')
    if(b!=0):
        l.append('L')          
    
def in_place(arr): #function to determine the number of boxes that are not in place
    a1=array([[1,2,3],[8,-1,4],[7,6,5]])
    i1=0
    for i in range(3):
        for j in range(3):
            if(a1[i,j]!=arr[i,j]):
                i1+=1
    return i1


def display_graph(arr,f, images_refs):
    
    lf = []
    lab = []
    cmp = 0
    for i in range(3):
     for j in range(3):
         lf.append(Frame(f, highlightbackground="white", highlightthickness=3))
         lab.append(Label(lf[cmp], image=images_refs[arr[i, j] - 1 if arr[i, j] != -1 else 8], background="#3b53a0"))
         lab[cmp].place(x=2, y=2, width=300, height=300)
         lf[cmp].place(x=j * 300, y=i * 300, width=300, height=300)
         cmp += 1