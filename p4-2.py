def smallLarge(arg):
    """
    smallest and largest of the inputs

    Args:
        int arg
    Variables:
        int smallest, largest, i
    Return:
        small and large of input
    """
    arg = str(arg)
    smallest = int(arg[0])
    largest = int(arg[0])
    for i in range(len(arg)):
        if int(arg[i]) > largest:
            largest = int(arg[i])
        elif int(arg[i]) < smallest: 
            smallest = int(arg[i])
    return smallest, largest

#print(smallLarge(1729))

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
    
adjacentDupl(133455662)
     

            
