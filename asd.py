parametr = input("rekni mi parametr:")

def writeTextToFile(parametr):
    STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "
    my_file = open("hj.txt", "w")
    my_file.write(STATICKY_TEXT)
    my_file.write(parametr)
    my_file.close()
    return "hj.txt"

writeTextToFile(parametr)