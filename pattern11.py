'''
1
0 1
1 0 1
0 1 0 1             ( When i=even, It starts with 1 and alternates, else it starts with 0 and alternates)
1 0 1 0 1

'''

def pattern11(n):
    for i in range(n):
        if i%2==0:
            c=1
        else:
            c=0

        for j in range(i+1):
            print(c,end = " ")
            c=1-c
        print()

x=int(input("Enter number of rows"))
pattern11(x)