from persistence import *

import sys

def main(args : "list[str]"):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            #TODO: apply the action (and insert to the table) if possible
            if int(splittedline[1]) < 0:
                prodL = repo.products.find(id = splittedline[0])
                product = prodL.pop()
                print(product.quantity)
                # prod = prodL.pop()
                # int(prod.quantity) > -1*int(splittedline[1])
                # repo.employees.find(splittedline[2])

            if int(splittedline[1]) > 0:
                prodL = repo.products.find(id = splittedline[0])
                product = prodL.pop()
                # repo.suppliers.find(splittedline[2])
                repo.products.delete(product)
                new_product = Product(product.id,product.description,product.price,int(product.quantity)+int(splittedline[1]))
                repo.products.update(new_product)



if __name__ == '__main__':
    main(sys.argv)



# python3 action.py action.txt