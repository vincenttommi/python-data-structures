""""


Python-Maps

is also called ChainMap - is a type of  data  structure  to manage multiple dictionaries
together as one unit.
it Eliminates any duplicate keys by  containing keys and value pairs in a specific sequence


#Example 
#creating a ChainMap

we create two dictionaries  and club them using the ChainMap method from the  collection library
Then we  print the  keys  and values of the result  of the combinationof dictionaries
if there are duplicate keys, then only the  value  from first key is preserved

"""

#Example
import collections

dict1  = {'day1':'Mon','day2':'Tue','day3':'Wen'}
dict = {'day4':'Thur','day5':'Fri'}


res  = collections.ChainMap(dict1,dict)


#creating a single dictionary

print(res.maps,'\n')



print('Keys  = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()



#Find  a specific  value  in the result

print('day1 in res:{}'.format(('day1' in res)))
print('day3 in res:{}'.format(('day2' in res)))
print('day4 in res:{}'.format(('day4' in res)))
print('day5 in res:{}'.format(('day5' in res)))



