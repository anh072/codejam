t = int(input())

def compute_trace(size, matrix):
    trace = 0
    for j in range(size):
        trace += int(matrix[j][j])
    return trace

def num_repeated_rows(size, matrix):
    n = 0
    for i in range(len(matrix)):
        bool_arr = [False] * size
        for j in range(len(matrix[0])):
            val = int(matrix[i][j])
            if not bool_arr[val-1]:
                bool_arr[val-1] = True
            else:
                n += 1
                break
    return n

def num_repeated_cols(size, matrix):
    n = 0
    for j in range(len(matrix[0])):
        bool_arr = [False] * size
        for i in range(len(matrix)):
            val = int(matrix[i][j])
            if not bool_arr[val-1]:
                bool_arr[val-1] = True
            else:
                n += 1
                break
    return n

def solve():
    size = int(input())
    matrix = []
    for i in range(size):
        row_str = input()
        row = row_str.split(" ")
        matrix.append(row)
    
    trace = compute_trace(size, matrix)
    cols = num_repeated_cols(size, matrix)
    rows = num_repeated_rows(size, matrix)
    return f"{trace} {rows} {cols}"

for c in range(t):
    print(f"Case #{c+1}: {solve()}")