test_list = [4,5,5,5,3,3,8,2,2,2]
k= 3
#		output = 5,2
c=1
list1=[]
for  i in range(len(test_list)-1):
	if test_list[i] == test_list[i+1]:
		c=c+1
		if c == 3:
			list1.append(test_list[i])
			c=0
for i in range(len(list1)-1):
	print(list1[i],end=',')
print(list1[-1])

