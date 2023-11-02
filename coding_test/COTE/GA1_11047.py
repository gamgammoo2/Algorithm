N, K = map(int, input().split())

lists = [int(input()) for _ in range(N)]
lists.reverse() # 제일 큰 값이 앞에 올 수 있게 뒤집기

ans = 0
for coin in lists:
    ans += K // coin
    K %= coin
    print(f'coin: {coin}, K: {K}, ans: {ans}')

print(ans)
