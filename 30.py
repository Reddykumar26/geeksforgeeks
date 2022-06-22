list1=[1,2,3,4,5,6,7,8,9]
list2=[]

c=0
n=int(input("no of rows :"))
m=int(input("no of columns :"))
l=int(len(list1))
if n*m!=l:
	print("not possible")
else:
	for i in range((n)):

		list3=[]	
		for j in range(m):


			list3.append(list1[c])

			c=c+1
		list2.append(list3)
	print(list2)
