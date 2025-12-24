#prime range

#define a function
#iterate the for loop from start to end+1 of range
#in the inner forloop take range from 2 to i and check if each number is prime
#if not->break the loop
#if prime append it to the list
#call func and print list
def prime(l,r):
    a=[]
    for i in range(l,r+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
           a.append(i)
    return a

l=int(input("input l value:"))
r=int(input("input r value:"))
print(prime(l,r))

