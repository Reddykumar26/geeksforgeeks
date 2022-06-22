""" 	enter string : 'bbbbc'
	['bbbb', 'c']
	not possible
	
	enter string : 'bbcbcac'
	['bbb', 'ccc', 'a']
	bcabcbc
"""
str1 = eval(input("enter string : "))
len_string = len(str1)
str2 = ''
list1 =[]
for i in str1.lower():
	if i not in str2:
		str2 = str2+i
str3=str1.lower()
for i in str2:
	list2=''
	k = str3.count(i)
	list2=list2+(i*k)
	list1.append(list2)
print(list1)
str4 =[]
l = 0
for i in list1:
	if l < len(i):
		l=len(i)
		remove = i
str4.extend(remove)
list1.remove(remove)
if l > (len_string+1)//2 or (len_string == None or len_string == 0):
	print("notpossible")
else:	
	a=0
	j=1
	for h in range(len(str1)):
		for i in list1:
			if  a < len(i):
				str4.insert(j,i[a])
				j=j+2					
		a=a+1
	print(''.join(str4))

			
	
