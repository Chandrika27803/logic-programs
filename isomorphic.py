#isomorphic strings
#2 strings where each char in first string mapped with another char to get the second string

#define a func
#check if the len of two strings is same
#if yes-->create two dictionaries for mapping of all the characters
#for loop-->initially asign char1 and char 2 with first char of both strings
#chech if char1 is in the dictionary and check if mapping of char1 is to char2-->do same for char 2 and mapping2
#if both are false then map char 1 and char 2
#continue till the end of the string
#take user input
#call func and print output

def isomorphic(s1,s2):
    if len(s1) != len(s2):
        return False
    else:
        maps1={}
        maps2={}
        for i in range(len(s1)):
            ch1,ch2=s1[i],s2[i]
            if ch1 in maps1 and maps1[ch1]!=ch2:
               return False
            if ch2 in maps2 and maps2[ch2]!=ch1:
                return False
            
            maps1[ch1]=ch2
            maps2[ch2]=ch1
            
        return True

s1=input("enter string1:")
s2=input("enter string2:")
if isomorphic(s1,s2)==True:
    print(f"{s1} and {s2} are isomorphic")
else:
    print(f"{s1} and {s2} are not isomorphic")
