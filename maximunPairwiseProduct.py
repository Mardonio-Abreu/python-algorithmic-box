#print ("Enter the size")
size = input()

#print ("Enter the numbers")
numbers = input()
numberArray = numbers.split()

numberArray.sort()
numberArray.reverse()

print(int(numberArray[0])*int(numberArray[1]))

