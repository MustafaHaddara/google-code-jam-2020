def find_trace(size, trace):
    diags = find_sum(size, trace)
    seen = set()
    for d in diags:
        d.sort()
        key = ''.join((str(i) for i in d))
        if key in seen:
            continue
        seen.add(key)
        r = make_latin_square(size, d)
        if r:
            return r
    return None


def find_sum(size, total):
    sums = find_sum_inner(size, total)
    return [s for s in sums if len(s) == size]


def find_sum_inner(size, total):
    sums = []
    if total == 0:
        return []

    for i in range(1, size+1):
        if total == i:
            sums.append([i])
            break
        else:
            rest = find_sum_inner(size, total-i)
            for r in rest:
                r.append(i)
                # if len(r) < size:
                sums.append(r)

    return sums


def make_latin_square(size, diagonal):
    mat = []
    for x in range(size):
        row = []
        for y in range(size):
            row.append(None)
        mat.append(row)
    for idx,item in enumerate(diagonal):
        mat[idx][idx] = item
    # brute force the rest
    return fill_in_latin_square(mat, size, 0, 1)


def fill_in_latin_square(mat, size, row, col):
    mine = []
    for r in mat:
        mine.append(r[:])
    for i in range(1, size+1):
        mine[row][col] = i
        if is_valid(mine):
            next_row, next_col = find_next_coord(size, row, col)
            if next_row == size:
                # we're at the end! it worked!
                return mine
            sq = fill_in_latin_square(mine, size, next_row, next_col)
            if sq:
                # we're in the right branch! it worked!
                return sq
        else:
            mine[row][col] = None


def find_next_coord(size, row, col):
    next_col = col+1
    next_row = row

    if next_col == next_row:
        next_col += 1

    if next_col == size:
        next_col = 0
        next_row = row + 1

    return next_row, next_col


def is_valid(mat):
    for row in mat:
        if contains_dupes(row):
            return False
    for i in range(len(mat)):
        col = [row[i] for row in mat]
        if contains_dupes(col):
            return False
    return True


def contains_dupes(row):
    seen = set()
    for i in row:
        if i is None:
            continue
        if i in seen:
            return True
        seen.add(i)
    return False


# mat = 2d array => 1d arrow of rows
def print_matrix(mat):
    for row in mat:
        for c in row:
            print('{} '.format(c if c is not None else 'N'), end='')
        print('')


if __name__ == '__main__':
    num_tests = int(input())
    for i in range(num_tests):
        size,trace = [int(i) for i in input().split()]
        res = find_trace(size, trace)
        if res:
            print("Case #{}: POSSIBLE".format(i+1))
            print_matrix(res)
        else:
            print("Case #{}: IMPOSSIBLE".format(i+1))