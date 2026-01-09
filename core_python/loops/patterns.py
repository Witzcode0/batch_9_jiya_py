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
#       * *
#     * * *
#   * * * *
# * * * * *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num-row+1):
#         print("  ", end="")
#     for col in range(1, row+1):
#         print("* ", end="")
#     print()


# * 
# * * 
# * * * 
# * * * * 
# * * * * *

#         *
#       * *
#     * * *
#   * * * *
# * * * * *


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


# * * * * *
# * * * *
# * * *
# * *
# *

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# * * * * *
# * * * *
# * * *
# * *
# *

# * * * * * * * * * *
#   * * * * * * * *
#     * * * * * *
#       * * * *
#         * *


#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# 1
# 22
# 333
# 4444
# 55555

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(row, end="")
#     print()

# 1
# 12
# 123
# 1234
# 12345

# A
# AB
# ABC
# ABCD
# ABCDE

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(chr(col + 64), end="")
#     print()

# a
# bb
# ccc
# dddd
# eeeee

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print(chr(row + 96), end="")
#     print()

1
23
456
78910
1112131415


# A
# B  C
# D  E  F
# G  H  I  J
# K  L  M  N  O

num = 5
global_var = 1
for row in range(1, num+1):
    for col in range(1, row+1):
        print(chr(global_var + 64)," ", end="")
        global_var += 1
    print()

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

num = 5
for row in range(1, num+1):
    for col in range(1, num+1):
        if(row == 1 or row == num or col == 1 or col == num):
            print("* ", end="")
        else:
            print("  ", end="")
    print()

# * * * * *
#  *       *
#   *       *
#    *       *
#     * * * * *

#     * * * * *
#    *       *
#   *       *
#  *       *
# * * * * *

# 01010
# 10101
# 01010
# 10101
# 01010

num = 5
flag = 0
for row in range(1, num+1):
    for col in range(1, num+1):
        if(flag == 0):
            print("0 ", end="")
            flag = 1
        else:
            print("1 ", end="")
            flag = 0
    print()


num = 15
for row in range(1, num+1):
    for col in range(1, num+1):
        if(row % 2 == 0):
            print("0 ", end="")
        else:
            print("1 ", end="")
    print()

num = 9

# * * * * * * * * *
# *   *   *   *   *
# * * *   *   *   *
# *       *   *   *
# * * * * *   *   *
# *           *   *
# * * * * * * *   *
# *               *
# * * * * * * * * *
# ----------------------
# * 
# *   
# * * *   
# *       
# * * * * *   
# *           
# * * * * * * *   
# *               
# * * * * * * * * *
# -----------------------
# * * * * * * * * *
#     *   *   *   *
#     *   *   *   *
#         *   *   *
#         *   *   *
#             *   *
#             *   *
#                 *
#                 *

# https://witzcode.pythonanywhere.com/technology/2/56/?wz_tech=C%20programming&wz_category=Star-Patterns
# num = 5

# * * * * *
#  *       *
#   *       * odd
#    *       *
#     * * * * *
#     * * * * *
#    *       *
#   *       * even
#  *       *
# * * * * *
# * * * * *
#  *       * 
#   *       * odd
#    *       *
#     * * * * *
#     * * * * *
#    *       *
#   *       * even
#  *       *
# * * * * *
# * * * * *
#  *       *
#   *       * odd
#    *       *
#     * * * * *
#     * * * * *
#    *       *
#   *       * even
#  *       *
# * * * * *

# * * * * *
# *       *
# *   -   *
# *       *
# * * * * *
