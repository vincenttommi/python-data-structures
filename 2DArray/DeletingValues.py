"""
We can delete  the entire  inner array or some specific  data elements  of the inner
array by reassinging the values using the del()method with index
for removing specific data elements in one  of the inner arrays we use  update process
"""

#Examples

marks  = [[100,20,40],[39,56,78,90,78],[34,50,60,70,80],[56,70,80,90]]


del marks[2]

#looping data from the 2dimensional array
for  r in marks:
    for c in r:
        print(c, end="")
        print()