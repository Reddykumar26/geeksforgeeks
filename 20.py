list1=eval(input("enter list :"))
print(list1)
c=0
e=0
for x in list1:
	if x%2==0:
		c=c+1
	else:
		e=e+1
print("even",c)
print("odd",e)
