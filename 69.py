test_list = [(4,5,5,5,4),(5,4,3),(5,5)]
k= 5
n=2
output=[]
#		output = [(4,5,5,4)]
for x in test_list :
	c=0
	for i in range(len(x)):
		if x[i] == k :
			c=c+1
			if c == n :
				output.append(x)
				break 
print(output)
