#product of array except self
#you have to create a new array where each element is a product of all elements in the array except itself

#define func
#create empty list to store products
#for loop
#take product=1
#another for loop to compare indexes
#if indexes are different take product and append to list
#take user input
#call func and print output

def productarr(a):
    b=[]
    for i in range(len(a)):
        p=1
        for j in range(len(a)):
            if i!=j:
                p*=a[j]
        b.append(p)
    print(b)
                

a=list(map(int,input("enter elements of array:").split()))
productarr(a)
