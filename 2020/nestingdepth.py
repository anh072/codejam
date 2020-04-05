t = int(input())

def solve():
    s = input()
    ans = ""
    num_opening_brackets = 0
    prev = ""
    for n in s:
        if num_opening_brackets == 0 or prev == "":
            ans += "(" * int(n)
            ans += n
            prev = n
            num_opening_brackets = int(n)
        else:
            if int(n) == int(prev):
                ans += n
            elif int(n) > int(prev):
                diff = int(n) - int(prev)
                ans += "(" * diff
                ans += n
                prev = n
                num_opening_brackets = int(n)
            else:
                diff = int(prev) - int(n)
                ans += ")" * diff
                ans += n
                prev = n
                num_opening_brackets = int(n)
    
    if num_opening_brackets > 0:
        ans += ")" * num_opening_brackets
                
    return ans


for c in range(t):
    print("Case #{}: {}".format(c+1, solve()))