#Harshad number-->number divisible by the sum of its digits
#list harshad number upto n

#define function
#for loop
#store i in temp to avoid modifying original value
#find sum of digits
#check if n divisble by sum
#take user input
#call func and print output

def harshad(n):
    a=[]
    for i in range(1,n+1):
        temp=i
        sum=0
        while temp>0:
            sum=sum+temp%10
            temp=temp//10
        if i%sum==0 and sum!=0:
            #print(f"{i} is a harshad number")
            a.append(i)
    return a
def main():         
    n=int(input("enter n value:"))
    harshad(n)
if __name__=="__main__":
    main()
        
