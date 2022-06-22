
list1=[]

l=int(input("enter length of list of lists :"))
for i in range(l):
	

	list1.append([])
	list1[i]=eval(input("enter list :"))
print(list1)
"""
list2=[]
c=0
for i in list1:
	if i != []:
		list2.append(i)
		c=c+1
if c==0:
	print("empty list")
else:
	print(list2)
"""
i=0
k=len(list1)
while i < k:
	if list1[i] == [] :
		list1.remove(list1[i])
		i=i-1
		k=k-1
	i=i+1
if list1 == []:
	print("empty list")
else:
	print(list1)		
