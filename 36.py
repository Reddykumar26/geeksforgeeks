list1=[4252,6578,3421,6545,6676,123]
#		output=[6578,3421]
list2=[]

for x in list1:

	y=str(x)
	c=0
	for i in y:
		if y.count(i)==1:
			c=c+1
			if c==len(y):
				list2.append(x)
		
print(list2)
