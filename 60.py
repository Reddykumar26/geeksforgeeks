test_list = [5,6,3,2,5,3,4]
k=1
#		output = [True,False,True,False,False,True]
output=[]
for i in range(len(test_list)-1) :
	#if test_list [i] - test_list[i+1] == k or test_list [i] - test_list[i+1] == -k :
	output.append(test_list [i] - test_list[i+1] == k or test_list [i] - test_list[i+1] == -k)
	#else:
	#	output.append("False")
print(output)
