
while(1):
    marks = float(input("Enter the percentage of marks you would like to\n"))
    if (marks > 80 and marks <= 100):
        print("You are distinction")
    elif (marks > 60 and marks <=80):
        print("You are good ")
    elif (marks > 40 and marks <=60):
        print("You are average")
    else:
        print("You are fail")