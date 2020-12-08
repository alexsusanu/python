def allEven():
    """ 
    Sum of all even numbers between 2..100(inclusive)
    
    Args:
        no args
    Variables:
        int sum
        int i
    Return:
        sum
    """
    sum = 0
    for i in range(2, 101):
        if (i % 2 == 0):
            sum += i
    return sum

#print(allEven())

def allSquares():
    """
    Sum of all squares between 1..100(incl)

    Args:
        no args
    Variables:
        int i, sum
    Return:
        sum
    """
    sum = 0
    for i in range(1, 101):
        sum += pow(i, 2)
    return sum

#print(allSquares())

def allPowersTwo():
    """
    Sum of all powers of 2..20(incl)

    Args:
        no args
    Variables:
        int i, sum
    Const:
        base
    Return:
        sum
    """
    sum = 0
    BASE = 2;
    for i in range(2, 21):
        if i % 2 == 0:
            sum += pow(BASE, i)
    return sum

#print(allPowersTwo())

def allOddNo(a, b):
    """
    Sum of all odd numbers between a..b(incl)

    Args:
        int a, b
    Variables:
        int sum, i
    Return:
        sum
    """
    sum = 0
    for i in range(a, b + 1):
        if i % 2 != 0:
            sum += i
    return sum

#print(allOddNo(1,100))

def sumOddDigits(arg):
    """
    Sum of all odd digits in a number
    example 32677 => 3 + 7 + 7

    Args:
        int arg
    Variables:
        int i, sum
    Return:
        sum
    """
    sum = 0
    arg = str(arg)
    for i in range(len(arg)):
        if int(arg[i]) % 2 != 0:
            sum += int(arg[i])
    return sum

print(sumOddDigits(32677))

