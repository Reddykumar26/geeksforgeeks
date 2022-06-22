list1= [3, 3, 3, 3, 6, 7, 5, 5, 5, 8,8, 6, 6, 6, 6, 6, 1, 1, 1, 2,2]
              
list2 = []
count = 1
for x in range(1, len(list1)):
     

    if list1[x - 1] != list1[x]:
        list2.append((list1[x - 1] * count))
        print(list2)
        count = 0
    count =count+ 1
    
print((list1[-1] * count))
list2.append((list1[-1] * count))

print(list2)
