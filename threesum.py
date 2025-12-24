#three sum zero
#take list as input and return 3 unique numbers whose sum is zero in sorted order

#define function
#take an empty list to store index
#for loop
#check if all 3 elements are unique
#check is sum=0
#sort the numbers to avoid diplicates in the list
#append them to the list
#take user input
#call the func and print output

def threesumzero(a):
    l=len(a)
    s=[]
    for i in range(l):
        for j in range(i+1,l):
            for k in range(j+1,l):
                if a[i]!=a[j] and a[j]!=a[k] and a[k]!=a[i]:
                    if a[i]+a[j]+a[k]==0:
                        b=sorted([a[i],a[j],a[k]])
                        if b not in s:
                            s.append(b)           
    return s

a=list(map(int,input("enter elements of list:").split()))
print(threesumzero(a))
