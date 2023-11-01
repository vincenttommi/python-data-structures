"""

when deleting a list  you can use  a del statement if you know exactly which elements you 
want to delete or using to remove()
"""

#Example of a  deleting Elements in a list


players  = ['Madueke','Caicedo','Enzo','Reece James','Levi colwil','palmer','Sterling']
print(players)
del players[2]

print('after deleting value at index 2:')
print(players)


country = ['England','France','Argentina','Brazil','Croatia','Kenya']
print(country)

del country[4]

print('After deleting value at index 4 ')
print(country)