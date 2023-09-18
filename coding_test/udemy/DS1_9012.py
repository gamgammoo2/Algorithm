list=[]
t=0
for i in input().split('/n'):
    if type(i)!=int:
        t=i
    else:
        list.append(i)

for j in list:
    a=0
    b=0
    for k in j:
        if k=='(':
            a+=1
        else:
            b+=1
    if a==b:
        return YES
        continue
    else:
        return NO
        continue


#문제
#괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

#어떤 자료구조와 맞을까?
#괄호가 쌍이 맞게 있다면 안쪽부터 짝지어서 지워나가보면 마지막까지 지워진다면 VPS => STACK 사용

T=int(input())

for _ in range(T):
    stk=[]
    isVPS=True
    for ch in input():
        if ch =='(':
            atk.append(ch)
        else:
            if len(stk)>0: #stk이 비어있는지 아닌지 한번 검사해줘야함. 비어있는데 pop 하면 리스트 인덱스 오류 발생
                stk.pop()
            else:
                isVPS=False
                break

    #for 문을 돌리고서 stk에서 자동 짝맺고 pop된다면 stk가 비어있을 거임
    if len(stk)>0:
        isVPS=False

    print('YES' if isVPS else 'NO') #3항 연산자로 풀이