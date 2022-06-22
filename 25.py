list1=eval(input("enter list :"))
print(list1)

list3=[]
for x in list1:
	k=int(list1.count(x))
	
	if k>1 and x not in list3:
		
		list3.append(x)

print(list3)
