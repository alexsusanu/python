def reverseWord(arg):
    """
    Print a word in reverse
    """
    for i in range(len(arg) - 1, -1, -1):
        print(arg[i], end="")

#reverseWord("Harry")
