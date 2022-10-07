"""import argparse 
 
parser = argparse.ArgumentParser() 

parser.add_argument('action', type = str, help = 'operation') 
parser.add_argument('a', type = float , help = 'first number') 
parser.add_argument('b', type = float, help = 'second number') 
 
args = parser.parse_args() 
     
if args.action == "add": 
    print(args.a + args.b) 
elif args.action == "substract": 
    print(args.a - args.b) 
elif args.action == "multiply": 
    print(args.a * args.b) 
elif args.action == "divide": 
    try: 
        print(args.a / args.b) 
    except ZeroDivisionError: 
        raise ValueError('This operation is not supported for given input parameters')
else: 
    raise ValueError('This operation is not supported for given input parameters')"""



import math 
import operator 
import argparse 
 
parser = argparse.ArgumentParser() 
 
parser.add_argument("action", help='operator or math functions') 
parser.add_argument('num', type=float, nargs='+', help='list of number') 
 
args = parser.parse_args() 
 
def operations(): 
    try: 
        if args.action == 'fsum' or args.action == 'prod': 
            return eval('math.' + args.action)(args.num) 
        else: 
            return eval('math.' + args.action)(*(args.num)) 
    except: 
        pass 
 
    try: 
        return eval('operator.' + args.action)(*(args.num)) 
    except: 
        pass 
 
    raise ValueError('This operation is not supported for given input parameters')
 
print(operations())