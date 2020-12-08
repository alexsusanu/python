#integer, numbers related exercises
#p4-(1,2)

def smallLarge(arg):
    """
    smallest and largest of the inputs

    Args:
        arg of type int, float
    Variables:
        int smallest, largest, i
    Return:
        smallest in position 0 and largest in position 1
    """
    smallest = arg[0]
    largest = arg[0]
    for i in range(len(arg)):
        if arg[i] > largest:
            largest = arg[i]
        elif arg[i] < smallest: 
            smallest = arg[i]
    return smallest, largest

#test = [1.2, 3, 4, 5.6]
#print(smallLarge(test))

def averageValue(arg):
    """
    Print the average of values

    Arguments:
        int, float arg
    Return:
        average
    """
    sigma = 0
    for i in range(len(arg)):
        sigma += arg[i]
    return sigma / len(arg)


def numberEvenOdd(arg):
    """
    Number of even and odd inputs

    Args:
        int arg
    Variables:
        int count_odd, count_even
    Return:
        number of even and odd numbers
    """
    count_odd = 0
    count_even = 0
    arg = str(arg)
    for i in range(len(arg)):
        if int(arg[i]) % 2 != 0:
            count_odd += 1
        else: count_even += 1
    return count_odd, count_even

#print(numberEvenOdd(1729))

def cumulativeTotal(arg):
    """
    Cumulative total

    Args:
        int arg
    Return:
        total
    """
    sum = 0
    arg = str(arg)
    for i in range(len(arg)):
        sum += int(arg[i])
        print(sum)

#cumulativeTotal(1729)

def adjacentDupl(arg):
    """
    Print  all adjacents duplicates
    ex: 1 2 3 3 4 5 5 5 6 6 7 => 3 5 6 

    Args:
        int arg
    Return:
        adjacent duplicates
    """
    arg = str(arg)
    for j in range(len(arg) - 1):
        if arg[j] == arg[j + 1]:
            print(arg[j])
    
#adjacentDupl(133455662)
     

            
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

#print(sumOddDigits(32677))

