"""
list can be updated   single or   multiple  by  giving the  slice on the left-hand side of 
assignment operator,
elements can be added to alist using append() method


"""

#usr/bin/python
teams  = ['Manchester-City','Real-Madrid','Barcelona','Chelsea','Manchester-United']

print("Value  available at index  2:")
print(teams[2])
teams[2] = "Bayern"

print("New value available at index 2:")
print(teams[2])


cities  = ['Nakuru','Nairobi','Mombasa','Eldoret','Naivasha']

print("city available at index 3:")
print(cities[3])


print("New available city 3:")
cities[3]= 'Kisumu'
print(cities[3])