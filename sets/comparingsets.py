"""


Comparing Set - is the ability to check if a given subset or superset of another set.
The result is True or False depending on elements present in sets



"""

#Example 
DaysA  = set(["Mon","Tue","Wed"])
DaysB  = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])


SubsetRes  = DaysA <= DaysB
SupersetRes  = DaysB >= DaysA

print(SubsetRes)
print(SubsetRes )