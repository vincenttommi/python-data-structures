"""
Recursion - allows a function to call itself
is a process where fixed steps of code  get executed again and again for new values



#Binary  Search using Recursion
we implement  the algorithm of binary  using python
we  use an ordered  list  of items  and design a recursive  function to take  in the list 
along with starting and ending index as input.



"""

 

#Exampleb
def bsearch(lst, idx0, idxn, val):
    if idxn < idx0:
        return None
    else:
        midval = idx0 + ((idxn - idx0) // 2)
        # Compare the search item with the middlemost value
        if lst[midval] > val:
            return bsearch(lst, idx0, midval - 1, val)
        elif lst[midval] < val:
            return bsearch(lst, midval + 1, idxn, val)
        else:
            return midval

lst = [8, 11, 24, 56, 88, 131]
print(bsearch(lst, 0, 5, 24))
print(bsearch(lst, 0, 5, 51))


