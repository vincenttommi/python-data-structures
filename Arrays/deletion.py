#Deletion - refers to removing  an existing element from  the arrayand re-organizing all elements


from array import *

vin =  array('i',[20,40,50,60,80,70])

vin.remove(80)

for x in vin:
    
    print(x)