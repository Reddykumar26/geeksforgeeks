i = int(input("enter starting value :"))
j = int(input("enter ending value :"))
test_list = eval (input("enter list :"))

test_list.sort()
if test_list[0] >= i and test_list[-1] <= j :
	print("YES")
else:
	print("NO")
