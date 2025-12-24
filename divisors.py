#perfect-->if sum of divisors=num
#abundant-->if sum of divisors>num
#deficient-->if sum of divisors<num

#define func
#for loop
#sum divisors
#comapare sum with num
#call func and print otp
def divisors(n):
    sum=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            sum+=i
    if sum==n:
        print(f"{n} is perfect num")
    elif sum<n:
        print(f"{n} is deficient num")
    else:
        print(f"{n} is abundant num")
    
    
n=int(input("enter n value:"))
divisors(n)
    
