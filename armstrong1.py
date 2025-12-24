##armstong numbers in the given range

#define function
#for loop
#store i value in temp and and store length of i in l
#while loop
#take user input
#call func and print output

def armstrong(n1,n2):
    arms=[]
    for i in range(n1,n2+1):
        temp=i
        sum=0
        l=len(str(i))
        while i>0:
            digit=i%10
            a=digit**l
            sum+=a
            i=i//10
        if temp==sum:
           # print(f"{temp} is an armstrong number")
           arms.append(temp)
    return arms
def main():
    n1=int(input("Enter start number:"))
    n2=int(input("Enter end number:"))
    armstrong(n1,n2)
if __name__=="__main__":
    main()
