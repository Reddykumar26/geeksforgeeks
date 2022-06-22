list1= [['a','b',1,2],['c','d',3,4],['e','f',5,6]]
#		output = {('a','b'):(1,2),('c','d'):(3,4),('e','f'):(5,6) }
dic={}
for x in list1:
	
	dic[tuple(x[:2:])]=tuple(x[2::])
print(dic)
