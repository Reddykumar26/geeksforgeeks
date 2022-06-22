list_of_strings=['gfg','is','bet','adc']
count=0
for index in range(0,len(list_of_strings)-1):
	for char in list_of_strings[index]:
		if char  in list_of_strings[index+1]:
			count=count+1
		
			

if count==0:
	print("TRUE")
else:
	print("FALSE")
