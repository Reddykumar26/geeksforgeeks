list1 =[2345,8786,2478,8664,3568,28]
k=int(input("enter number :"))
#		output=[1,4342,34,4220,124,4]

list3=[]
for x in list1:
	y=str(x)
	list2=''
	for i in y:
		n=int(i)
		j=n-k
		if j>=0:
			list2=list2+str(j)
	print(list2)
	list3.append(int(list2))
print(list3)			
