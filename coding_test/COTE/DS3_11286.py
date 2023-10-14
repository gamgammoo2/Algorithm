import heapq as hq
import sys
imput = sys.stdin.readline
min_heap=[]
max_heap=[] 

for _ in range(int(input())):
    x = int(input())
    if x : 
        if x>0:
            hq.heappush(min_heap, x)
        else:
            hq.heappush(max_heap, -x) 
    else :
        if min_heap:
            if max_heap:
                if min_heap[0] < abs(-max_heap[0])):
                    print(hq.heappop(min_heap))
                #elif min_heap[0] >abs(max_heap[0])):
                #    print(hq.heappop(max_heap))
                else:
                    print(-hq.heapop(max_heap))
            else:
                print(hq.heappop(min_heap))
        else:
            if max_heap:
                print(-hq.heappop(max_heap))
            else:
                print(0)