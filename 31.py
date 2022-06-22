list1=[[5,3,2],[8,6,3],[3,5,2],[3,6],[3,7,4],[2,9]]
list2=[]
c=1
k=int(input("enter row :"))
if k<=len(list1):
	for x in list1:
		if k==c:
			list2.append(x[::-1])

		else:
			list2.append(x)
		c=c+1
	print(list2)
else:
	print("out of range")
