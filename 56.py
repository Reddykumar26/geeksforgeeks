test_input = ["gfg_1",4,6,"gfg_2",3,"gfg_3",9,2] 
t= 'gf'
#		output = {"gfg_1":[4,6],"gfg_2":[3],"gfg_3":[9,2]}

dic = {}

i=0
p=0
while i< len(test_input):
	
	if t in str(test_input[i]):
		if i == 0 :
			k = test_input[i]
			p=p+1
		else:

			dic[k]=test_input[p:i]
			k = test_input[i]		
			#print(dic)
		i=i+1
		p=i
	else:
		
		i=i+1	
if test_input[-1] != k:
	dic[k]=test_input[p:]

else :
	dic[k] = []
	
print(dic)
	
	
			
		

			
	


