file = open("sample.txt", "r")

# print(file.read())
# print(file.read(9))
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

print(file.readlines())

['this is a line - 1\n', 'this is a line - 2\n', 'this is a line - 3\n', 'this is a line - 4\n', 'this is a line - 5']