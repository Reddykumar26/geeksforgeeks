test_list = ["gfg","is","best","","i","love","","gfg"]
print(test_list)
#		output = ['gfg is best','i love','gfg']
k=""
p=0
list1=[]
for i in range(len(test_list)):
	
	if test_list[i] == k:
		if i!=0:
		
			list1.append(test_list[p:i:])
			p=i+1
		else:
			p=i+1
if test_list[-1]!=k:

	list1.append(test_list[p::])

print(list1)
list2=[]
for i in list1:
	list2.append(' '.join(i))
print(list2)
