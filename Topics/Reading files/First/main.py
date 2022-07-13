# read test_file.txt
test = open('test_file.txt', 'r', encoding='utf-16')

print(test.readline())
test.close()
