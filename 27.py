list1=[1,2,3,4,5,6,7]
print(list1)
list2=[1,2,3,7,10,11]
print(list2)
list3=[]
list4=[]
intersection=[]
c=[]

for x in list1 :

	if x not in list2:

		list3.append(x) 
	else :
		c.append(x)
print(list3)

for x in list2 :

	if x not in list1:

		list4.append(x)
		
print(list4)
print("common elements :",c)
