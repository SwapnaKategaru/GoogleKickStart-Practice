# ################### Problem 1 ###################

# N - No.of houses for sale
# B - Budget
# A - Price of i(th) house
# T - No.of test cases

def solve():
    N, B = map(int, input().split())
    A = list(map(int, input().split()))
    c = 0
    for i in range(len(A)):
        if B >= A[i]:
            B -= A[i]
            c += 1
    return c


T = int(input())
for j in range(1, T + 1):
    print("Case #{}: {}".format(j, solve()))

""" Output:
2
4 100
10 10 20 40
Case #1: 4
3 1000
1111 1111 1112
Case #2: 0 

3
4 100
20 90 40 90
Case #1: 2
4 50
30 30 10 10
Case #2: 3
3 300
999 999 999
Case #3: 0 """


# ################### Problem 2 ###################

T = int(input())
for x in range(1, T + 1):
    N, P = map(int, input().split())
    S = map(int, input().split())
    S = sorted(S, reverse=True)
    hours = sum(S[0] - s for s in S[:P])
    for i in range(1, N - P + 1):
        hours -= (S[i - 1] - S[i]) * (P - 1)
        hours += S[i] - S[P + i - 1]
        if hours < y:3
            y = hours
    print("Case #{}: {}".format(x, y), flush=True)

""" Output:
3
4 3
3 1 9 100
Case #1: 14
6 2
5 5 1 2 3 4
Case #2: 0
5 5
7 7 1 7 7
Case #3: 6 """


# ################### Problem 3 ###################


