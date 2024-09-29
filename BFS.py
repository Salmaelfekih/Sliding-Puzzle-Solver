from numpy import array
import numpy as np
import time
import tools as t
def solve(display_graph, frame, images_refs):
    start_time = time.time()
    l1=[]
    g=[] #list of generated nodes
    j=0
    c=0
    l1.append(t.arr) #matrix list
    while(t.Final_State(l1[0]) == False):
        a,b=t.search(l1[0])
        j+=1# number of visited nodes
        l=[] #list of possible moves
        t.fill(l,a,b)
        t1=len(l)
        i= - 1
        while(i < t1 - 1):
            i+= 1
            if (len(l)!=0 and l[0]=='D'):
                arr1=t.down(l1[0],a,b)
                l.remove('D')
                l1.append(arr1)
                g.append(arr1)
                if(t.Final_State(arr1)):
                    c = 1
                    display_graph(arr1,frame,images_refs)
                    break
            if (len(l)!=0 and l[0]=='U'):
                arr2=t.up(l1[0],a,b)
                l.remove('U')
                l1.append(arr2)
                g.append(arr2)
                if(t.Final_State(arr2)):
                    c = 1
                    display_graph(arr2,frame,images_refs)
                    break
                
            if (len(l)!=0 and l[0]=='R'):
                arr3=t.right(l1[0],a,b)
                l.remove('R')
                l1.append(arr3)
                g.append(arr3)
                if(t.Final_State(arr3)):
                    c = 1
                    display_graph(arr3,frame,images_refs)
                    break
                
            if (len(l)!=0 and l[0]=='L'):
                arr4=t.left(l1[0],a,b)
                l.remove('L')
                l1.append(arr4)
                g.append(arr4)
                if(t.Final_State(arr4)):
                    c = 1
                    display_graph_fn(arr4,frame,iamges_refs)
                    break
        if(c == 1):
            break
        l1.pop(0)
        display_graph(l1[0],frame,images_refs)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time ,j ,len(g)
