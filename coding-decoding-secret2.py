import random
import string
def coding():
    x = input("Enter a word: ")
    splited = x.split(" ")
    # print(splited)

    for i in splited:
        split_2 = []
        for j in i:
            split_2.append(j)
        if (len(split_2) <= 2):
            split_2.reverse()

        # print(split_2)
        else:
            split_2.append(split_2[0])
            split_2.remove(split_2[0])
            for a in range(3):
                split_2.insert(0, random.choice(string.ascii_letters))
                split_2.append(random.choice(string.ascii_letters))
        print("".join(split_2), end=" ")
def decoding():
    x=input("Enter the statement to be decoded: ")
    splitted=x.split(" ")
    for i in splitted:
        split_2=[]
        for j in i:
            split_2.append(j)
        if(len(split_2)<3):
            split_2.reverse()
        else:
            for k in range(3):
                  split_2.pop(0)
            for l in range(3):
                  split_2.pop(-1)
            
            # print(split_2)
            split_2.insert(0,split_2[-1])
            split_2.pop()
            # print(split_2)

        print("".join(split_2), end=" ")
d="Welcome to secret code generator!!!!!!!!"
print(d.center)
x=int(input("Enter your choice\n 1. Want to generate secret code \n 2. Want to decode a coded statement\n Enter your choice: "))
if(x==1):
    coding()
elif(x==2):
    decoding()