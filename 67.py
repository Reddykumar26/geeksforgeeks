test_input = [(4,5),(1,6),(3,1),(0,0)]
k=0
#		output= [(4,5),(1,6),(3,1)]
i = 0

l = int (len(test_input))

while i < l:
	c = 0
	j=0

	while j < len (test_input[i]):
		print(j)
		if test_input[i][j] == k :
			c=c+1
			
			if  c == len(test_input[i]):
				test_input.remove(test_input[i])
				i=i-1
				l=l-1
			
		j=j+1
	i=i+1
print(test_input)
		
			
