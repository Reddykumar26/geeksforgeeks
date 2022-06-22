"""
list1 = eval(input("enter list :"))
value= eval(input("enter value :"))
s = 0
for i in range(len(list1)):
	list2 = []
	s=0
	
	for j in range(len(list1)):

		#if list1[i] == value:
		#	print(value)
		#	exit()

		s=s+int(sum(list1[i:j+1]))

		list2.extend(list1[i:j+1:])
		print(list2)
		print(sum(list2))
		
		if s == value and len(list2) > 2:
			print(list2)
			print(value)
		
			exit()

		list2=[]

		s = 0
	
if s ==0:
	print("no  elements are matching")
	
"""
list1 = eval(input("enter list :"))
value= eval(input("enter value :"))
s = 0
from itertools import combinations
for i in range(1,len(list1)+1):
	c=combinations(list1,i)
	#print(i)
	for i in c:
		if  sum(i) == value and len(i) > 2 :
			s=value
			print(i)
			print(value)
			exit()
		#print(i)
		#print(sum(i))
	
if s==0:
	print("cannot be created")
	
	
	
	
	
	
	
	
	
	
	
	
	
