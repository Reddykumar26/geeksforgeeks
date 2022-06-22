list1=eval(input("enter list :"))
s=a=0;
for x in list1:
	s=s+x
	a=a+1
print("sum :",s)
print("no of elements :",a)
print("average :",s/a)

print(sum(list1))
print(sum(list1)/len(list1))
