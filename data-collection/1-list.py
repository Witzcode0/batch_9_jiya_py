"""
List - Mutable | Orderd | indexing | slicing | allow duplicate values

syntax :

list_name = []
list_name = list()
Example: 
list_name = [ele1, ele2,...elen]
"""

# nums = [1,2,3,4,5]

# print(type(nums)) # <class 'list'>
# print(nums) # [1, 2, 3, 4, 5]
# print(len(nums)) # 5

# empty_list = list()
# print(len(empty_list))

# mix_data_list = [12, 234.43, "brijesh", 45 + 76j]
# print(mix_data_list)

nums = [1,2,3,4,5]

# indexing (+ / -)
# print(nums[0])
# print(nums[1])
# print(nums[2])
# print(nums[3])
# print(nums[4])
# print(nums[5]) # IndexError: list index out of range
# print(nums[-1])
# print(nums[-2])

# access elements using for
# for num in range(len(nums)):
#     print(nums[num])

# slicing
# list_name[start : end-1 : step-1]
# print(nums[1:4])
# print(nums[-2:-5:-1])
# print(nums[::-1])

# nums = [1,2,3]
# chars = ['a', 'b', 'c', 'd', 'e']

# Concat
# print(nums + chars)

# Replica
# print(nums*5)

# fruits = ["apple", "banana", "mango", "guava", "pinapple"]

# print(dir(fruits))

# vegs = ["onion", "potato", "tomato", "okra"]
# fruits.append(vegs)
# fruits.extend(vegs)
# fruits.insert(1, vegs)

# fruits.clear()
# fruits.pop()
# fruits.pop(2)
# fruits.remove("apple")

# print(fruits)

# copy_fruit = fruits.copy()
# fruits.reverse()
# fruits.sort(reverse=True)


# print(fruits.index("banana"))

# 'count'
# nums = [1,2,1,32,54,2,4,5,1,4,12,1,3,1,3,1,46,7,81,6]
# print(nums.count(1))


# num1, num2 = input("enter num1 & num2: ").split()
# print(num1, num2)
# print(input("enter num1 & num2: ").split())

# nums = [1,2,3,4,5]
# nums[1] = 22
# print(nums)

# nested_list = [
#     [1,2,3],
#     [4,5,6,7],
#     [8,9,10,11, [12,[13,[14, 15]]]]
# ] 
# # print(nested_list[-1])
# print(nested_list[-1][4])
# print(nested_list[-1][4][-1])
# print(nested_list[-1][4][-1][-1])
# print(nested_list[-1][4][-1][-1][-1])