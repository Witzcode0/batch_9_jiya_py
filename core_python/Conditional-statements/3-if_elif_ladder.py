score = float(input("Enter your score: "))

if((score <= 100) and (score >= 0)):
    if(score >= 80):
        print("Grade A")
    elif (score >= 60):
        print("Grade B")
    elif (score >= 40):
        print("Grade C")
    else:
        print("Sorry, You are failed")
else:
    print("Invalid score")
