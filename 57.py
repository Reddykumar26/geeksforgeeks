test_list = [(4,5),(4,),(8,6,7),(1,),(3,4,6,7)]
k=2
output=[]
#		output =[(4,),(8,6,7),(1,),(3,4,6,7)]
"""
for i in range(len(test_list)):
	if len(test_list[i]) != k :
		output.append(test_list[i])
		
print(output)
"""
i=0
l=int(len(test_list)) 
while i < l :
	
	if len(test_list[i]) == k :	
		test_list.remove(test_list[i])
		l=l-1
		i=i-1
	i=i+1
print(test_list)
