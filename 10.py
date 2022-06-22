list1=eval(input("enter list :"))
l2=list1.copy()
print(l2)
l3=[]
for i in list1:

	l3.append(i)
print(l3)

#slicing

l4=list1[::]
print(l4)

# extend

k=[]
k.extend(list1)
print(k)

#using list 

n=list(list1)
print(n)
