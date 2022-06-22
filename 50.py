test_list = ['gfg',3,'is',8]
key_list = ['name','id']
output=[]

# 		output = [{'name':'gfg','id':3},{'name':'is','id':8}]	
dic={}
for  j in test_list :
	if j == str(j):
		dic[key_list[0]] = j
	else:
		dic[key_list[1]] = j
		output.append(dic)
		dic={}
print(output)
			 
