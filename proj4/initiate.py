from persistence import *

import sys
import os
def add_branche(splittedline : list[str]):
    #TODO: add the branch into the repo

    #------ADDED--------
    dbcon = sqlite3.connect("bgumart.db")
    with dbcon:
        cursor = dbcon.cursor()
        cursor.execute("INSERT INTO branches VALUES(?,?,?)",
                       (splittedline[0],splittedline[1],splittedline[2]))
    # ------ADDED--------

    pass

def add_supplier(splittedline : list[str]):
    #TODO: insert the supplier into the repo

    #------ADDED--------
    dbcon = sqlite3.connect("bgumart.db")
    with dbcon:
        cursor = dbcon.cursor()
        cursor.execute("INSERT INTO suppliers VALUES(?,?,?)",
                       (splittedline[0],splittedline[1],splittedline[2]))
    # ------ADDED--------


    pass

def add_product(splittedline : list[str]):
    #TODO: insert product

    #------ADDED--------
    dbcon = sqlite3.connect("bgumart.db")
    with dbcon:
        cursor = dbcon.cursor()
        cursor.execute("INSERT INTO products VALUES(?,?,?,?)",
                       (splittedline[0],splittedline[1],splittedline[2],splittedline[3]))
    # ------ADDED--------

    pass

def add_employee(splittedline : list[str]):
    #TODO: insert employee

    #------ADDED--------
    dbcon = sqlite3.connect("bgumart.db")
    with dbcon:
        cursor = dbcon.cursor()
        cursor.execute("INSERT INTO employees VALUES(?,?,?,?)",
                       (splittedline[0],splittedline[1],splittedline[2],splittedline[3]))
    # ------ADDED--------

    pass

adders = {  "B": add_branche,
            "S": add_supplier,
            "P": add_product,
            "E": add_employee}

def main(args : list[str]):
    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    # uncomment if needed
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()

    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])

if __name__ == '__main__':
    main(sys.argv)