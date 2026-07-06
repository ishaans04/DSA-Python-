def pattern9(n):
    p=n//2
    for i in range(p):
        #space
        for j in range(p-i-1):
            print(' ', end=" ")
        #star
        for j in range((2*i)+1):
            print("*",end=" ")
        #space
        for j in range(p-i-1):
            print(' ', end=" ")
        print()

def patterns9(n):
    p=n//2
    for i in range(p):
        for j in range(i):
            print(' ', end=" ")
        for j in range((2*p)-((2*i)+1)):
            print('*',end=" ")
        for j in range(i):
            print(' ', end=" ")
        print()

n=int(input("Enter the number of rows you want"))

pattern9(n)
patterns9(n)