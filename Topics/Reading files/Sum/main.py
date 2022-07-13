# read sums.txt
sums = open('sums.txt', 'r')

for line in sums:
    print(sum(map(int, line.split())))

sums.close()
