string = eval(input('enter string : '))
output = ''
for i in string.split():
	output=output+i[::-1]+' '	
print(output)
"""s=eval(input('enter string :'))
l=''
i=''
for j in s :
	if j==' ':
		l=l+i[::-1]+' '
		i=''
	else :
		i=i+j
l=l+i[::-1]
print(l.strip())
"""


		
