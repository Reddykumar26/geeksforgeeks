l=[13,10,4,243]
for i in l:
	t=i
	s=0
	while(t>0):
		s+=t%10
		t=t//10
	print(s)
		
