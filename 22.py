list1=eval(input("enter list :"))
print(list1)
list2=[]
list3=[]
p=0
n=0
for x in list1:
	if x==0:
		k=0
	elif x>0:
		list2.append(x)
		p=p+1
	else:
		list3.append(x)
		n=n+1
print("positive numbers :")
print(list2)	
print("no of positive numbers :",p)

print("negative numbers :")
print(list3)	
print("no of negative numbers :",n)

