'''           *
             ***
            *****       [space, * ,space]
           *******
          *********

        {(n-i-1) -> spaces
        (2xi)+1 -> *}

        (3 loops)

'''

def pattern7(n):
    for i in range(n):
        #space
        for j in range(n-i-1):
            print(" ", end=" ")
        #star
        for j in range((2*i)+1):
            print('*', end=' ')
        #space
        for j in range(n-i-1):
            print(" ", end=" ")
        print()

pattern7(5)