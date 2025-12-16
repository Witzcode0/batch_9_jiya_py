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