#!/usr/bin/env python

def reverse_string(string):
    """
    A Function that gets a string and reverse it.
    """
    index = len(string) # calculate length of string and save in index
    reversedString = ""
    while index > 0: 
        reversedString += string[ index - 1 ] # save the value of str[index-1] in reverseString
        index = index - 1 # decrement index
    return reversedString


if __name__ == '__main__':
    string  = input("Enter your string: ")
    res = reverse_string(string)
    print("reversed string: ", res)