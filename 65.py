input_list = [1,2,3]
#	output = 1 2 3	  1 3 2
"""
for i in input_list :
	for j in input_list :
		for k in input_list :
			if i != j and j != k and k != i :
				print(i,j,k)
"""
from itertools import permutations

comb = permutations([1,3,4],3) # change 2 here for obervations
for i in comb :
	print(i)
