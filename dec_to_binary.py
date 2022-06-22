l=eval(input("enter decimal number : "))
h='' 
while l > 0:
	h = h+ str(l % 2)
	l= l //2
print(h[::-1])

k= input( " : ")
print(k)
