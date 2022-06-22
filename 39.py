list_of_dict=[{'gfg':2,'is':8,'good':3},{'gfg':9,'for':10,'geeks':9},{'love':3}]
key='good'
l=[]
#		output=[{'gfg':2,'is':8,'good':3},{'gfg':9,'for':10,'geeks':9}]
for dic in list_of_dict:
	if key in dic.keys():
		l.append(dic)
print(l)
"""

pos=0
for i in range(len(list_of_dict)):
	print(i)
	
	count=0
	for k in list_of_dict[pos].keys():
		if key==k:
			count=count+1
		
	print('count',count)
	print('pos',pos)	
	if count==0:
		
		
		del	list_of_dict[pos]
		pos=pos-1
	pos=pos+1
print(list_of_dict)
"""
