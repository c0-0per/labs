import argparse 
 
parser = argparse.ArgumentParser() 
 
parser.add_argument('formula') 
 
args = parser.parse_args() 
 
def is_formula(str_input): 
    if str_input and str_input[0].isdigit(): 
        str_input = str_input.lstrip("1234567890") 
        if not str_input: 
            return True 
        if str_input[0] in "+-": 
            return is_formula(str_input[1:]) 
    return False 
 
def res_formula(str_input): 
    current = '' 
    arr = [] 
    for i in str_input: 
        if i.isdigit(): 
            current += i 
        else: 
            arr.append(int(current))
            current = '' 
 
    arr.append(int(current)) 
 
    result = arr[0] 
    j = 1 
    for i in str_input: 
        if i == '+': 
            result += arr[j] 
            j +=1 
        elif i == '-': 
            result -= arr[j] 
            j +=1 
 
    return result 
 
str_input = args.formula 
ind = bool(is_formula(str_input)) 
 
if ind: 
    print(ind, res_formula(str_input)) 
else: 
    print(ind, None)