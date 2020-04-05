
cache = set()

def row_valid(matrix, row, n):
    for val in matrix[row]:
        if val == n:
            return False
    return True

def col_valid(matrix, col, n):
    size = len(matrix)
    for i in range(size):
        if matrix[i][col] == n:
            return False
    return True

def find_empty_cell(matrix, size, l):
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False


def compute_trace(matrix, size):
    trace = 0
    nums = []
    for i in range(size):
        nums.append(matrix[i][i])
        trace += matrix[i][i]
    nums.sort()
    nums = tuple(nums)
    if nums in cache:
        return -1, nums, False
    return trace, nums, True

def backtrack(matrix, size, target):
    l = [0, 0]
    if not find_empty_cell(matrix, size, l):
        trace, nums, is_latin = compute_trace(matrix, size)
        if not is_latin:
            return False
        if trace != target:
            cache.add(nums)
            return False
        return True

    row, col = l[0], l[1]
    for n in range(1, size+1):
        if row_valid(matrix, row, n) and col_valid(matrix, col, n):
            matrix[row][col] = n
            if backtrack(matrix, size, target):
                return True
            matrix[row][col] = 0
    return False

def convert_matrix_to_str(matrix, size):
    ans = ""
    for i in range(size):
        row = " ".join(map(str, matrix[i]))
        ans += row
        if i < size-1:
            ans += "\n"
    return ans

def solve():
    size, target = map(int, input().split(" "))
    matrix = [[0 for i in range(size) ] for j in range(size)]
    if not backtrack(matrix, size, target):
        return "IMPOSSIBLE"
    matrix_str = convert_matrix_to_str(matrix, size)
    ans = "POSSIBLE\n{}".format(matrix_str)
    return ans

T = int(input())
for c in range(T):
    print("Case #{}: {}".format(c+1, solve()))