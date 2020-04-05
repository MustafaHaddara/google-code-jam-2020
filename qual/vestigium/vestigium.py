# mat = 2d array => 1d arrow of rows
def latin_square_trace(mat):
    n = len(mat)
    rows_with_dupes = 0
    cols_with_dupes = 0
    trace = 0
    # check rows
    for row in mat:
        if contains_dupes(row):
            rows_with_dupes += 1

    # check cols
    for i in range(n):
        col = (row[i] for row in mat)
        if contains_dupes(col):
            cols_with_dupes += 1
    
    # compute trace
    for i in range(n):
        trace += mat[i][i]
    return [trace, rows_with_dupes, cols_with_dupes]

def contains_dupes(row):
    seen = set()
    num_counted = 0
    for i in row:
        num_counted += 1
        seen.add(i)
    return len(seen) != num_counted

def parse_matrix():
    mat = []
    n = int(input())
    for i in range(n):
        row_str = input().split()
        mat.append([int(i) for i in row_str])
    return mat

if __name__ == '__main__':
    num_tests = int(input())
    for i in range(num_tests):
        mat = parse_matrix()
        trace,rows,cols = latin_square_trace(mat)
        print("Case #{}: {} {} {}".format(i+1, trace, rows, cols))