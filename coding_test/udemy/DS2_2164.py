#my sol:
# N=int(input())
# cards=[]
# for i in range(1,N+1):
#     cards.append(i)
#     while len(cards)>1:
#         if len(cards)>2:
#             cards[1]=cards[len(cards)]
#             cards.pop(2)
#         else:
#             cards.pop()
# print(cards)

#문제
#N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

#이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

#예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.

#N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

#ex) N=6 -> 답:4


#sol:
#array를 이용해서 구현할 수 있을것으로 보임.
# 1,2,3,4,5,6 있으면 1버리고 2가 index0이 되고 이걸 맨 뒤로 보내면 index0는 3이 됌 
#즉, 3,4,5,6,2 다음으로는
#4,6,2,4
#2,4,6
#6,4
#4

#그럼 배열인걸 알았으니 바로 코드 작성으로 넘어가야하나? =>nono 자료구조에 따른 시간복잡도를 배웟으므로 시간복잡도를 판단해봐야함.
#맨 앞의 값을 삭제
#맨 앞의 값을 맨 뒤로 보낸다 -> 즉, 삭제/ 삽입(맨 뒤로 보임)
#배열에서 삽입/삭제는 O(N)
#문제에서 N의 최대는 500,000임. 우리는 숫자 하나가 남을때까지 해야함. 즉 N개 중에서 (N-1)번만큼을 삭제/삽입(두가지 다) 해야함 => (N-1)*(삭제 +(삭제+ 삽입))=>즉 (N-1)*3*O(N) -> 가장 큰 항을 보면되므로 시작복잡도는 O(N^2)에 해당한다. 500,000^2 (1억당 1초라고 보면되므로) 이미 문제에서 제시한 2초를 초과할 수 밖에 없음. =>시간 초과 => 다른 자료구조를 써야함.


#queue를 이용해서 사용하면 됌. queue의 삽입/삭제의 시간복잡도는 O(1)이었다.
#파이썬에서 queue 이용하려면 deque 사용해야함

from collections import deque

dq = deque()
N=int(input())
for i in range(1,N+1):
    dq.append(i)

#N=int(input())
#dq=deque(range(1,N+1)) 이렇게 줄여서 써도 된다.

print(dq)

while len(dq)>1 :
    dq.popleft() #맨앞에있는 값 빼기
    dq.append(dq.popleft()) #뺀값을 바로 맨 뒤로 넣기
print(dq)

print(dq.popleft())

#교사의 array 풀이
N=int(input())
arr=[*range(1,N+1)] # *를 range 앞에 쓰면은 값을 unpacking해서 일일이 넣어줌
#또는 for i in range(1,N+1):
#       arr.append(i) 가능.
print(arr)
while len(Arr)>1:
    arr.pop(0)
    arr.append(arr.pop(0))
    print(arr)
print(arr.pop())