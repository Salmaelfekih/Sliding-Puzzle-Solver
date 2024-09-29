from numpy import array
import time
import numpy as np
import tools as t


def solve (display_graph, frame, images_refs):
    start_time = time.time()
    l1=[]#l1 is a list of matrix that we will visit
    l2=[]#l2 list of matrix already visited
    l1.append(t.arr)
    a,b=t.search(l1[0])
    print(a,b)
    
    dep=0 #number of nodes visited
    while(len(l1)!=0):
        print(a,b)
        dep+=1 
        score=[] #score list
        move=[] #list of possible moves

        for i in l1:
            score.append(t.in_place(i)+dep) #in place(i)+dep calculates the heuristic function
        a1=l1[score.index(min(score))]#matrix having the minimum score
        l2.append(a1)
        t.display_graph(a1,frame,images_refs)
        if(t.Final_State(a1)):
            t.display_graph(a1,frame,images_refs)
            break
        else:
            a,b=t.search(a1)
            t.fill(move,a,b)
            if (len(move) > 0 and move[0]=='D'):
                arr1=t.down(a1,a,b)
                if(not t.exist(arr1,l2)):
                    l1.append(arr1) 
                move.remove('D')
            if (len(move) > 0 and move[0]=='U'):
                arr2=t.up(a1,a,b)
                if(not t.exist(arr2,l2)):
                    l1.append(arr2)
                move.remove('U')
            if (len(move) > 0 and move[0] =='R'):
                arr3 = t.right(a1,a,b)
                if(not t.exist(arr3,l2)):
                    l1.append(arr3)
                move.remove('R')
            if (len(move) > 0 and move[0] =='L'):
                arr4=t.left(a1,a,b)
                if(not t.exist(arr4,l2)):
                    l1.append(arr4)
                move.remove('L')
            l2.append(a1)
            
            l1 = [x for x in l1 if not np.array_equal(np.array(x), np.array(a1))]
            t.display_graph(a1,frame,images_refs)
            
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, dep, len(l2)
