"""
@Author Organi
"""

import random
import argparse

class randomPass:
    def randomPass(self):
        parser = argparse.ArgumentParser(description='Create login login credetials for user rsa_auth')
        parser.add_argument('path', help='path to passwd file')
        parser.add_argument('num_pass', help='number of passwords')
        parser.add_argument('max', help='max pass length')
        parser.add_argument('min', help='min pass length')
        args = parser.parse_args()
        with open(str(args.path), "w") as file:
            array = []
            for index in range(95):
                array.append(32+index)
                print(str(array))
            for index in range(int(args.num_pass)):
                passarray = []
                for passwordlenght in range(int(args.max)):
                    password = ""
                    randomnum = random.random()
                    indexchar = randomnum * 94
                    indexchar = int(indexchar)
                    passarray.append(indexchar)
                    if passwordlenght >= int(args.min):
                        for indexing in range(len(passarray)):
                            password = password + chr(array[passarray[indexing]])
                        file.write(str(index) + " " + str(password))
                        file.write("\n")
            file.close()

if __name__ == '__main__':
    randomobj = randomPass()
    randomobj.randomPass()

