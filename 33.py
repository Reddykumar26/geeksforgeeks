list1=['a','b','c','d','e','f','g']	
list2=[1,2,3,4,5]

list3=[]
i=int(len(list1))
j=int(len(list2))
k=int(max(i,j))
n=0
m=0
for z in range(k):
	
	list3.append(list1[n])
	list3.append(list2[m])
	n=n+1
	m=m+1
	if  n==i:
		n=0
	if m==j:
		m=0
print(list3)	
