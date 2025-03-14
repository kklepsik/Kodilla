print('Zadania dla orłów - moduł 3')

print('Zadanie 1')

numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0

for index in range(len(numbers)):
  numbers[index] = round(numbers[index], -1)

numbers.sort()
minimum = min(numbers)
maximum = max(numbers)

numbers = [number for number in numbers if number != minimum and number != maximum]

print(numbers)


mean_number = sum(numbers)/len(numbers)

print(round(mean_number))

