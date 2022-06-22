input_list=[4,4,5,4,4,4,1,2,3,4,4,4,4,4,4,4,5,6,7,4,4,5,3,4,4,4,7,4,4,4,5,6,3,5,4,4,4,6,4,4,1,4,2,4,4]
N=15
k=4
#	output=[2,3,6]
count=0
l1=[]
for index in range(N):
	if input_list[index]==k:
		count=count+1

	
	else:
		

		if count !=0:
			l1.append(count)
		count=0
l1.append(count)
print(l1)
