test_list = [7,3,7,6,4,9]
k=2
#		output = [7,3,4,6,7,9]
list1=test_list[k::]
output=test_list [:k:] + sorted(list1)
print(output)
