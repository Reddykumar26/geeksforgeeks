list1 = ["gfg","is","best"]
list2 = [0,1,2,1,1,1,0,0,2]
#		output = ['gfg','is','best','is','is','is','gfg','gfg','best']
output=[]
for x in list2:
	output.append(list1[x])
print(output)
