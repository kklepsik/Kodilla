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


print('Zadanie 2')

def build_bridge(chunk,goal):
  n = 1
  while True:
    most = n * chunk + (n - 1) * chunk / 2
    if most == goal:
      return True
    elif most > goal:
      return False
    else:
      n = n + 1

print(build_bridge(3,8))
print(build_bridge(10,30))
print(build_bridge(2, 98))