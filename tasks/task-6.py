# print(conditions)
# print(conditions.count(True))
# print(conditions.count(False))

# print([[True, 20 < 40, 0 == 45, 45 != 0, 0 < 85, 85 > 99, False, 0, 1].count(i) for i in (True, False)])

# print([.count(i) for i in [True, 20 < 40, 0 == 45, 45 != 0, 0 < 85, 85 > 99, False, 0, 1]])

# [expression_if_true if condition else expression_if_false for item in iterable]

# print([c if c else c for c in [True, 20 < 40, 0 == 45, 45 != 0, 0 < 85, 85 > 99, False, 0, 1]])

# p={'T':0,'F':0}
# # for r in (True,False):
# for c in [True, 20 < 40, 0 == 45, 45 != 0, 0 < 85, 85 > 99, False, 0, 1]:
#     if c == True:
#         p['T']=p['T']+1
#     else:
#         p['F']=p['F']+1
# print(p)

# print({'T': sum(c == True for c in [True, 20 < 40, 0 == 45, 45 != 0, 0 < 85, 85 > 99, False, 0, 1]),'F': sum(c != True for c in [True, 20 < 40, 0 == 45, 45 != 0, 0 < 85, 85 > 99, False, 0, 1])})