from persistence import *

def main():
    #TODO: implement
    # print("Activities")
    # for a in repo.activities.find_all():
    #     print("(" + str(a.product_id) + ", " + str(a.quantity) + ", " + str(a.activator_id) +", " + str(a.date.decode()) +")")

    # print("Branches")
    # for b in repo.branches.find_all():
    #     print("(" + str(b.id) + ", " + str(b.location.decode()) + ", " + str(b.number_of_employees) + ")")

    # print("Employees")
    # for e in repo.employees.find_all():
    #     print("(" + str(e.id) + ", " + str(e.name.decode()) + ", " + str(e.salary) +  ", " + str(e.branche) +")")
    
    # print("Products")
    # for p in repo.products.find_all():
    #     print("(" + str(p.id) + ", " + str(p.description.decode()) + ", " + str(p.price) +  ", " + str(p.quantity) +")")
    
    
    # print("Suppliers")
    # for s in repo.suppliers.find_all():
    #     print("(" + str(s.id) + ", " + str(s.name.decode()) + ", " + str(s.contact_information.decode()) + ")")

    # print("Employees report")
    # sorted_list = list(repo.employees.find_all())
    # sorted_list.sort(key=lambda x: x.name) 
    # for e in sorted_list:
    #     activitie_l = repo.activities.find(activator_id = e.id)
    #     sum_employee_income = 0
    #     for activitie in activitie_l:
    #         product_quantity = activitie.quantity
    #         product_price = repo.products.find(id = activitie.product_id).pop().price
    #         sum_employee_income += product_price*product_quantity
        
    #     print(str(e.name.decode()) + " " + str(e.salary) + " " + str(repo.branches.find(id = e.branche).pop().location.decode()) + " " + str(sum_employee_income))
    
    print("Activities report")
    
    
    c = repo._conn.cursor()
    c.execute("SELECT a.date, p.description, a.quantity , e.name, s.name FROM activities as a JOIN products as p ON a.product_id = p.id LEFT JOIN employees as e ON e.id = a.activator_id LEFT JOIN suppliers as s ON s.id = a.activator_id")
    # print(c.fetchall())
    
    # req_table = list(c.fetchall())
    # req_table.sort(key=lambda x: x[0])
    # for a in req_table:
    #     print(a)
        # print_list = list(a)
        # for var in print_list:
        #     if isinstance(var,str):
        #         var = var.decode()

        # print(print_list)

    for a in c.fetchall():
        print(a)
            
        
      

        
            
    

    
    pass

if __name__ == '__main__':
    main()