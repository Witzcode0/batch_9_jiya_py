# print([1,2,3,4].append(5))

# print(print(print()))

# data = "this Is MY $1000"
# {
#     "lower": 5,
#     "upper": 3,
#     "spec-char": 4,
#     "digits" : 4,
#     "even-number": 3,
#     "odd-number": 1
# }

#       *
#     * * *
#   * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *

# nums = [1,2,3,4,5,6,7,8,9,10]
# print(nums[::-1])

import string
def lower(data):
    empty_str = ''
    upper = string.ascii_uppercase
    # print(upper)
    for ch in data:
        if ch in upper:
            empty_str += upper.index(ch)
        else:
            empty_str += ch
    print(empty_str)
lower(input("Enter something: "))