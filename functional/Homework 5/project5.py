
def evenprt(n1, n2, n3):
    def get_evens(n1, n2):
        if n1 > n2:
            return []
        elif n1 % 2 == 0:
            return [n1] + get_evens(n1 + 2, n2)
        else:
            return get_evens(n1 + 1, n2)
    
    def print_evens(evens, n3):
        if not evens:
            return
        print(evens[:n3])
        print_evens(evens[n3:], n3)

    evens = get_evens(n1, n2)
    print_evens(evens, n3)


def napa(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    def mark_non_primes(i):
        if i * i > n:
            return
        if sieve[i]:
            sieve[i * i:n + 1:i] = [False] * len(range(i * i, n + 1, i))
        mark_non_primes(i + 1)
    mark_non_primes(2)
    return [i for i in range(2, n + 1) if sieve[i]]

def primefactors(n):
    def find_factors(n, primes):
        if n == 1:
            return []
        for p in primes:
            if n % p == 0:
                return [p] + find_factors(n // p, primes)
        return [n]

    primes = napa(n)
    return list(set(find_factors(n, primes)))


def sortedzip(lists):
    sorted_lists = [sorted(sublist) for sublist in lists]
    return zip(*sorted_lists)
def reversedzip(lists):
    reversed_lists = [list(reversed(sublist)) for sublist in lists]
    return zip(*reversed_lists)
def funczip(func, lists):
    return func(lists)
def unzippy(zipped):
    return list(map(list, zip(*zipped)))
