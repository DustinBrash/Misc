inputStr = raw_input("Input encrypted string: ")
outputStr = ''
for i, char in enumerate(inputStr):
    ascii = ord(char)
    ascii = ascii - i
    ascii = chr(ascii)
    outputStr += ascii
print outputStr
    
