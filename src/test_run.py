def check_points():
    N = map(int, input().split())
    p = list(map(int, input().split()))
    c = 0
    for i in range(len(p)-2):
        if p[i+1] > p[i]:
            c += 1
            return c


T = int(input())

for j in range(1, T + 1):
    print("Case #{}: {}".format(j, check_points()))


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    K = [int(_) for _ in input().split()]

    ans = 0
    for i in range(1, N - 1):
        if K[i - 1] < K[i] and K[i] > K[i + 1]:
            ans += 1

    print("Case #%d: %d" % (t, ans))

""" Output:
4
3
10 20 14
4
7 7 7 7
5
10 90 20 90 10
3
10 3 10
Case #1: 1
Case #2: 0
Case #3: 2
Case #4: 0
"""
