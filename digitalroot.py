#digital root-->iterative sum of until we get a single digit

#define function
#while loop
#find sum of digits until and keep replacing sum with n
#if sum is not greater than 9..print sum
#take user input
#call func and print output

def digital_root(n):
    while n>9:
        sum=0
        i=n
        while i>0:
            sum=sum+i%10
            i=i//10
        n=sum
    print(f"digital root is {sum}")
n=int(input("enter n value:"))
digital_root(n)
    

