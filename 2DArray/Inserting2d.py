"""

we can insert new data  elements at specific position by using the  insert() method and 
specifying the index
"""

#Example 

from array  import *

vincente = [[10,20,40,50,60],[30,10,20,40,50],[60,70,80,90,70,80],[12,13,14,15,16]]

vincente.insert(2,[1,2,3,4,5,6,7])

for r in vincente:
    for c in r:
        print(c,end="")
    print()  
