"""

matrix is an example of two dimensional array where  each data  element is  of strictly same size

Every matrix is a two dimensional array but not viceversa
Very important for mathematics and  scientific calculations 
"""

#Example ofight  matrix 
"""

consider  in a case  of recording temperature  for 1week measured in the morning,midday,evening and midn
it can be  presented using an array and  reshape  method  available  in  numpy

"""
#example 

from numpy import *

vincente =  array(['Mon',18,20,22,17],['Tue',11,18,21,18],['Wen',20,30,40,50,60,70],['Thur',80,90,60],['fri',[1,2,3,4,5,],[
    'Sat',[18,17,16,15,20,23],['Sat',23,24,25,26,27],['Sun',13,3,4,5,6]
]])

m = reshape(vincente(7,5))


