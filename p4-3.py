def readUpper(arg):
    """
    Read only uppercase letters in a string

    Arguments:
        string arg
    Return:
        uppercase letters
    """
    returnChars = ""
    if (arg, str):
        for char in arg:
            if char.isupper():
                returnChars += char
    else:
        return "not a string"
    return returnChars

#print(readUpper("aDsDCFEase"))

def secondLetter(arg):
    charsToReturn = ""
    for i in range(0, len(arg), 2):
        charsToReturn += arg[i]
    return charsToReturn

#print(secondLetter("asdasdasdasd"))

def replaceVowels(arg):
    """
    Replace all vowels with _

    Arguments:
        string arg
    Return:
        vowels => _
    """
    newString = ""
    VOWELS = ["a", "e", "i", "o", "u"]
    for i in range(len(arg)):
        if arg[i] in VOWELS:
            newString += "_"
        else:
            newString += arg[i]
    return newString

#print(replaceVowels("aeifgcobu"))

def noDigitsString(arg):
    count_int = 0
    for char in arg:
        try:
            int(char)
            count_int += 1
        except: pass
    return count_int

#print(noDigitsString("123asd"))

def positionVowel(arg):
    VOWELS = ["a", "e", "i", "o", "u"]
    for i in range(len(arg)):
        if arg[i] in VOWELS:
            print(i)

#positionVowel("aeidfgo")
