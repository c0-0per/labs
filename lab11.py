import argparse 
 
parser = argparse.ArgumentParser() 
 
parser.add_argument('a', type = float , help = 'first number') 
parser.add_argument('action', help = 'operations with numbers') 
parser.add_argument('b', type = float, help = 'second number') 
 
args = parser.parse_args() 
     
if args.action == "+": 
    print(args.a + args.b) 
elif args.action == "-": 
    print(args.a - args.b) 
elif args.action == "*": 
    print(args.a * args.b) 
elif args.action == "/": 
    try: 
        print(args.a / args.b) 
    except ZeroDivisionError: 
        raise ValueError('This operation is not supported for given input parameters')
else: 
    raise ValueError('This operation is not supported for given input parameters')
    
    
