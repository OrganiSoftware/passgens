"""
@AUTHOR organi
"""

import json
import random
import os
import numpy as cp
class randomPass:
    def randomPass(self):
        array = cp.array([])
        for index in range(95):
            temparray = cp.append(array, 32+index)
            array = temparray
        print(str(array))
        initalchars = len(array)
        passwords = cp.array([])
        for index in range(initalchars):
            tempasswords  = cp.append(passwords,str(chr(int(array[index]))))
            passwords = tempasswords
        for passlen in range(15):
            newpasswords = cp.array([])
            f2 = open("/home/organi/passlist.txt", "a")
            count = 0
            for index in range(initalchars):
                for charindex in range(len(array)):
                    stringy = str(passwords[index]+chr(int(array[charindex])))
                    print(str(stringy))
                    tempnewasswords = cp.append(newpasswords, str(stringy))
                    newpasswords = tempnewasswords
                    count += 1
            for newindex in range(len(newpasswords)):
                f2.write(str(passlen) + " " + str(newpasswords[newindex] + "\n"))
            passwords = newpasswords
            initalchars = count

if __name__ == '__main__':
    randomobj = randomPass()
    randomobj.randomPass()
