#prime factorization
#12-->2,3

#define function
#create a list and put all the primes from 1 to n in it
#now divide n with those primes until n%i==0
#take user input for n
#call func and print output

def primefact(n):
    a=[]
    b=[]
    for i in range(2,n):
        for j in range(2,i):
            if i%j==0:
                break
        else:
           a.append(i)
    for i in a:
        while n%i==0:
                b.append(i)
                n=n//i
    return b

n=int(input("input n value:"))
print(primefact(n))

