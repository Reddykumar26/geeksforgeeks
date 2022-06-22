test_arr = [[1,3,3],[2,1,2],[3,2,1]]
#test_arr = [['java',1995],['c++',1983],['python',1989]]
arr = test_arr
i=0
for k in range ((len(test_arr[0]))):
	
	for x in range(len(test_arr)-1):
		if arr[x][i] > arr [x+1][i]:
			t = arr[x]
			arr[x] = arr [x+1]
			arr[x+1] = t

	i=i+1
	print("sorted array specific to column ",i,":",arr)
	arr = test_arr
	
