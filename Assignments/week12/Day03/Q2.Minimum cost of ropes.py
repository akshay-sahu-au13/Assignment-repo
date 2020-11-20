# https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1

def minCost(a, n):

    heap = []
    for i in a:
        heapq.heappush(heap, i)

    c, m = 0, 0
    while n > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        m = a+b
        c = c+m
        heapq.heappush(heap, m)
        n -= 1

    return c
