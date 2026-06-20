def add (a,b):
    res = a + b
    print ("The result of addition", a ,"+",b, "is", res)
def subs (a,b):
    res = a-b
    print ("The result of substraction", a ,"-",b, "is", res)
def mult (a,b):
    res = a*b
    print ("The result of multiplication", a ,"*",b, "is", res)
def div (a,b):
    res = a/b
    print ("The result of division", a ,"/",b, "is", res)
def percent (a,b):
    res = a%b
    print ("The result of modulus", a ,"%",b, "is", res)
    
function = {
    "+": add,
    "-": subs,
    "/" : div,
    "*" : mult,
    "%" : percent
    
}

def thisIsFunction():   
    print(
"------------------------ \n" 
"|     Laura Natalia    |\n"
"|       Tangerang      |\n"
"------------------------")  

thisIsFunction() 

while (True):
    process = str(input("Enter Menu (+|-|/|*|%|stop): "))
    
    if (process=="stop"):
        print("Program stopped. Thank you for using my program.")
        break
        
    elif process in function:
        a= int(input("Value 1= "))
        b= int(input("Value 2= "))
        print(function[process](a,b))
    else:
        print("Input invalid.")
        continue
        
    
    
    
    
    


