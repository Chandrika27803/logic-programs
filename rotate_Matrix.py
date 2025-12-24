#import libs
#taking user input for length of the matrix
#taking array input from user

#transpose:
#we have to 2 for loop one for rows and for columns
#and initialize the loop from row 0 and we are going to check the columns by skipping the previous.
#example:
#for i in range(n):
# for j in range(i+1,n):

#swapping through row:
#traverse through each row
#reverse the elements of row means the columns for each row


#print the output
def transpose(mat,n):
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            
    return mat
    
def rev(mat,n):
    for row in range(n):
        start=0
        end=n-1
        while start<end:
            mat[row][start],mat[row][end]=mat[row][end],mat[row][start]
            start+=1
            end-=1
    return mat
            
#main
n=int(input("Enter length of sq matrix: "))
arr=[]
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input(f"enter the element of {i} {j} :" )))
    arr.append(row)
print("Orginal Matrix:",arr)
res=transpose(arr,n)
print("Transposed matrix:",res)
print("After rotating matrix:",rev(res,n))
