import re
import ast

def info_proj_get(file_name):
    try:
        with open(file_name, 'r') as file:
            nested_list = file.read()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"
    nested_list = convert_to_nested_list(nested_list)
    fixed_array = transform(nested_list)
    print(fixed_array)

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


def transform(array):
    # Base case: if the array is empty, return an empty array
    if not array:
        return array

    # Recursive case: process each element of the array
    result = []
    for element in array:
        if isinstance(element, list):
            # Check if the list matches the pattern ['aX', num1, num2]
            if len(element) == 3 and isinstance(element[0], str) and isinstance(element[1], int) and isinstance(element[2], int):
                # Transform the list to ['aX', num1 - num2]
                result.append([element[0], abs(element[1] - element[2])])
            else:
                # Recursively process nested lists
                result.append(transform(element))
        else:
            result.append(element)

    return result


info_proj_get('project_info.txt')
