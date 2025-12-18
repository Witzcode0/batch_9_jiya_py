# num = 9
# if (num % 2 != 0):
#     for row in range(1, num+1):
#         for col in range(1, row+1):
#             if col == 1:
#                 print("- ", end="")
#                 continue
#             if(row % 2 != 0):
#                 print("- ", end="")
#             else:
#                 print("  ", end="")
#         for col in range(num-row, 0, -1):
#             if row == 1:
#                 print("* ", end="")
#                 continue
#             if(col % 2 != 0):
#                 print("* ", end="")
#             else:
#                 print("  ", end="")
#         print()

num = 5
flag =(num//2) + 1
if (num % 2 != 0):
    for row in range(1, num+1):
        for col in range(1, num+1):
            if (row == 1 or row == num or col == 1 or col == num):
                print("* ", end="")
            else:
                if (row == flag) and (col == flag):
                    print(num, end=" ")
                else:
                    print("  ", end="")
        print()