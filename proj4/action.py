from persistence import *

import sys

def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            #TODO: apply the action (and insert to the table) if possible
            if int(splittedline[1]) < 0:
                print(splittedline[0])
                prodL = repo.products.find(id = 3)
                print("hello")
                # prod = prodL.pop()
                # int(prod.quantity) > -1*int(splittedline[1])
                # repo.employees.find(splittedline[2])

            # if int(splittedline[1]) > 0:
                # repo.suppliers.find(splittedline[2])



if __name__ == '__main__':
    main(sys.argv)