a=eval(input("enter 1st number :"))
b=eval(input("enter 2nd number :"))
c=eval(input("enter 3rd number :"))
print(min(a,b,c))
if a==b:
	print(a,"equal to",b)
elif a<b:
	print(a,"is less than",b)
else:
	print(b,"is less than",a)
