list1=[[5,6,3,1],[7,5,3,1],[3,2],[7,3,3,2],[2,3],[9,8,1]]


list2=[]
list4=[]
list4.append(list2)
for x in range(len(list1)-1):
	list3=[]
	for i in list1[x+1]:
		if i not in list1[x]:
			list3.append(i)
	list4.append(list3)
print(list4)
