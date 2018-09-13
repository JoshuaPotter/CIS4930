#!/usr/bin/env python 
''' Joshua Potter, jop13
    Palindromes.py '''

def palindromic(word):
    if word[::-1].lower().replace(" ","") == word.lower().replace(" ",""):
        return True
    else:
        return False

if __name__ == "__main__":
    i = 1
    wordList = {}
    userInput = input("Enter the strings: ")
    while userInput != "Done":
        if palindromic(userInput):
            wordList[i] = userInput
            i += 1
        userInput = input()

    if len(wordList) > 0:
        print(wordList)
    else:
        print("No palindromes found.")
