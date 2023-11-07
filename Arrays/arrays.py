"""
Array is  a container  wich can hold  a fix number  of items  and these items are of the same 
type

import terms in arrays
1 Element - each item stored in an array  is called an element
2 index  -t


*Basic Operation that can be  carried in an array
-Traverse -> printing all elements  one by one
-Insertion ->  adding an element to an array
-Deletion -> Deleting an element at given index
-Search -> Searching an element at given index or  value
-update   -> Updates an element at given index
 
"""

#Example of an array

from array import *

array1 = array('i',[10,20,30,40,50])


for x in  array1:
    print(x)