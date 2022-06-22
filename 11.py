list1=eval(input("enter list :"))
ele=eval(input("enter element to search :"))
if ele in list1:
	c=0
	for x in range(len(list1)):
		if ele==list1[x]:
			c=c+1
			print(ele,"is present at",x,"index")
	print(ele,"occurs",c,"times")
	
else:
	print("not present")
print(list1.count(ele))
