def main():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    numbers[0] # Answer: 3
    numbers[-1] # Answer: 2
    numbers[3] # Answer: 1
    numbers[:-1] # Answer: [3, 1, 4, 1, 5, 9]
    numbers[3:4] # Answer: [1]
    5 in numbers # Answer: True
    7 in numbers # Answer: False
    "3" in numbers # Answer: False
    numbers + [6, 5, 3] # Answer: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

#Change the first element of numbers to "ten" (the string, not the number 10)
    numbers = [3, 1, 4, 1, 5, 9, 2]
    numbers.remove(3)
    numbers.append(10)
    print(numbers)
#Change the last element of numbers to 1
    numbers = [3, 1, 4, 1, 5, 9, 2]
    numbers.pop()
    numbers.append(1)
    print(numbers)
#Get all the elements from numbers except the first two (slice)
    numbers = [3, 1, 4, 1, 5, 9, 2]
    L = numbers
    print(L[1:])
#Check if 9 is an element of numbers
    numbers = [3, 1, 4, 1, 5, 9, 2]
    numbers.count(9)
    print(numbers.count(9))
main()