input_list=[5,6,2,9,7,1,10,4,2,1,11,12,2]
#	output=[[5,6],[2],[9],[7,1],[10],[4,2,1],[11,12],[2]]

l2=[]
l1=[]
l3=[]
i=0
while (i <= len(input_list)-2):
	#print(input_list[i] , input_list[i+1])
	l1=[]
	while (i <= len(input_list)-2 and input_list[i] <= input_list[i+1]):
		#if input_list[i] <= input_list[i+1]:

		l1.append(input_list[i])
		
		i=i+1
	l1.append(input_list[i])
	l3.append(l1)
	i=i+1
	l2=[]
	while (i <= len(input_list)-2 and input_list[i] >= input_list[i+1]):
		#if input_list[i] >= input_list[i+1] :
#		print(input_list[i+1] , input_list[i+2])

		l2.append(input_list[i])
		i=i+1
			
	
	l2.append(input_list[i])
	
	l3.append(l2)
	i=i+1
	
print(l3)
