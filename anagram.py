#####ANAGRAM######
'''CHARACHTER SHOULD BE SAME BUT MEANING CAN BE DIFFERENT.
IT IS ALWAYS WORK USING SORTED().'''

'''a='tea'
b='eat'
if sorted(a)==sorted(b):
    print("it is anagram")
else:
    print("it is not")'''

#armstrong number#####
'''a=153
total=0
b=str(a)
print(b)
power=len(b)
print(power)
for i in b:
    total=total+int(i)**power
if total==a:
    print("its armstrong number")
else:
    print("its not")'''
#to print table

'''for i in range(1,11):
    for j in range(2,11):
        print(i*j,end=' ')
    print()
print(f'{i}*{j}====={i*j}')'''

#
'''a="good day"
for i in range(len(a)):
    print(i+3,a[i])
print()
or
for i in enumerate(a,start=3):
    print(i)'''

    #syntax====for variable in enumerate(iterable,start=position)

1.#1.WAP to return a dictionary with word & its len pair
#from a string
'''string = 'hello good morning how are youu'
#exp o/p : {hello:5, guys:4, morning:7, how:3, are:3, you:4}
d={}
for i in string.split():
    #d.update({i:len(i)})

    d[i]=len(i)
print(d)'''
        
#2.2.WAP to count number of vowels present in given string
'''s = 'GooD mOrnIng'
total=0
for i in s:
    if i in "aeiouAEIOU":
        total=total+1
print(total)'''
#3.WAP to get below o/p:
'''s = 'Hi how are you'
for i in s.split():
    e=i[::-1]+" "+e
print(e)'''
#exp o/p : 'iH woh era uoy'



#4.WAP to print all the digits in a below list
'''l = ['hello', '123', 'hai', 'python', '345']
for i in l:
    if i.isdigit():
        print(i)'''

#8.Replace negative numbers with 0
'''numbers = [10, -5, 20, -3, 40]
for i in range(len(numbers)):
    if numbers[i]<0:
        numbers[i]=0
print(numbers)'''
#find the sum of even numbers from 1 to 20
'''sum=0
for i in range(1,21,1):
    if i%2==0:
        sum=sum+i'''
#count numbers divisible by 3 from 1 to 50
'''total=0
for i in range(1,51,1):
    if i%3==0:
        total=total+1
print(total)'''
#print position of each charachter
'''word="PYTHON"
for i in enumerate(word,start=1):
    print(i)'''
#count even and odd numbers in a list
'''num=[10,15,22,31,40,51]
even=[]
odd=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(print(even)
print(odd)'''

#wap to print repeated char and count of repetition
'''s="helloworld"
count={}
for i in s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)'''

#grouping flowers and annimals seperately

'''items=["lotus=flower","cat=animal","dog=animal","sunflower=flower"]
flower=[]
animal=[]
for i in items:
    if i ==flower:
        flower.append(i)
    else:
        animal.append(i)
print(flower)
print(animal)'''
#filter only charachters except digits
'''s="Think456 and 123 answers it 789 guys"
result=""
for i in s:
    if i.isalpha():
        result+=i
print(result)'''
#15.replace all vowels with *
'''s="hello world welcome to python"
e=""
for i in s:
    if i in "aeiouAEIOU":
        e+="*"
    else:
        e+=i
print(e)'''
        
###
'''a=[12,13,{15:15},(3,4,5),"anuja"]
list=[]
str=" "
tuple=()
dict={}
for i in a:
    if type(i)==isinstance(i,list):
        list.append(i)
    print(i)'''
'''d=d.fromkeys(["a","b","c"],[])
d[a].append(10)'''
'''a="anuja"
low=0
high=len(a)-1
mid=low+high//2
print(mid)
print(a[mid])'''
'''a="hello"
b=" "
count=0
for i in a:
    if a.count(i)>1:
        b=b+"_"
    else:
        b=b+i
print(b)'''
'''a=""
print(len(a))'''

a={}



