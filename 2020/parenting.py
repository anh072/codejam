from collections import defaultdict

t = int(input())

def change_assignee(current):
    return "C" if current == "J" else "J"

def solve():
    num_tasks = int(input())
    intervals = []
    assignee = "C"
    for i in range(num_tasks):
        interval_str = input()
        interval = interval_str.split(" ")
        interval.append(i) # append order of the task
        intervals.append(interval)
    intervals.sort(key=lambda i: int(i[0]))
    lookup = defaultdict(list)
    ans = [""] * len(intervals)

    for j in intervals:
        if not lookup:
            lookup[assignee] = j
            ans[j[-1]] = assignee
        else:
            start = int(j[0])
            if start >= int(lookup[assignee][1]):
                lookup[assignee] = j
                ans[j[-1]] = assignee
            else:
                assignee = change_assignee(assignee)
                # check if collision with other person
                if not lookup[assignee] or start >= int(lookup[assignee][1]):
                    lookup[assignee] = j
                    ans[j[-1]] = assignee
                else:
                    return "IMPOSSIBLE"

    return "".join(ans)

for c in range(t):
    print("Case #{}: {}".format(c+1, solve()))