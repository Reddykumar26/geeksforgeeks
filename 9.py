list1=eval(input("enter list :"))

# slicing print(list1[::-1])
l2=[]
k=int(len(list1))
for i in range(-1,-(k+1),-1):
	l2.append(list1[i])
print(l2)

# using reversed()
l1=[1,2,3,4,5,6]
k=[]
for i in reversed(l1):
	k.append(i)
print(k)

# reverse() like sort eg l.sort() and l.reverse()
l1.reverse()
print(l1)
