def deduce_db(size):
    pos = 1
    print(pos)

    db = [None] * size
    ## figure out what's in the array
    ## determine what happened to the array
    ## print
    for i in range(1,11):
        print(i)
        db[i] = int(input())
    
    # at this point, the array has gone through some transformation, we don't know what
    # either:
    # - complement => 0 into 1 and vice versa
    # - reverse
    # - complement and reverse
    # - nothing

    comp = complement(db)
    rev = reverse(db)
    b = both(db)

    # now we need to differentiate between db, comp, rev, b
    for idx in range(len(db)):
        in_db = db[idx]
        in_comp = comp[idx]
        in_rev = rev[idx]
        in_b = b[idx]

        if  in_b == in_comp and in_db == in_rev and in_db == in_comp:
            # transitive, they're all equal
            # this idx doesn't help us
            continue

        


def complement(db):
    return [int(not i) for i in db]

def reverse(db):
    return db[::-1]

def both(db):
    return [int(not db[i]) for i in range(len(db)-1, -1, -1)]

if __name__ == '__main__':
    num_tests,size = (int(i) for i in input().split())
    for i in range(num_tests):
        deduce_db(size)