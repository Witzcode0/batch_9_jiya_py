# nums = [6,7,34,5,21,8,0,1,4,-5,-8,-4,554]
# pivot = nums[len(nums)//2]
# left_child = []
# right_child = []

# for num in range(len(nums)):
#     if nums[num] < pivot:
#         left_child.append(nums[num])
#     else:
#         right_child.append(nums[num])
# print(left_child)
# print(right_child)

# def insert(root, key):
#     if root is None:
#         return {"data": key, "left": None, "right": None}

#     if key < root["data"]:
#         root["left"] = insert(root["left"], key)
#     else:
#         root["right"] = insert(root["right"], key)

#     return root

# {"data": 50, "left": None, "right": None}

# def bst_sort(arr):
#     root = None

#     # Build BST
#     for x in arr:
#         root = insert(root, x)
#         print(x)
#         print("T1 : ", root)

#     # Get sorted result using inorder traversal
#     result = []
#     inorder(root, result)

#     return result


# def inorder(root, result):
#     if root is not None:
#         inorder(root["left"], result)
#         result.append(root["data"])
#         print("T2",result)
#         inorder(root["right"], result)

# def bst_sort(arr):
#     result = []
#     root = {
#         'data': 50, 
#         'left': {
#                 'data': 30, 
#                 'left': {
#                         'data': 20, 
#                         'left': None, 
#                         'right': None
#                     }, 
#                 'right': {
#                     'data': 40, 
#                     'left': None, 
#                     'right': None
#                     }
#                 }, 
#         'right': {
#             'data': 70, 
#             'left': {
#                 'data': 60, 
#                 'left': None, 
#                 'right': None
#                 }, 
#             'right': {
#                 'data': 80, 
#                 'left': None, 
#                 'right': None
#                 }
#             }
#         }
#     inorder(root, result)
#     return result

# arr = [50, 30, 20, 40, 70, 60, 80]
# sorted_arr = bst_sort(arr)
# print("Original:", arr)
# print("Sorted:", sorted_arr)

