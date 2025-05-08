import re
import ast

def format_string(input_string):
    # Regular expression to match variables (sequences of alphabetic characters)
    pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
    
    # Function to replace matched variables with quoted versions
    def replace_variable(match):
        return f'"{match.group(0)}"'
    
    # Use re.sub to replace all occurrences of the pattern
    formatted_string = re.sub(pattern, replace_variable, input_string)
    
    return formatted_string

def convert_to_nested_list(input_string):


    
    # Format the string to enclose variables in quotes
    formatted_string = format_string(input_string)
    
    # Use ast.literal_eval to safely evaluate the formatted string
    nested_list = ast.literal_eval(formatted_string)
    
    return nested_list




def info_proj_get(file_name, cost_per_time_unit):
    try:
        with open(file_name, 'r') as file:
            nested_list = file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"
    nested_list = convert_to_nested_list(nested_list)
    tmp = process_first_layer(nested_list)
    cost_per_time_unit = float(cost_per_time_unit)
    result = ((tmp[0], tmp[0] * cost_per_time_unit), (tmp[1], tmp[1] * cost_per_time_unit), (tmp[2], tmp[2] * cost_per_time_unit))
    print(result)


def process_first_layer(array):
    result = [0,0,0]
    for element in array:
        if isinstance(element, list) and len(element) == 2 and isinstance(element[0], list) and len(element[0]) == 3:
            sublist = element[0]
            if isinstance(sublist[0], str) and isinstance(sublist[1], int) and isinstance(sublist[2], int):
                # Apply transformation
                new_sublist = [sublist[0], sublist[1] - sublist[2]]
                result[0] += sublist[1]
                result[1] += sublist[2]
                result[2] += sublist[2] - sublist[1]
    return result


def reverseList(lst):
    if not lst:
        return []
    elif isinstance(lst[-1], list):
        return [reverseList(lst[-1])] + reverseList(lst[:-1])
    else:
        return [lst[-1]] + reverseList(lst[:-1])


def input_list():
    import ast
    user_input = input("enter a list")
    try:
        lst = ast.literal_eval(user_input)
        if not isinstance(lst, list):
            raise ValueError
        return lst
    except (ValueError, SyntaxError):
        print("ERROR")
        return input_list()
    

def isPalindrome(lst):
    if len(lst) <= 1:
        return True
    if lst[0] == lst[-1]:
        return isPalindrome(lst[1:-1])
    else:
        return False


def input_list_1():
    import ast
    user_input = input("enter a list")
    try:
        lst = ast.literal_eval(user_input)
        if not isinstance(lst, list):
            raise ValueError
        return lst
    except (ValueError, SyntaxError):
        print("ERROR")
        return input_list()
    

def sieve_of_eratosthenes(n):
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

def twinp(n):
    primes = sieve_of_eratosthenes(n)
    return {primes[i]: primes[i + 1] for i in range(len(primes) - 1) if primes[i + 1] - primes[i] == 2}


def input_positive_integer():
    try:
        n = int(input("input a number"))
        if n > 0:
            return n
        else:
            return input_positive_integer()
    except ValueError:
        return input_positive_integer()
    
def dicts3add(d1, d2, d3):
    keys1, keys2, keys3 = set(d1.keys()), set(d2.keys()), set(d3.keys())
    common_keys = keys1 & keys2 & keys3
    all_keys = keys1 | keys2 | keys3

    def merge_values(k):
        return tuple(set(filter(None, [d1.get(k), d2.get(k), d3.get(k)])))

    return {k: merge_values(k) if k in common_keys else d1.get(k) or d2.get(k) or d3.get(k) for k in all_keys}

def input_dict():
    import ast
    user_input = input("input dictionary")
    try:
        d = ast.literal_eval(user_input)
        if not isinstance(d, dict):
            raise ValueError
        return d
    except (ValueError, SyntaxError):
        print("error")
        return input_dict()
