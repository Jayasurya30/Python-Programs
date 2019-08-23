n=int(input())
a=[]
b=[]
for i in range(n):
    names=input()
    score=float(input())
    a.append([names,score])
    b.append(score)
c=sorted(list(dict.fromkeys(score)))[1]
for names,score in sorted(a):
    if score == c:
        print(names)

