#tail recursion for factorial
def factorial(n,i=1):
    if(n==0):
        return i;
    else:
        return factorial(n-1,i*n)
    
#non tail recursion for factorial
def fact(a):
    if a==0 or a==1:
        return 1
    else:
        return a*fact(a-1)
    
print("fact=",factorial(5))
print("fact=",fact(5))