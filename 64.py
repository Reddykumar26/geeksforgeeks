input_arr = [1,2,2,3,4,5]
#		output = 2 2 3 4 5

for i in range(len(input_arr)-1):
	if i == 0:
		
		print(input_arr [i+1],end=" ") 
			
	else:		
			 
		if input_arr[i-1] <= input_arr [i+1]:
			print(input_arr [i+1],end=" ")
		else:
			print(input_arr [i-1],end=" ")
		
print()
