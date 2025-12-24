#word frequency-print most frequent(case sensitive)

#define a function
#split the sentence into words
#create a dictionary to store words and their count
#check if each word is in the dict-->if yes increment count by 1,if no keep count=1
#for loop to print word and its count
#take user input
#call func and print output

def word_frequency(s):
   words=s.split()
   freq={}
   for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
   for word,count in freq.items():
        print((word,count))

s=input("enter the sentence:")
word_frequency(s)
