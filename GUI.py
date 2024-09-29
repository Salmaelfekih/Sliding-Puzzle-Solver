from tkinter import *
from PIL import Image,ImageTk
from win32api import GetSystemMetrics
from numpy import array
import subprocess
import numpy as np
import tools
import A_Star as a_star 
import BFS as bfs


t =Tk()
t.geometry(f"650x650+{int(GetSystemMetrics(0)/2)-300}+40")
t.title((" "*80)+"Sliding Puzzle")
global f
f=Frame(t,bg="#002960")
f.place(x=0,y=0,width=2000,height=2000)

path="images/1.png"
image = Image.open(path).resize((900, 900))
global cropped_images
global images_refs
cropped_images = []
images_refs = []
for i in range(3):
    for j in range(3):
        cropped_image = ImageTk.PhotoImage(image.crop((j * 300, i * 300, j * 300 + 300, i * 300 + 300)))
        cropped_images.append(cropped_image)
        images_refs.append(cropped_image)


def display_graph(arr):
    lf=[]
    lab=[]
    cmp=0
    for i in range(3):
     for j in range(3):
         lf.append(Frame(f, highlightbackground="white", highlightthickness=3))
         lab.append(Label(lf[cmp], image=cropped_images[arr[i, j] - 1 if arr[i, j] != -1 else 8], background="#3b53a0"))
         lab[cmp].place(x=2, y=2, width=300, height=300)
         lf[cmp].place(x=j * 300, y=i * 300, width=300, height=300)
         cmp += 1


def run_external_script_A():

    execution_time, visited_nodes, generated_nodes = a_star.solve(display_graph,f,images_refs)
    Output1.config(state=NORMAL)
    Output1.delete(1.0, END)
    Output1.insert(END, f'Time Execution is: {execution_time:.2f} seconds')
    Output1.config(state=DISABLED)

    Output2.config(state=NORMAL)
    Output2.delete(1.0, END)
    Output2.insert(END, f'Generated nodes: {generated_nodes}')
    Output2.config(state=DISABLED)

    Output3.config(state=NORMAL)
    Output3.delete(1.0, END)
    Output3.insert(END, f'Visited nodes: {visited_nodes}')
    Output3.config(state=DISABLED)

    
def run_external_script_BFS():
    
    execution_time, visited_nodes, generated_nodes = bfs.solve(tools.display_graph,f,images_refs)
    Output1.config(state=NORMAL)
    Output1.delete(1.0, END)
    Output1.insert(END, f'Time Execution is: {execution_time:.2f} seconds')
    Output1.config(state=DISABLED)

    Output2.config(state=NORMAL)
    Output2.delete(1.0, END)
    Output2.insert(END, f'Generated nodes: {generated_nodes}')
    Output2.config(state=DISABLED)

    Output3.config(state=NORMAL)
    Output3.delete(1.0, END)
    Output3.insert(END, f'Visited nodes: {visited_nodes}')
    Output3.config(state=DISABLED)
    

def run_menu():
    tools.menu(tools.arr)
    tools.display_graph(tools.arr,f,images_refs)
    

arr = array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
Button(t,text="BFS", width=10, height=2, font=("arial",20,"bold"),bd=1,fg="#fff",bg="#3697f5",command=run_external_script_BFS).place(x=1600,y=200)
Button(t,text="A Star", width=10, height=2, font=("arial",20,"bold"),bd=1,fg="#fff",bg="#3697f5",command=run_external_script_A).place(x=1350,y=200)
Button(t,text="INIT", width=9, height=2, font=("arial",20,"bold"),bd=1,fg="#fff",bg="#3697f5",command=run_menu).place(x=1100,y=200)
Output1 = Text(t, height =1,width =80, bg = "white",fg="#3697f5",font=("arial",20), padx =10,pady = 15,highlightthickness=2)
Output1.place(x=1100, y=350, width =745)
Output1.insert(END,'Time Execution is :')
Output1.config(state=DISABLED)

Output2 = Text(t, height =1,width =80, bg = "white",fg="#3697f5",font=("arial",20), padx =10,pady = 15,highlightthickness=2)
Output2.place(x=1100, y=500, width =745)
Output2.insert(END,'Generated nodes :')
Output2.config(state=DISABLED)

Output3 = Text(t, height =1,width =80, bg = "white",fg="#3697f5",font=("arial",20), padx =10,pady = 15,highlightthickness=2)
Output3.place(x=1100, y=650, width =745)
Output3.insert(END,'Visited nodes :')
Output3.config(state=DISABLED)


tools.display_graph(tools.arr,f,images_refs)


t.mainloop()
