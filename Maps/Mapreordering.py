"""


Reordering in python

if we change the order  of dictionaries  while clubbing them in above example
we see  the positionof elements  get interchanged as if they  are in continuos chain

"""

#example of reordering
import collections

dict1 = {"player1":'cole palmer',"player2":'Raheem Sterling',"player3":'Reece james'}
dict2  = {"player4":'Levi Colwil',"player5":'Moises Caicedo',"player6":'Conor Callagher'}



res1  =  collections.ChainMap(dict1, dict2)
print(res1.maps,'\n')


res2  = collections.ChainMap(dict2, dict1)
print(res2.maps, '\n')