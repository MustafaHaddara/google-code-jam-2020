from math import sqrt

def find_pascal_walk(sum):
    if sum == 1:
        return [ [1,1] ]
    return find_walk(sum)

def lin(n):
    return 1

def arth(x):
    n = x-1
    return n

def tri(x):
    n = x-2
    return (n) * (n+1) / 2

def tetra(x):
    n = x-3
    return (n) * (n+1) * (n+2) / 6

def find_walk(sum):
    result = [ [1,1] ]
    total = 1
    x = 2
    y = 1
    while total < sum:
        if y == 4:
            if total + tetra(x) < sum:
                y = 4
                total += tetra(x)
            elif total + tri(x) < sum:
                y = 3
                total += tri(x)
            elif total + tri(x-1) < sum:
                y = 3
                x = x-1
                total += tri(x-1)
            else:
                print('oops')
        elif y == 3:
            if total + tetra(x) < sum:
                y = 4
                total += tetra(x)
            elif total + tri(x) < sum:
                y = 3
                total += tri(x)
            elif total + arth(x) < sum:
                y = 2
                total += arth(x)
            else:
                print('oops')
        elif y == 2:
            if total + tri(x) < sum:
                y = 3
                total += tri(x)
            elif total + arth(x) < sum:
                y = 2
                total += arth(x)
            elif total + lin(x) < sum:
                y = 1
                total += lin(x)
            else:
                print('oops')
        elif y == 1:
            if total + arth(x) < sum:
                y = 2
                total += arth(x)
            elif total + lin(x) < sum:
                y = 1
                total += lin(x)
            else:
                print('oops')
        else:
            print('not possible!')

        result.append( [x, y] )
        x += 1


    return result


if __name__ == '__main__':
    num_tests = int(input())
    for i in range(num_tests):
        sum = int(input())
        walk = find_pascal_walk(sum)
        print("Case #{}:".format(i+1))
        for step in walk:
            print("{} {}".format(step[0], step[1]))