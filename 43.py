input_list=[3,4,6,6,3,2,3,5,6,3,4,5,5,3,6]
k=int(input("reference  value :"))
m=int(input_list.index(k))
count=0
if k not in input_list:
	print("raference value not present")
else:
	for index in range(m+1,len(input_list)):
		if input_list[index] not in input_list[:m+1]:
			count=count+1
			print(input_list[index])
			break
	if count==0:
		print([])	
