test_list = ["gfg","is","best","geeks"]
#		output = ['gfg','is','geeks','best'] g<is<ks<t

#print(sorted(test_list,key = lambda x : x[len(x)-1]))

list1=[]
for x in test_list :
	list1.append(x[::-1])
list1.sort()

list2=[]
for x in list1 :
	list2.append(x[::-1])	

print(list2)
	
	
	
	
	
	
	
	
	
	
	
	
