#nth fibonacci number
#0 1 1 2 3 5 8 13..

#define a func
#set n=1 & n=2 as 0 and 1
#since we have to find the nth element we have get the sum of (n-1) and (n-2)th elements
#take n value from user
#call the func and rint output

def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def main():
    n=int(input("enter a number:"))
    #print(fib(n))
    fib(n)
if __name__=="__main__":
    main()









