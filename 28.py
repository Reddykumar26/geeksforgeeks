list1=[{'manoj':'java','bobby':'python'},{'manoj':'php','bobby':'java'},{'manoj':'cloud','bobby':'c++'},{'prudhvi':'oops'}]
dict1={}

for x in list1:
	for k,v in x.items():
		if k not in dict1:
			dict1[k]=[]
			dict1[k].append(v)
		else:
			if v not in dict1[k]:
				dict1[k].append(v)
print(dict1)
