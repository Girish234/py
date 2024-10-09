def fact(n):
    if(n==0):
        return 1
    else:
            return n*fact(n-1)
def binco(n, r):
    return fact(n) // (fact(r) * fact(n - r))
n=int(input("enter the value of n"))
r=int(input("enter the value of r"))
if(n<r):
    print("invalid inputs")
else:
    result= binco(n,r)
    print(f"\n{result}")