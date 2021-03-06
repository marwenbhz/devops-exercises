#!/usr/bin/env python

def compress_string(string):
    """
    A Function that gets a string and compresses it.
    """
    res = ""
    count = 1
    #Add in first character
    res += string[0]
    #Iterate through loop, skipping last one
    for i in range(len(string)-1):
        if(string[i] == string[i+1]):
            count+=1
        else:
            if(count > 1):
                #Ignore if no repeats
                res += str(count)
            res += string[i+1]
            count = 1
    #print last one
    if(count > 1):
        res += str(count)
    return res


if __name__ == '__main__':
    string  = input("Enter your string: ")
    res = compress_string(string)
    print("compressed string: ", res)
