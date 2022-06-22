#method 1
"""
list1=eval(input("enter string list:"))
list2=[]

for x in list1:
	k=x.replace('a','g')
	print(x)
	print(k)
	list2.append(k)
print(list2)
"""
"""
#method 2 
list1=eval(input("enter string list:"))
list2=",".join(list1)
print(list2)
k=list2.replace('a','b').replace('k','n')
print(k)
l=k.split(',')
print(l)
"""
#method 3(own long method)

list1=eval(input("enter string list:"))
list2=[]
element1=str(input("enter first element to replace :"))
r1=str(input("first element replace with :"))
element2=str(input("enter second element to replace :"))
r2=str(input("second element replace with :"))
for x in list1:
	x=list(x)
	print("x",x)
	for y in x:
		y=str(y)
		print("y",y)
		if y==element1:
			k=x.index(y)
			print("k",k)
			x.insert(k,r1)
			del x[k+1]
		if y==element2:
			k=x.index(y)
			print("k",k)
			x.insert(k,r2)
			del x[k+1]
	print("new x:",x)
	list3=str()
	for i in x:
		list3=list3+i
	print(list3)
	list2.append(list3)

print(list2)

