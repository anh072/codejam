import sys

def solve(B):

    print(m)
    sys.stdout.flush()
    s = input()
    if s == "N" or s == "Y:
        return
    solve(B)

T, B = map(int, input().split(" "))
for _ in range(T):
    solve(B)