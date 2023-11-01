#insertion is a process of inserting one or more elements into an array Based
#Based on requirement an array can be inserted  at the begnining, end or any given index of array


#Example of insertiion in an array

from array import *

tommi =  array('i',[12,34,56,76,80,90,30])

tommi.insert(1,30)
for x in tommi:
    print(x)
    