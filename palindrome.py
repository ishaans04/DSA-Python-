def check_pal(n):
    num_rev=0
    d=n

    while n>0:
        last=n%10
        num_rev = (num_rev * 10) + last
        n//=10

    if d==num_rev:
        print("This is a palindrome")
    else:
        print("Not a palindrome")

x=int(input("Enter your number "))
check_pal(x)