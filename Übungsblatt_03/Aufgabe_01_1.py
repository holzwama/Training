def ggt(numbers):
	for i in range(0, len(numbers)-1):
		while numbers[1]:      
			numbers[0], numbers[1] = numbers[1], numbers[0] % numbers[1]
		numbers[1] = numbers[i+1]
		
	return numbers[0]

lis = [12, 3 , 6]

