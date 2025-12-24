#Two-sum(indices)-return valid pair
#take a list and target as input
#find indices of number whose sum==target

#define function
#take an empty list to store index
#for loop
#add every elements to all the next element and check if sum==target
#if yes append the indices to the created list
#take user input
#call the func and print output 

def twosum(a,t):
    l=len(a)
    s=[]
    for i in range(l):
        for j in range(i+1,l):
            if a[i]+a[j]==t:
                s.append((i,j))
    print(s)
            
a=list(map(int,input("enter elements of list:").split()))
t=int(input("enter target sum:"))
twosum(a,t)
