MAX_MATCH_LEN = 10**4

def find_match(patterns):
    common = patterns[0]
    for i in range(1, len(patterns)):
        p2 = patterns[i]
        res = unify_pattern(common,p2)
        if res is None:
            res = unify_pattern(p2,common)
            if res is None:
                return '*'
        common = res
    return common[1:]

def unify_pattern(p1, p2):
    result = ''
    if p1[0] == '*':
        if p2[0] == '*':
            if p1.endswith(p2[1:]):
                return p1
            else:
                return None
        else:
            # todo test set 2
            return None

def find_match_2(patterns):
    beginning = ''
    end = ''
    for p in patterns:
        # print(beginning, end)
        beginning, end = unify_pattern_2(beginning, end, p)
        # print(beginning, end)
        if beginning is None or end is None:
            return '*'
    return beginning + end

def unify_pattern_2(beginning, end, pattern):
    # print(beginning, end, pattern)
    b,e = pattern.split('*')
    # print('>> |{}|  |{}|  {}'.format(e, end, e.endswith(end)))
    if beginning.startswith(b):
        newb = beginning
    elif b.startswith(beginning):
        newb = b
    else:
        return None, None

    if end.endswith(e):
        newe = end
    elif e.endswith(end):
        newe = e
    else:
        return None, None
    
    return newb,newe

def get_patterns():
    num_patterns = int(input())
    patterns = []
    for i in range(num_patterns):
        patterns.append(input())
    return patterns

if __name__ == '__main__':
    num_tests = int(input())
    for i in range(num_tests):
        patterns = get_patterns()
        match = find_match_2(patterns)
        print("Case #{}: {}".format(i+1, match))