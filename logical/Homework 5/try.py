grades = [
    {"name": "sara", "grade": 97},
    {"name": "rivka", "grade": 88},
    {"name": "naama", "grade": 67},
    {"name": "rachel", "grade": 81}
]

def milga(num):
    L = []
    Grade = 0
    sorted_grades = sorted(grades, key=lambda x: x["grade"], reverse=True)
    
    for i in range(num):
        L.append(sorted_grades[i])
        Grade = sorted_grades[i]["grade"]

    return Grade, L

def allDivs(NUM):
    L = []
    i = 1
    while i <= NUM:
        if NUM % i == 0:
            L.append(i)
        i = i + 1
    return L

def max_min(L):
    if not L:
        return None, None  # Handle empty list

    max_val = L[0]
    min_val = L[0]

    for i in range(1, len(L)):
        if L[i] > max_val:
            max_val = L[i]
        if L[i] < min_val:
            min_val = L[i]

    return max_val, min_val


def main():
    # # Example call to milga
    # Grade, L = milga(2)  # This will print the highest grade

    # print(Grade)
    # print(L)


    # L = allDivs(12)
    # print(L)

    X, Y = max_min(["a","b","c","c","a","c","c"])

    print(X)
    print(Y)

if __name__ == '__main__':
    main()
