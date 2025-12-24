#ugly numbers-->number who's prime factor are only 2,3,5
#define a func
#create a list with 2,3,5
#for loop to iterate through list
#while loop to check divisibility
#take user input
#call func and print output

def uglynum(n):
    u=[2,3,5]
    temp=n
    for i in u:
        while n>0 and n%i==0:
                n=n//i
    if n==1:
        print(f"{temp} is an ugly number")
    else:
        print(f"{temp} is not an ugly number")

n=int(input("enter n value:"))
uglynum(n)
    
                
