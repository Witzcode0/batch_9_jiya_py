# name = "Bharat Futurist AI"

# print(len(name))

# for ch in name:
#     print(ch, end="")

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         print("* ", end="")
#     print()

# * 
# * * 
# * * * 
# * * * * 
# * * * * *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print("* ", end="")
#     print()

# - - - - * 5 - 1 = 4
# - - - * * 5 - 2 = 3
# - - * * * 5 - 3 = 2
# - * * * * 5 - 4 = 1
# * * * * * 5 - 5 = 0

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num-row+1):
#         print("  ", end="")
#     for col in range(1, row+1):
#         print("* ", end="")
#     for col in range(1, row):
#         print("* ", end="")
#     print()


# - - - - -
# - - - -
# - - -
# - -
# -

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num-row+2):
#         print("- ", end="")
#     for col in range(1, row+1):
#         print("  ", end="")
#     print()

# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row):
#         print("  ", end="")
#     for col in range(1, num-row+2):
#         print("* ", end="")
#     for col in range(1, num-row+1):
#         print("* ", end="")
#     print()


# print(ord("A")) # 65
# print(ord("Z")) # 90
# print(ord("a")) # 97
# print(ord("z")) # 122

# print(chr(65)) # A
# print(chr(122)) # z

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(chr(col + 64), end="")
#     print()
# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(chr(row + 96), end="")
#     print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# num = 5
# global_var = 1
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(chr(global_var + 64)," ", end="")
#         global_var += 1
#     print()

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         if(row == 1 or row == num or col == 1 or col == num):
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


num = 15
for row in range(1, num+1):
    for col in range(1, num+1):
        if(row % 2 == 0):
            print("0 ", end="")
        else:
            print("1 ", end="")
    
    print()
