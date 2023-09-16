# 틀림.

# while True:
#     a,b=map(int,input().split(" "))
#     print(a+b)
#     continue
#     if EOF:
#         break

# 출력이 완료되고 아무것도 입력안했을 대 빠져나와야 하므로 except 에 EOFerror를 적어 error가 났을 때 break 하는 식.

while True:
    try:
        a,b=map(int,input().split())
        print(a+b)
    except: 
    # except EOFError:이라고 적어도 된다.
        break