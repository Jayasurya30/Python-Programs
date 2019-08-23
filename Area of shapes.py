print("1.Triangle")
print("2.square")
print("3.rectangle")
print("4.parallelogram")
S=int(input("Select your option:"))
if S==1:
    b=int(input("Enter the base:"))
    h=int(input("Enter the height:"))
    B=1/2*b*h
    print("Area of triangle is:",B)
elif S==2:
    a=int(input("Enter the area:"))
    A=a*a
    print("Area of square:",A)
elif S==3:
    w=int(input("Enter the width:"))
    h=int(input("Enter the height:"))
    W=w*h
    print("Area of rectangle:",W)
elif S==4:
    b=int(input("Enter the base:"))
    h=int(input("Enter the height:"))
    H=b*h
    print("Area of parallelogram:",H)
else:
    print("The given option is invalid")
