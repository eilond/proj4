from persistence import *

def main():
    #TODO: implement
    print("Activities")
    for a in repo.activities.find_all():
        print("(" + str(a.product_id) + ", " + str(a.quantity) + ", " + str(a.activator_id) +", " + str(a.date.decode()) +")")

    print("Branches")
    for b in repo.branches.find_all():
        print("(" + str(b.id) + ", " + str(b.location.decode()) + ", " + str(b.number_of_employees) + ")")

    print("Employees")
    for e in repo.employees.find_all():
        print("(" + str(e.id) + ", " + str(e.name.decode()) + ", " + str(e.salary) +  ", " + str(e.branche) +")")
    
    print("Products")
    for p in repo.products.find_all():
        print("(" + str(p.id) + ", " + str(p.description.decode()) + ", " + str(p.price) +  ", " + str(p.quantity) +")")
    
    
    print("Suppliers")
    for s in repo.suppliers.find_all():
        print("(" + str(s.id) + ", " + str(s.name.decode()) + ", " + str(s.contact_information.decode()) + ")")

    
    pass

if __name__ == '__main__':
    main()