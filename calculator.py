

def addition(x, y):
    return(int(x)+int(y))


def subtraction(x, y):
    return(int(x)-int(y))


def multiplication(x, y):
    return(int(x)*int(y))


def division(x, y):
    if y == 0:
        return(ValueError('This operation is not supported for given input parameters'))
    else:
        return(int(x)/int(y))


def modulo(x, y):
    if x>=y and y>0:
        return(int(x)%int(y))
    else:
        return(ValueError('This operation is not supported for given input parameters'))

def secondPower(x):
    return(int(x)*int(x))


def power(x, y):
    if int(y) >= 0:
        return(float(int(x)**y))
    else :
        return(ValueError('This operation is not supported for given input parameters'))


def secondRadix(x):
    if int(x) > 0:
        return(x**0.5)
    else:
        return(ValueError('This operation is not supported for given input parameters'))


def magic(x, y, z, k):
    l = int(x) + int(k)
    m = int(y) +int (z)
    n = ((l/m) + 1)
    return(n)


def control(a, x, y, z, k):
    if a == "ADDITION":
        return(addition(x,y))
    elif str(a) == "SUBTRACTION":
        return(subtraction(x,y))
    elif str(a) == "MULTIPLICATION":
        return(multiplication(x,y))
    elif a == "DIVISION":
        return(division(x,y))
    elif str(a) == "MOD":
        return(modulo(x,y))
    elif str(a) == "SECONDPOWER": 
        return(secondPower(x))
    elif str(a) == "POWER": 
        return(power(x,y))
    elif str(a) == "SECONDRADIX":
        return(secondRadix())
    elif str(a) == "MAGIC":
        return(magic(x, y, z, k))
    else:
        raise ValueError('This operation is not supported for given input parameters')
        

print(control("ADDITTION", 1, 2, 3, 4))

