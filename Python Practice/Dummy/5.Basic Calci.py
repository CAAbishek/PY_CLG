def calci( ):
    n1= float(input("Enter 1st Numeber: "))
    op= input("Enter Operator: ")
    n2= float(input("Enter 2nd Numeber: "))
   

    if op =='+' :
        return n1+n2
    elif op =='-':
        return n1-n2
    elif op=='*':
        return n1*n2
    elif op=='/':
        return n1/n2
    else:
        print ("Invalid operator")



print(calci())

