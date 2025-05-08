# ID: 216175398
# Name: Joesf Heifetz

import math

# ----------------------------------------------------------------
# not tail! after the recursive call, it is added to the sum
def pentaNumRange(n1, n2):
    if not type(n1) == int or not type(n2) == int or n1 <= 0 or n2 <= 0:
        return ('ERROR')
    
    if n1 == n2:
        return []
    
    getPentaNum = lambda n: 0.5*n * (3*n - 1)

    return [int(getPentaNum(n1))] + pentaNumRange(n1+1,n2) 

# ----------------------------------------------------------------
def printByTen(array, j = 0):
     if not array:
        return
    
     print(array[0], end=' ')
    
     if j == 9:
        print()  
        j = 0   
     else:
        j += 1

     printByTen(array[1:], j)

def handlePentaNumner():
    n1 = int(input("enter the value of n1: "))
    n2 = int(input("enter the value of n2: "))
    array = pentaNumRange(n1, n2)
    printByTen(array)

# ----------------------------------------------------------------

def reverseNum(n):
   flag = False
   if n < 0:
       flag = True
       n = abs(n)
   array = [int(digit) for digit in str(n)]
   array.reverse()
   result = int(''.join(map(str, array)))
   if flag:
       result = result * -1
   return result

# ----------------------------------------------------------------

def handleReverseNum():
    n = int(input("Enter an integer number n (positive or negative): "))
    try:
        print(reverseNum(n))
    except:
        print("Error: Input number is incorrect!")

# ----------------------------------------------------------------

def pi(n):
    def generate_series_terms(n):
        return list(map(lambda i: 4 * pow(-1, i + 1)/(2 * i - 1), range(1, n + 1)))
    series_terms = generate_series_terms(n)

    return sum(series_terms)

# ----------------------------------------------------------------

def handlePi():
    n = int(input("Enter a Natural number n: "))
    try:
        print(pi(n))
    except:
        print("Error: Input number is incorrect!")

# ----------------------------------------------------------------

def all_primes(n):
    def sieve(lst, i):
        if i * i > n:
            return lst
        if lst[i - 2]:
            lst = mark_non_primes(lst, i ** 2, n, i)
        return sieve(lst, i + 1)
    
    def mark_non_primes(lst, start, end, step):
        if start >= end:
            return lst
        lst[start - 2] = False
        return mark_non_primes(lst, start + step, end, step)
    
    lst = [True] * (n - 2)
    lst = sieve(lst, 2)
    
    return [m + 2 for m in range(len(lst)) if lst[m]]

def twinp(n, array=None, index=0):
    if array is None:
        array = all_primes(n)
    if index >= len(array) - 1:
        return []
    if array[index + 1] - array[index] == 2:
        return [(array[index], array[index + 1])] + twinp(n, array, index + 1)
    else:
        return twinp(n, array, index + 1)


print(twinp(10))

