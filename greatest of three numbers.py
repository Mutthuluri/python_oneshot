a = int(input("Enter the first number :\n"))
b = int(input("Enter the second : \n"))
c = int(input("Enter the third :\n"))
if(a==b or b==c or a==c):
    print("Duplicate values found")
elif(a>b and a>c):
    print("A is greatest of three numbers")
elif(b>a and b>c):
    print("B is greatest of three numbers")
else:
    print("C is greatest of three numbers")