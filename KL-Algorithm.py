def Dvalue():                               
    c3 = []                                 # Variable to store the D-values                                          
    e=0
    f=0
    D=0
    
    #PRINTING THE D VALUES
    print('c1=',update_c1)
    print('c2=',update_c2)
    for nm in c1:                           # We are in set c1
        for nd in M.neighbors(nm):          # Getting neighbour nodes near to nodes in c1
            for x in update_c1:             # Checking each neighbor nodes with c1-->if matches neighbor node is in c1 
                if nd==x:
                    f=f+1
            for mn in update_c2:            # Checking each neighbor nodes with c2-->if matches neighbor node is in c2 
                if nd==mn:
                    e=e+1
        D=e-f                               # Calculating D value
        c3.append(D)                        # Storing in matrix c3
        f=0
        e=0
    for nm in c2:                           # We are in se c2
        for nd in M.neighbors(nm):          # Getting neighbour nodes near to nodes in c2
            for x in update_c2:             # Checking each neighbor nodes with c1-->if matches neighbor node is in c1 
                if nd==x:
                    f=f+1
            for mn in update_c1:            # Checking each neighbor nodes with c2-->if matches neighbor node is in c2 
                if nd==mn:
                    e=e+1
        D=e-f
        c3.append(D)                        # Storing the values into c3
        f=0
        e=0
    print('D-values=',c3)



    #PRINTING GAIN VALUE
    c5={}                                                       # Listing all gain values 
    for xx in c1:                                               # Calculating gain
        for yy in c2:
            if yy in M.neighbors(xx):
                g=c3[c4.index(xx)]+c3[c4.index(yy)]-2
                c5[xx,yy]=g
            else:
                g=c3[c4.index(xx)]+c3[c4.index(yy)]
                c5[xx,yy]=g
    print('Gains=',c5)
    maxv = max(c5.values())                                     # Find the maximum value
    max_key=None
    for key, value in c5.items():                               # Finding the index
        if value == maxv:
            max_key = key
    print('Max gain=',maxv,'Nodes to be swapped=',max_key)
    all_gain.append(maxv)
    

    if len(c1)!=1:                                              # Swpping and updating the cutsets c1 and c2
        c1.remove(max_key[0])
        c2.remove(max_key[1])
        update_c1.remove(max_key[0])
        update_c1.append(max_key[1])
        update_c2.remove(max_key[1])
        update_c2.append(max_key[0])
        print('After swapping c1',update_c1)
        print('After swapping c2',update_c2,'\n')
    
    c4.clear()                                                  # Resetting cutsets to find for next loop eleminating the swapped nodes
    for x in c1:
        c4.append(x)
    for x in c2:
        c4.append(x)
    
    return all_gain         
    return update_c1        
    return update_c2
    
#   *******************
#       **********
# MAIN PROGRAM STARTS HERE
#       **********
#   *******************


import networkx as nx                                           # Importing networkx
import matplotlib.pyplot as out                                 
M=nx.Graph()
M.add_nodes_from([1,2,3,4,5,6,7,8])                             # Fixing nodes
M.add_edges_from([(1,3),(2,3),(4,6),(5,6),(3,7),(6,7),(7,8)])   # Fixing edges 

#ADDING CUTSETS
c1 = [1,5,6,7]                      # Cutset c1
c2 = [2,3,4,8]                      # Cutset c2
update_c1=[]                        # Store updated c1 
update_c2=[]                        # Store updated c2
for cr in c1:                       # Appending updated cutsets
    update_c1.append(cr)
for cr in c2:
    update_c2.append(cr)
full_c1=[]                          # Stores the final best cutset c1
full_c2=[]                          # Stores the final best cutset c2
all_gain=[]                         # Stores all max gain values from each swapping
c4=[]
cumulative_gains=[]                 # Stores the cumulative gains 
final_c1=[]                         # Stores the final best cutset c1
final_c2=[]                         # Stores the final best cutset c2
Sum=0                               # Variable to store and print cumulative gains
for x in c1:                        # Appending c1 nad c2 in c4                        
    c4.append(x)
for x in c2:
    c4.append(x)
for ii in update_c1:                # Loop to initiate the KL-Algorithm
    Dvalue()                        # Calling function Dvalue()
    full_c1=full_c1+update_c1       # Appending all the nodes in update_c1 after each iteration 
    full_c2=full_c2+update_c2       # Appending all the nodes in update_c2 after each iteration
                            
for ov in all_gain:                 # Loop for cumulative gain
    Sum=Sum+ov
    cumulative_gains.append(Sum)
print('\n\nAll maximun gains from each swapping=',all_gain)
print('Cumulative_gains=',cumulative_gains)
val=cumulative_gains.index(max(cumulative_gains))                               # Finding the maxing cumulative gain
jjj=val*len(update_c1)
while (val*len(update_c1)<=jjj<=(val*len(update_c1))+(len(update_c1)-1)):       # Final best cutsets 
    final_c1.append(full_c1[jjj])
    final_c2.append(full_c2[jjj])
    jjj=jjj+1
print('The best partitioning cutset is: c1=',final_c1,'c2=',final_c2)

