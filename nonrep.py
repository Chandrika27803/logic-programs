#first non repeating char in a string

#define function
#for loop
#compare every letter in the string to every letter except itself
#if same break the loop
#print first non repeating char
#take user input
#call func and print output

def nonrepeatingchar(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i]==s[j] and i!=j:
               break
        else:
            print(f"first repeating character in the string is '{s[i]}' at index '{i}'")
            return

s=input("enter string:")
nonrepeatingchar(s)
