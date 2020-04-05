def match_nesting(s):
    current_depth = 0
    result = ''
    for c in s:
        val = int(c)
        while current_depth < val:
            result += '('
            current_depth += 1
        while current_depth > val:
            result += ')'
            current_depth -= 1
        result += c
    while current_depth > 0:
        result += ')'
        current_depth -= 1
    return result


if __name__ == '__main__':
    num_tests = int(input())
    for i in range(num_tests):
        s = input()
        balanced = match_nesting(s)
        print("Case #{}: {}".format(i+1, balanced))