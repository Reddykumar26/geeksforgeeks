list1=[[4,5,6],[2,4,5],[6,7,1,5]]
#		output = [[[4,6],[5,6]],[[2,5],[4,5]],[[6,5],[7,5],[1,5]]]
output=[]
for x in list1:
	l=[]
	for i in range(len(x)-1):
		l.append([x[i],x[-1]])

	output.append(l)
print(output)
