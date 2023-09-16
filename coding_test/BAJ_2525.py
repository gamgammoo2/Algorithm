A,B=map(int,input().split(" "))
C=int(input())

c=A*60+B+C
if c/60>=24:
    a=c//60-24
    b=c%60
    print(a,b)
if c/60<24:
    a=c//60
    b=c%60
    print(a,b)
