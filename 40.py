input_list=[2,7,4,1,9,2,10,3,1,5]
output_list=[]
k=int(input("enter k value :"))
# k=4	output=[9,10]
for index in range(1,len(input_list)-1):
	if input_list[index]-input_list[index-1] > k and input_list[index]-input_list[index+1] > k:
		output_list.append(input_list[index])
print(output_list)
