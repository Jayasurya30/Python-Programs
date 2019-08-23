print("**************SIMPLE CALCULATOR**************")
print("1.Addition")
print("2.Subtraction")
print("3.multiplication")
print("4.division")
S=int(input("Select the option"))
A=int(input("Enter the first number:"))
B=int(input("Enter the second number:"))
if S==1:
    C=A+B
    print("Addition of the number is:",C)
elif S==2:
    D=A-B
    print("Subtraction of the number is:",D)
elif S==3:
    E=A*B
    print("Multiplication of the number is:",E)
elif S==4:
    F=A/B
    print("Divison of the number is:",F)
else:
    print("given option is invalid")




