#we can update  the entire  inner array  or some specific   data elements of the  inner array by 
# reassigning the values  using the array index
vincente = [[10,20,40,50,60],[30,10,20,40,50],[60,70,80,90,70,80],[12,13,14,15,16]]


vincente[2] = [11,20]
#inserts a value to the  second 2da a

vincente[0][3] =7
#inserts an aray 0indices on 3rd row

for r in vincente:
    for c in vincente:
        print(c, end="")
    print()    