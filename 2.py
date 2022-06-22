s = input("enter string :")
result= 0
c=0
for i in  s[::-1]:
	if i.isdigit():
		result = result + (int(i) * (16**int(c)))
	else:
		result = result + ( (int(ord(i)) - 55 ) * (16**int(c)))
	c=c+1
print(result)
