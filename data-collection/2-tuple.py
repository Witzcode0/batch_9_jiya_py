"""
Docstring for data-collection.2-tuple

Tuple : Immutable | odered | indexing | slicing | allow duplicate values

syntax: 

tuple_name = ()
tuple_name = tuple()
tuple_name = 10,

Example : 
tuple_name = (ele1, ele2, ..., elen);

"""


empty_tuple = tuple()
# print(type(empty_tuple)) # <class 'tuple'>
# print(len(empty_tuple))

mix_data_tuple = (1, 34.5, "bit", 34 + 86j, 1)
# print(mix_data_tuple)

# indexing (+/-)
# print(mix_data_tuple[0])
# print(mix_data_tuple[-1])

# slicing (+/-)
# print(mix_data_tuple[:-3])
# print(mix_data_tuple[:-3:-1])
# print(mix_data_tuple[:-5:-1])
# print(mix_data_tuple[-1:-5:-1])

# nums = (1,2,3,1,1,1,4,5,1)
# 'count', 'index'
# print(dir(nums))
# print(nums.count(1))
# print(nums.index(2))
# print(nums.index(1, 6))


# nums = (1,2,3,4,5)
# nums[0] = 1111 # TypeError: 'tuple' object does not support item assignment
# print(nums) 

# comma_tuple = 10,
# print(type(comma_tuple))

# xyz = 2,4,5,6,6
# function(xyz)