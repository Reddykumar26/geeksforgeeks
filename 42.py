input_list=[425,500,540,450,475]
k=int(input("enter reference k value :"))

# output=TRUE

input_list.sort()
if k > int(input_list[-1] - input_list[0]):
	print("TRUE")
else:
	print("FALSE")
