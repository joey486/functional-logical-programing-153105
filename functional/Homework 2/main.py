# Name: Joesf Heifetz

# ----------------------------------------------------------------
def pentaNumRange_1(n1, n2):
    if not type(n1) is int or not type(n2) is int or n1 <= 0 or n2 <= 0:
        return ('ERROR')
    
    if n1 == n2:
        return []
    
    getPentaNum = lambda n: 0.5*n * (3*n - 1)

    return [int(getPentaNum(n1))] + pentaNumRange_1(n1+1,n2) 

def pentaNumRange_2(n1, n2):
    if n1 > n2 or n2 <= 0:
        print("ERROR")
        return
    penta_numbers = []

    for i in range (n1,n2-1):
        penta_numbers.append(int(0.5*i * (3*i - 1)))

    for i in range(len(penta_numbers)):
        print(penta_numbers[i], end=' ')
        if (i + 1) % 10 == 0:
            print()

def pentaNumRange_3(n1, n2):
    if not type(n1) is int or not type(n2) is int or n1 <= 0 or n2 <= 0:
        return ('ERROR')
    
    if n1 == n2:
        return []
    
    getPentaNum = lambda n: 0.5*n * (3*n - 1)

    return [int(getPentaNum(n1))] + pentaNumRange_3(n1+1,n2) 

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

def sectionThreeQuestionOne(n1, n2):
    printByTen(pentaNumRange_3(n1,n2))

# ----------------------------------------------------------------

def sumDigits(n):
    if n < 10:
        return n
    
    return n % 10 + sumDigits(n // 10)

def sumHandle():
    try:
        n = int(input("Enter an integer number n (positive or negative): "))
        print(sumDigits(abs(n)))
    except ValueError:
        print("ERROR: Input number is incorrect!")

# ----------------------------------------------------------------

def isPalindrome (n):
    return str(n) == str(n)[::-1]

def palindrome():
    try:
        n = int(input("Enter an integer number n (positive or negative): "))
        if(isPalindrome(n)): print("It is a palindrome ")
        else: print("It is not a palindrome")
    except ValueError:
        print("ERROR: Input number is incorrect!")

# ----------------------------------------------------------------

def m(n):
    def generate_series_terms(n):
        return list(map(lambda i: i / (i + 1), range(1, n + 1)))
    series_terms = generate_series_terms(n)

    total_sum = sum(series_terms)

    return total_sum

def printM():
    n = int(input("Enter a Natural number n: "))

    if n <= 0 or not isinstance(n, int):
        print("Error: Input number is incorrect!")
        return
    else:
        results = list(map(lambda i: (i, m(i)), range(n)))
        for i, result in results:
            print(i, ' ', result)

# ----------------------------------------------------------------

def add3dicts(d1, d2, d3):
    common_keys = lambda d1, d2, d3: set(d1.keys()) & set(d2.keys()) & set(d3.keys())
    unique_keys = lambda d1, d2, d3: (set(d1.keys()) | set(d2.keys()) | set(d3.keys())) - common_keys(d1, d2, d3)
    
    common = common_keys(d1, d2, d3)
    unique = unique_keys(d1, d2, d3)
    
    merged_common = {key: tuple(set(filter(None, [d1.get(key), d2.get(key), d3.get(key)]))) for key in common}
    merged_unique = {key: (d1.get(key) or d2.get(key) or d3.get(key)) for key in unique}
    
    merged_dict = {**merged_common, **merged_unique}

    return merged_dict

def print5():
    d1 = eval(input("Enter first dictionary: "))
    d2 = eval(input("Enter second dictionary: "))
    d3 = eval(input("Enter third dictionary: "))
    
    result = add3dicts(d1, d2, d3)
    
    print("Merged dictionary:", result)

# ----------------------------------------------------------------




def main():
    lfuncs = [pentaNumRange_1, pentaNumRange_2, sectionThreeQuestionOne, sumDigits, sumHandle,
              palindrome, printM, print5] # function names 
    lstrs = [
        "Generates a list of pentagonal numbers within a specified range using recursion.",
        "Prints pentagonal numbers within a specified range using loops.",
        "Prints pentagonal numbers within a specified range in sections of ten.",
        "Calculates the sum of digits of a given integer.",
        "Handles user input to compute the sum of digits of an integer.",
        "Checks if a given integer is a palindrome.",
        "Computes and prints a series sum based on user input.",
        "Merges three dictionaries, handling common and unique keys."
    ] #description of functions 
    
    while True:
        print("Your choices:")
        for i, s in enumerate(lstrs):
            print(f"{i} : {s}")
        c = int(input("Please enter your choice: "))
        if c == 0:
            break
        elif 1 <= c <= 7:
            lfuncs[c-1]()
        elif 8 <= c <= 10:
            lfuncs[c-1]
        else:
            print("Error: Invalid choice")

if __name__ == "__main__":
    main()
