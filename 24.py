list1=[(),('2','3'),(),('fr'),('',''),('','','8')]
print(list1)
"""
for x in list1:
	k=int(len(x))
	if k==0:
		list1.remove(x)
print(list1)
"""
list2=[]
for x in list1:
	k=int(len(x))
	if k>0:
		list2.append(x)
print(list2)
		
