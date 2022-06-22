list1=eval(input("enter list :"))
list2=[]

for x in list1:
	c=0
	
	for y in range(len(list1)):
		if x==list1[y]:
			c=c+1
	if x not in list2:
		print(x,"occurs",c,"times")
		list2.append(x)

"""
for x in list1:
	k=int(list1.count(x))
	if x not in list2:
		print(x,"occurs",k,"times")
		list2.append(x)
"""		
		
		
		
