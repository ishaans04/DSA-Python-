#Approach 1:

def GCD(n1,n2):
    gcd=1
    for i in range (1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            gcd = i
    return gcd 

n1=int(input("enter first number : "))
n2=int(input("enter second number : "))
print(GCD(n1,n2))

#Approach 2:

def GCD2(n1,n2):
    for i in range(min(n1,n2),0,-1):
        if n1%i==0 and n2%i==0:
            return i
    return 1 

n1=int(input("enter first number : "))
n2=int(input("enter second number : "))
print(GCD2(n1,n2))
    
#Approach 3(Optimal):

def GCD3(n1,n2):
    while n1>0 and n2>0:
        if n1>n2:
            n1=n1%n2
        else:
            n2=n2%n1
        
    if n1==0:
        return n2
    else:
        return n1 

a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
print(GCD3(a,b))
