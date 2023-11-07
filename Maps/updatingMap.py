""""
when the  element of dictionary is  updated , the result  is instantly updated  in the result
of the  ChainMap.

"""
#Example 
import collections

dict1 = {"player1":'cole palmer',"player2":'Raheem Sterling',"player3":'Reece james'}
dict2  = {"player4":'Levi Colwil',"player5":'Moises Caicedo',"player6":'Conor Callagher'}

res  = collections.ChainMap(dict1,dict2)
print(res.maps, '\n')


dict2['player4'] = 'Noni Madueke'
print(res.maps, '\n')