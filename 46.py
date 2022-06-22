list_of_tuples1=[(4,8),(19,22),(28,30),(31,50)]
list_of_tuples2=[(10,12),(23,26),(15,20),(52,58)]
#l1=[]		
#	output = [((4,8),(10,12),(19,22)),((19,22),(23,26),(28,30))]  10>8 12<19

l5=[]
for i in range(len(list_of_tuples1)):
	#l4=[]
	#l3=[]
	#k=[]
	
	for j in range(len(list_of_tuples2)-1):
		#print(list_of_tuples2[i][0] , list_of_tuples2[i][1] )
		#print(list_of_tuples1[j][1] ,  list_of_tuples1[j+1][0])
		
		if  list_of_tuples2[i][0] >  list_of_tuples1[j][1]  and list_of_tuples2[i][1] <  list_of_tuples1[j+1][0] :
			new = (list_of_tuples1[i],list_of_tuples2[i],list_of_tuples1[i+1]) # update new values in the new tuple
			print('new',new)
			l5.append(new)
			break
			#print(list_of_tuples2[i][0],list_of_tuples2[i][1])
			"""l3.append(list(list_of_tuples1[i]))
			k.append(list_of_tuples2[i][0])
			k.append(list_of_tuples2[i][1])
			l3.append(k)
			#l1.append(list_of_tuples1[i][1])
			l3.append(list(list_of_tuples1[i+1]))
			#print('l3',l3)
	if len(l3) !=0:
		#print(tuple(l3))
		for i in tuple(l3):
			l4.append(tuple(i))
		#print('l4',l4)
		l5.append(tuple(l4))"""
print(l5)
