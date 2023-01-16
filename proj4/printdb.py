from persistence import *

def main():
    #TODO: implement
    print("Activities")
    for a in repo.activities.find_all():
        print("(" + str(a.product_id) + ", " + str(a.quantity) + ", " + str(a.activator_id) +", " + "'"+str(a.date.decode())+"'" +")")

    print("Branches")
    for b in repo.branches.find_all():
        print("(" + str(b.id) + ", " + "'"+str(b.location.decode())+"'" + ", " + str(b.number_of_employees) + ")")

    print("Employees")
    for e in repo.employees.find_all():
        print("(" + str(e.id) + ", " + "'" +str(e.name.decode())+"'" + ", " + str(e.salary) +  ", " + str(e.branche) +")")
    
    print("Products")
    for p in repo.products.find_all():
        print("(" + str(p.id) + ", " + "'"+str(p.description.decode())+"'" + ", " + str(p.price) +  ", " + str(p.quantity) +")")
    
    
    print("Suppliers")
    for s in repo.suppliers.find_all():
        print("(" + str(s.id) + ", " +"'"+ str(s.name.decode())+"'" + ", " + "'"+str(s.contact_information.decode())+"'" + ")")

    print()
    print("Employees report")
    sorted_emp_rep_list = list(repo.employees.find_all())
    sorted_emp_rep_list.sort(key=lambda x: x.name) 
    for e in sorted_emp_rep_list:
        activitie_l = repo.activities.find(activator_id = e.id)
        sum_employee_income = 0
        for activitie in activitie_l:
            product_quantity = activitie.quantity
            product_price = repo.products.find(id = activitie.product_id).pop().price
            sum_employee_income += product_price*product_quantity
        
        print(str(e.name.decode()) + " " + str(e.salary) + " " + str(repo.branches.find(id = e.branche).pop().location.decode()) + " " + str(-1*sum_employee_income))
    
    print()
    print("Activities report")
    
    c = repo._conn.cursor()
    c.execute("SELECT a.date, p.description, a.quantity , e.name, s.name FROM activities as a JOIN products as p ON a.product_id = p.id LEFT JOIN employees as e ON e.id = a.activator_id LEFT JOIN suppliers as s ON s.id = a.activator_id")


    sorted_act_rep_list = list(c.fetchall())
    sorted_act_rep_list.sort(key=lambda x: x[0]) 


    for a in sorted_act_rep_list:
        memb1 = a[3].decode() if isinstance(a[3],bytes) else a[3]
        memb2 = a[4].decode() if isinstance(a[4],bytes) else a[4]
        printed_tuple = (a[0].decode(),a[1].decode(),a[2],memb1,memb2)
        print(printed_tuple.__str__())


    # for a in c.fetchall():
    #     string_to_print = "(" +"'" + str(a[0].decode())+"'" + ", " + "'"+ str(a[1].decode())+"'" + ", " + str(a[2]) + ", "
    #     # print(type(a[3]))
    #     if isinstance(a[3],bytes):
    #         string_to_print += "'" + str(a[3].decode())+"'" + ", "
    #     else :
    #         string_to_print += str(a[3]) + ", " 
    #         # print(str(a[3]))

    #     if isinstance(a[4],bytes):
    #         string_to_print += "'" + str(a[4].decode())+"'" + ")"
    #     else :
    #         string_to_print += str(a[4]) + ")"
    #         # print(str(a[4]))
    #     print(string_to_print)
    
            
        
      

        
            
    

    
    pass

if __name__ == '__main__':
    main()