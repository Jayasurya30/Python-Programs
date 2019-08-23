def fib(n):
    a=0
    b=1
    if n==0:
        print(a)
    elif n==1:
        print(b)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
    for i in range(n):
        if c%2==0:
            print(c)
fib(int(input()))
