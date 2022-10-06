
def writeTextToFile(a):
    STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "
    x = STATICKY_TEXT + str(a)
    with open('aragage.txt', 'w') as file:
        file.write(x)
    print(x)
    return 'uk2.txt'



writeTextToFile('asd')