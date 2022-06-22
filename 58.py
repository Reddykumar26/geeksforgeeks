test_str = "667,34,2"
#		output = [(6,6,7),(3,4),(2,)]

test=test_str.split(',')
print(test)
output=[]
for i in test:
	list1=[]
	for j in i :
		j =int(j)
		list1.append(j)
	output.append(tuple(list1))
print(output)




"""
i=0
p=0
while i < len(test_str):
	if test_str[i] == ',':
		g= list[int(test_str[p:i:])]
		t = tuple(g)
		print(test_str[p:i:])
		list1.append(t)
		p = i+1
	i=i+1
g=test_str[p::]
list1.append(tuple(g))
print(list1)
"""
