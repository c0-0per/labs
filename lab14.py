import argparse 
 
parser = argparse.ArgumentParser() 
 
parser.add_argument('-W', dest='capacity', type=int) 
parser.add_argument('-w', dest='weights', type=int, nargs='*') 
parser.add_argument('-n', dest='bars_number', type=int) 
 
args = parser.parse_args() 
 
 
def func(W, w, n): 
    m = [[0 for i in range(W + 1)] for i in range(n + 1)] 
    for i in range(1, n + 1): 
        for j in range(W + 1): 
            if w[i - 1] <= j: 
                m[i][j] = max(w[i - 1] + m[i - 1][j - w[i - 1]], m[i - 1][j]) 
            else: 
                m[i][j] = m[i - 1][j] 
    return m[n][W] 
 
 
capacity = args.capacity 
weights = args.weights 
bars_number = args.bars_number 
list_check = [x for i, x in enumerate(weights) if i != weights.index(x)] 
 
 
if len(weights) != bars_number or min(weights) < 0 or capacity < 0 or list_check: 
    raise ValueError('This operation is not supported for given input parameters')
else: 
    print(func(capacity, weights, bars_number))