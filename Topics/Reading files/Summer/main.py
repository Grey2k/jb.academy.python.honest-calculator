#  write your code here 
dataset = open('data/dataset/input.txt', 'r')

counter = 0

for line in dataset.readlines():
    if line == "summer\n":
        counter += 1

print(counter)
