# syntax

# match subject:
#     case pattern_1:
#         # Code block 1
#     case pattern_2:
#         # Code block 2
#     # ...
#     case _:
#         # Default action (wildcard)

# mon - 0, tue - 1 ,....sun - 6
# mon - 1, tue - 2,....sun - 7

# day = int(input("Enter a day: "))

import datetime

match (datetime.datetime.now().weekday()):
    case 0:
        print("Today is Mon: 1. IND Vs PAK")
    case 1:
        print("Today is Tue")
    case 2:
        print("Today is Wed")
    case 3:
        print("Today is Thu")
    case 4:
        print("Today is Fri")
    case 5:
        print("Today is Sat 1. IND Vs PAK 2. BAN Vs. AUS")
    case 6:
        print("Today is San")
    case _:
        print("Invalid day")