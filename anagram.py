#groups words into anagram buckets

#define function
#take every word in the list sort it and compare it to remaining words in the list
#if it matches append them to the new list
#take user input
#call func and print output


def anagrams(s):
    a=[]
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if sorted(s[i])==sorted(s[j]):
                a.append((s[i],s[j]))
    return a

def main():
    s=list(map(str,input("enter words:").split()))
    print(anagrams(s))
    #anagrams(s)
if __name__=="__main__":
    main()


