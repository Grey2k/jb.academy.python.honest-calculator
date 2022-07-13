# read test.txt
test = open('test.txt', 'r')

for line in test:
    print(line[0])

test.close()
