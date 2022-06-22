input_list = [1,2,3]

from itertools import combinations

comb = combinations([1,3,4],2) #here 2 is r (n-r)!
for i in comb :
	print(i)
