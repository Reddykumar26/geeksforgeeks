list1 = [[4,1,6],[7,8],[4,10,8]] 
#		output=[[6,4,1],[8,7],[10,8,4]]

output=[]
for x in list1 :
	x.sort()
	output.append(x[::-1])
	
print(output)
