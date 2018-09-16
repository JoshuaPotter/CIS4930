'''
    Joshua Potter, jop13
    Palindromes.py 
'''

def palindromic(word):
    ''' 
        Remove white space, convert to lower case, and compare
        word frontward and backward 
    '''
    if word[::-1].lower().replace(" ","") == word.lower().replace(" ",""):
        return True
    else:
        return False

if __name__ == "__main__":
    i = 1
    wordList = {}
    userInput = input("Enter the strings: ")

    ''' 
        Calls plaindromic() to determine if word
        should be added with key to wordList dictionary, then
        asks for another input value to check 
    '''
    while userInput != "Done":
        if palindromic(userInput):
            wordList[i] = userInput
            i += 1
        userInput = input()

    # Prints the list if there are palindromes found 
    if len(wordList) > 0:
        print("The palindromes are:")
        print(wordList)
    else:
        print("No palindromes found.")
