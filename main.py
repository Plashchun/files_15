#1
numbers = []
with open("text.txt") as file:
    data = file.read()
    for line in data.split():
        if line.isdigit():
            numbers.append(int(line))
print(numbers)
file.close()

#2
text = input("Enter text: ")
with open("data.txt", "w") as file:
   file.write(text)
file.close()

#3
N = int(input("Enter numbers: "))
numbers = []
for i in range(N):
    number = input("Enter number: ")
    numbers.append(number)

with open("numbers.txt", "w") as file:
    file.write(" ".join(numbers))
print(numbers)
file.close()

#4
import random
with open("random_numbers.txt", "w") as file:
    for i in range(100):
       number = random.randint(1, 1000)
       file.write(str(number) + "\n")
file.close()

#5
with open("text.txt") as file:
    words = file.read().split()
    print(len(words))
file.close()

#6
numbers = []
with open("text.txt") as file:
    data = file.read()
    for line in data.split():
        if line.isdigit():
            numbers.append(int(line))
    print(sum(numbers))
file.close()

#7
from collections import Counter
with open('text.txt', 'r') as f:
    text = f.read()
    lines = text.splitlines()
    counter = Counter(lines)
    top_five = counter.most_common(5)
    for i, (line, count) in enumerate(top_five):
        print(f'{i+1}) "{line}" - {count} разів')
file.close()