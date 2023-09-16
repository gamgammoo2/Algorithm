H,M=map(int,input().split(" "))

if 0<H<=23:
    if 0<=M<45:
        m=M+60-45
        h=H-1
        print(h,m)
    else:
        m=M-45
        print(H,m)
if H==0:
    if 0<=M<45:
        m=M+60-45
        h=H+23
        print(h,m)
    else:
        m=M-45
        print(H,m)