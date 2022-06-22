"""
list1=l=["gfg","is","geeks","and","bell","cs"]
#		kth index k=0
#		output=['best','for','geeks']
list2=[]
list3=[]
list4=[]
l=[]
x=''
m=0
k=int(input("enter index :"))
c=0
lens_of_strings = []
for string in list1:
	lens_of_strings.append(len(string))
if k > min(lens_of_strings):
	print([])
else:
	for i in range(1,len(list1)):
		#print(list1[i-1],list1[i])
		#print("c",c)
	
		
		if list1[i-1][k]<list1[i][k]:
	
			list2.append(list1[c])
	
			c=c+1
		else :
			list2.append(list1[c])
			
			list2=[]
			c=c+1
		if list2 not in list3:
			print(list3)
			list3.append(list2)
	list3[-1].append(list1[-1])
	print(list3)
	for i in list3:
	
		l.append(int(len(i)))

	print(l)
	z=int(max(l))
	print(z)
	print(list3[(l.index(z))])

"""
list_of_strings=[]
k=int(input("enter index :"))
lens_of_strings=[]
if (len(list_of_strings)==0):
	print("entered empty list")
else:
	for string in list_of_strings:
		lens_of_strings.append(len(string))
	
	if k<min(lens_of_strings):
	
	
		index=0
		maxlength=0
		length=1
		end_index=0
					
		while(index<=len(list_of_strings)-2):
			while(index <= len(list_of_strings)-2 and list_of_strings[index][k]< list_of_strings[index+1][k]):
				length=length+1
				index=index+1
			print("length",length)
			if maxlength < length:
				maxlength=length
				end_index=index
			length=1
			index=index+1
		print("Max length is ",maxlength)
		print(list_of_strings[end_index-maxlength+1:end_index+1])
	else:
		print("value of k is invalid")





























