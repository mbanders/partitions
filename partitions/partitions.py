from math import exp, pi, sqrt

def partitions(n, k=1):
    '''
    Generate all partitions of a positive integer 'n'.
    '''
    yield (n,)
    for i in range(k, n//2 + 1):
        for p in partitions(n-i, i):
            yield p + (i,)

def pretty_partitions(n):
    '''
    Print all partitions of 'n' in a nice human-readable way.
    '''
    count = 0
    for x in partitions(n):
        count += 1
        print(" + ".join(str(i) for i in x))
    print("Listed all %s partitions of %s." % (count, n))

def total_partitions(n):
    '''
    Return the number of ways of writing 'n' as a sum
    of positive integers. The answer grows roughly (1/n)*exp(sqrt(n)).
    '''
    data = [1] + [0]*n
    for i in range(1, n+1):
        for j, x in enumerate(range(i, n+1)):
            data[x] += data[j]
    return data[-1]

def estimate_total_partitions(n):
    '''
    Return an estimate for the total number of ways of
    writing 'n' as a sum of positive integers.
    '''
    return int((1/(4*n*sqrt(3))) * exp(pi * sqrt(2*n/3)))
