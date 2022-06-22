list1=eval(input("enter list :"))
ele=int(input("enter element to search :"))
"""
if ele in list1:
	for x in range(len(list1)):
		if ele==list1[x]:
			print(ele,"is present at",x,"index")
	
else:
	print("not present")
"""

c=0
for x in list1:
	if x==ele:
		c=c+1
if c==0:
	print("not present")
else:
	print("present")
	
	
	
#using count also we can find  l.count("element") if it is zero not found else found
	

