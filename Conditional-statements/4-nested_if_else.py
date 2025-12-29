age = int(input("Enter Age: "))

if age >= 18:
    weight = float(input("Enter Weight: "))
    if weight >= 50:
        print("You can donate")
    else:
        print("You can not donate")
else:
    print("You can not donate")