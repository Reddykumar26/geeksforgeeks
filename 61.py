test_list = [4,6,4,3,3,4,3,4,3,8,6,6]
k= 2
#		output = [4,3]
output =[]
for i in test_list :
	if i not in output :
		if test_list.count(i) > k:
			output.append(i)
print(output)
