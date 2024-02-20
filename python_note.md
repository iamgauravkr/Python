# __________Lesson 1__________
### Python 
 __code__
 ```python
name="gaurav"
age = 20
old=False
print(name)
print(type(old))
print(type(old))
```

### Sum of two numbers
 __code__
 ```python
a=10
b=20
sum=a+b
print(sum)
```
or<bR>
__code__
```python
a,b=10,40
print(a+b)
```
### Substraction of two numbers
__code__
```python
a=10
b=20
diff=a-b
print(diff)
```
### Multiplication of two numbers
__code__
```python
a=10
b=20
mul=a*b
print(mul)
```
### Division of two numbers
 __code__
```python
a=10
b=20 
div=b/a
print(div)
```
### Print name,age,price by using user entered in one line 
 __code__
```python
name=input("name:")
age=int(input("age:"))
price=float(input("price:"))
print("My Name is ",name,"Age is: ",age,"and price is: ",price)
```
### Traffic light code 
__code__
```python
light = input("light:")
if(light=="red"):
    print("stop")
elif(light=="yellow"):
     print("ready")
elif(light=="green"):
     print("Go")
else:
    print("Light is Broken")

```
###  Grades Distribution of Students  
__code__
```python
Marks=float(input("Grade: "))
if(Marks>=90):
    print("A")
elif(Marks>=80 and Marks<90):
    print("B")
elif(Marks>=70 and Marks<80):
    print("C")
else:
    print("D")
```
__Question .__  Print output for<br>
                A=5 and G="M"<br>
                b=2 and G="F"<br>
__code__
```python
A=int(input("A: "))
G=input("G: ")
if((A==1 or A==2 )and G=="M"):
    print("Fee is 100")
elif((A==3 or A==4) or G=="F"):
    print("Fee is 200")
elif(A==5 and G=="M"):
    print("Fee is 300")
else:
    print("No Fee")
```
# Conditional statement 
### Single line 
__code__
```python
food=input("food: ")
eat ="yes" if(food=="cake") else "no"
print(eat)
```
__code__
```python
food=input("food: ")
print("sweet") if food=="cake" or food=="jalebi" else print("nosweet")
```
## Clever if / Ternary operator
__code__
```python
age=int(input("age: "))
vote = ("yes" , "no")  [age < 18]
print(vote)
```
__code__
```python
sal=float(input("salary: "))
tax=sal*(0.1,0.2) [sal>5000]
print(tax)
```
### Calculate simple interest
__code__
```python
p=float(input("principle: "))
r=float(input("Rate: "))
t=float(input("time: "))
si=(p*r*t)/100
print(si)
```
## Type conversion
__code__
```python
a=2
b=4.25
c=a+b  #2.00+4.25=6.25
print(c)
```
# Type casting
__code__
```python
a,b=2,"4"
c=int(b)
sum=a+c
print(sum)
```
# __Practice Qusetion__
__Question 1.__ Write a program to print sum of two user input<br>
__code__
```python
a=int(input("a: "))
b=int(input("b: "))
sum=a+b
print("sum is:",sum)
```
__Question 2.__ Write a program to print area of square of user given side of square.<br>
__code__
```python
a=float(input("a:"))
arofsq=a*a
print(arofsq)
```

__Question 3.__ WAP to input 2 floating point numbers and print their average. <br>
__code__
```python
a=float(input("a: "))
b=float(input("b: ")) 
average=(a+b)/2
print(average)
```

__Question 4.__ WAP to input 2 int numbers, a and b. Print True if a is greater than or equal to b. If not print False<br>
__code__
```python
a=int(input("a: "))
b=int(input("b: "))
if(a>b):
     print("True")

else:
    print("False")
```
# __________Lesson 2__________
# String Declaration Method
__code__
```python
-str1="this is one way to store string uder double qution\n" 
-str2='this is second way to store string\n' 
-str3="""this is third way to store string""" 
print(str1,str2,str3)
```
# Concatenation
__code__
```python
str1="Gaurav "
str2="kumar"
print(str1+str2)
print(len(str1),len (str2))
```
# Indexing
__code__
```python
str="Brain On Rent"
ch=str[10]
str[4]="k"  #we can't modify the string in python
print(ch)
print(str)
```
# Slicing
__code__
```python
str="Ramayan"
print(str[1:4]) #gives ama as output
print(str[0:4]) #gives Rama as output
print(str[:4]) #gives Rama as output
print(str[0:len(str)]) # gives Ramayan as output

print(str[-5:-2]) #gives may as output as indexing start from backside with -1. 
```

# String Function
__code__
```python
str="i am studying python from youtube"
print(str.endswith("ube")) #gives True
print(str.endswith("ue")) #gives False
print(str.capitalize()) # i bacomes capital letter but not change the original string
print(str) #gives as i am studying python from youtube , i doesn' change

str1=str.capitalize()
print(str1) # i becomes capital i permanent

str2="Gaurav"
print(str2.replace("G","S"))
print(str.replace("python","javascript"))

print(str.find("python")) #gives (14) no. of starting index from where it started 

print(str.count("from")) # gives no. of times word present in sentence.    
```

__Question__ WAP to input user's first name and find it's length.<br>
__code__
```python
"""name=input("first name: ")
print(name,"\n", len(name))  """
```
__Question__ WAP to find the occurence of $ in a string.<br>
__code__
```python
str= "$money$"
print(str.count("$"))  
```
# Conditional Statement
__code__
```python
marks=int(input("marks: "))
if(marks>=90):
    print("Grade: A")
elif(marks>=80 and marks<90):
    print("Grade: B")
elif(marks>=70 and marks<80):
    print("Grade: C")
else:
    print("Grade: D")  
```
# Nested if else
__code__
```python
age=int(input("age: "))
if(age>=18):
     if(age>80):
          print("can't drive")
     else:
        print("drive")
else:
    print("cannot drive") 
```

# __Practice Qusetion__
__Question 1.__ WAP to chack if a number entered by user is odd or even.<br>
__code__
```python
number=int(input("number: "))
if(number%2==0):
    print("Number is Even")
else:
    print("Number is Odd") 
```

__Question 2.__ WAP to find the greatest of 3 number entered by user.<br>
__code__
```python
num1=float(input("number1: "))
num2=float(input("number2: "))
num3=float(input("number3: "))
if(num1>num2 and num1>num3):
    print("Greatest Number is: ",num1)
elif(num2>num3):
     print("Greatest Number is: ",num2)
else:
     print("Greatest Number is: ",num3) 
```

__Question 3.__ WAP to check if a number is multiple of 7 or not.<br>
__code__
```python
num=int(input("number: "))
if(num%7==0):
    print("Number is Multiple of 7")
else:
    print("not multiple of 7") 
```

# __________Lesson 3__________
# Mutable
__code__
```python
student=["karan",118,111.11,"Kolkata"]
print(student)
print(student[0])

student[0]="arjun" # lists are mutable in python so it can be change
print(student) 
```

# Immutable
__code__
```python
str="hello"
str[0]="c"
print(str) # strings are immutable so cannot change  
```

# Slicing list
__code__
```python
marks=[45,78,56,79,56,90,100]
print(marks[:4]) # gives 45,78,56,79
print(marks[0])  # gives 45
print(marks[1:]) #gives 78,56,79,56,90,100
print(marks[-5:-1]) # gives 56,79,56,90  
```

# List method
__code__
```python
list=[1,2,3,4]
list.append(5)
print(list) #gives output[1,2,3,4,5]

list2=[2,8,1,54,6,4,3,8,9,10,7,]
list2.sort() #arrange the elements of list in ascending order
print(list2)

list2.sort(reverse=True) #arrange the elements of list in descending order
print(list2)

list3=['a','b','c','s','g','t','e','z','h']
list3.sort()#arrange the elements of list in ascending order
print(list3) 
list3.sort(reverse=True)#arrange the elements of list in descending order
print(list3)

list4=[3,4,2,5,6,7]
list4.reverse() # reverse the list 
print(list4)

list5=[4,5,7,9,8,6,1]
list5.insert(1,10)# insert value 10 at index 1
print(list5)

list6=[1,3,2,4,1,6]
list6.remove(1)#remove 1 which is in starting
print(list6)

list7=[1,2,3,5,6,3,2,7]
list7.pop(3)# pop the elements present at given index
print(list7)
```
- list are mutable data type where as tuple are immutable data type
- in list we use [ ] and in tuple we use parenthesis ( ) 

# Tuples
__code__
```python
tup=(12,23,5,7,8,1)
print(tup[0])
print(tup[1])
# tup[0]=5 # not allowed we cant change the value as tuple are immutable 
print(tup[1:4]) # gives 23,5,7
print(tup.index(5)) # gives 2 as it present on index 2
print(tup.count(7)) # gives 1 as output as it comes one time

tup1=()
print(tup1)
print(type(tup1)) # class 'tuple'

tup2=(1,)
print(tup2)
print(type(tup2)) # class 'tuple'

tup3=(1)
print(tup3)
print(type(tup3)) # class 'int' because no comma is after 1 is given for class tuple after 1 comma should be given

tup4=(1.0)
print(tup4)
print(type(tup4)) # class 'float' as float value is given

tup5=("hello")
print(tup5)
print (type(tup5)) # class 'string' as string value is given
```
# __Practice Qusetion__
__Question 1.__ WAP to ask the user to enter names of threir favourite movies and store thhem in a list.
__code__
```python
list=[]
fav1=input("enter your  1st favourite movies name: ")
fav2=input("enter your  2st favourite movies name: ")
fav3=input("enter your  3st favourite movies name: ")
list.append(fav1)
list.append(fav2)
list.append(fav3)
print(list) 
```

__Question 2.__ WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
__code__
```python
#list1=['madam','movie','book','wow']
list=[1,2,3,3,2,1]
list1=list.copy()
list1.reverse()
if(list1==list):
    print("palindrome")
else:
    print("not palindime")  
```

__Question 3.__ WAP to count the number of students with the “A” grade in the following tuple.
[”C”,“D”,“A”,“A”,“B”,“B”,“A”].
__code__
```python
tup=("C","D","A","A","B","B","A")
print(tup.count("A"))
```

#__Question 4.__ Store the above values in a list & sort them from “A” to “D”.
__code__
```python
list1=["C","D","A","A","B","B","A"]
list1.sort()
print(list1)
```
# __________Lesson 4__________
# Dictionary in python 
__code__
```python

info={
    "name":"Gaurav",
    "age":18,
    "subject":["python","c++","c"],
    "topic":["dictionary in python","listinpython"],
    "is_adult":True,
    "marks":[90,85,89,86]
   
}
print(info) 
print(info["age"])

info["name"]="Sonu"
info["subject[1]"]=90
print(info) 
```

# Nested dictionary
__code__
```python
student={
    "name":"Gaurav",
    "subject":{
        "physics":80,
        "english":90,
        "hindi":85
    }
}

print(student)
print(len(student)) #gives 2 as o/p
print(list(student.keys()))# gives ['name', 'subject'] as o/p    #returns all keys
print(student.values()) #o/p ["Gaurav",{'physics:80,'english':90, "hindi':85}]  #returns all values

print(student.items()) #returns all (key, val) pairs as tuples   o/p [('name','Gaurav'),('subject',{'physics:80,'english':90, "hindi':85})]


print(student['name']) #o/p "Gaurav" but when access name2 instead of name, which does not exist(name2) then it gives error 
print(student.get("name")) #o/p "Gaurav" but when access name2 instead of name, which does not exist(name2) then it print None as o/p 

student.update({"city":"delhi"}) #inserts the specified items to the dictionary 
print(student) #o/p {('name':'Gaurav'),('subject':{'physics:80,'english':90, "hindi':85},'city': 'delhi'}

new_dict={"city":"delhi"}
student.update(new_dict)# update the previous dictionary and also create a new dictionary with these values
print(student)  
```
# Set in python
-Set is the collection of the unordered items.<br>
-Each element in the set must be unique & immutable.<br>
-nums = { 1, 2, 3, 4 }<br>
-set2 = { 1, 2, 2, 2 }<br>
-repeated elements stored only once, so it resolved to {1, 2}

__code__
```python
collection={1,2,2,2,3,4,4,4,5,6,7, "helloooo","python"}
print(collection) #just remove the dublicate values and print the values
print(type(collection)) #class 'set'
print(len(collection))# gives 9  as remove the dublicate values  

collection2={}# empty dictionary not a set
print(type(collection2))

collection3=set()#empty set 
collection3.update(1)
collection3.update(2)
collection3.update(2) 
collection3.update(3)
collection3.update("python")# we can also pass string into the set 
collection3.update((1,2,3,4)) # we can update set bacause it is immutable which cannot be changed so its hash value is possible
# collection3.update([1,2,3,4]) # we can't update list because list is unhashable type means it is mutable its value can be changed 
collection3.remove(3) # remove 3 from set
print(type(collection3))
print(collection3) # gives 1, 2 as remove dublicate values and also remove 3 as per request
print(len(collection3))

#sets are mutable but elements of set are immutable

collection4={"apna college","hello","world","python","java"}
print(type(collection4))#set
print(collection4.pop())#pop random value from set
print(collection4.pop())#pop random value from set
```

# Set Method
__code__
```python
set1={1,2,3}
set2={2,3,4,5,6}
print(set1)
print(set2)
print(set1.union(set2)) #{1,2,3,4,5,6}
print(set1.intersection(set2))#{2,3}  
```

# __Practice Qusetion__
__Question 1.__ Store following word meanings in a python dictionary :<br>
table : “a piece of furniture”,“list of facts & figures”<br>
cat : “a small animal”  <br>
__code__
```python
dict={
    "table":["a piece of furniture","list of facts & figures"],
    "cat":"a small animal"
}
print(dict)  
```
__Question 2.__  You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.<br>
"python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C” <br>
__code__
```python
subject={"python","java","c++","python","javascript","java","python","java","c++","c"}
print(subject)#"python","java","c++","javascript,"c"
print(len(subject))#"python","java","c++","javascript,"c"
```
__Question 3.__  WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.  
__code__
```python
dictionary={}
sub1_marks=int(input("Marks of subject1:"))
dictionary.update({"Marks of subject1":sub1_marks})
sub2_marks=int(input("Marks of subject2:"))
dictionary.update({"Marks of subject2":sub2_marks})
sub3_marks=int(input("Marks of subject3:"))
dictionary.update({"Marks of subject3":sub3_marks})
print(type(dictionary)) 
print(dictionary)
```
__Question 4.__ Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of built-in data types).<br>
__code__
```python
values={9,"9.0"}
print(values) 
```
__code__
```python
values2={
    ("int",9),
     ("float",9.0)
}
print(values2)
```
# __________Lesson 5__________
# Loops in python
-Loops are used to repeat instructions<br>
__code__
```python
count=1
while count<=5:
print("hello")
count+=1
print(count)
```
__code__
```python
i=1
while i<=10:
    print("Python")
    i+=1
```
__code__
```python
    i=1
    while i<=20:
    print(i) #1,2.....20
    i+=1
```
__code__
```python
i=5
while i>=1:
    print(i)#5,4,3,2,1
    i-=1
```
# __Practice Qusetion__
__Question 1.__  Print numbers from 1 to 100
__code__
```python
i=1
while i<=100:
    print(i)#1,2,3,4,......100
    i+=1
```
__Question 2.__  Print numbers from 100 to 1
__code__
```python
i=100
while i>=1:
    print(i)
    i-=1
```
__Question 3.__  Print the multiplication table of a number n.
__code__
```python
n=int(input("enter the table no: "))
i=1
while i<=10:
    print(n*i)
    i+=1
 ```
__Question 4.__  Print the elements of the following list using a loop:<br>
[1, 4, 9, 16, 25, 36, 49, 64, 81,100] <br>
__code__
```python
list=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i=0
while i<=len(list)-1:
    print(list[i])
    i+=1
```

__Question 5.__ Search for a number x in this tuple using loop:<br>
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]<br>
__code__
```python
list=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
n=int(input("search: "))
i=0
while i<=len(list)-1:
    if(list[i]==n):
        print("present at index: ",i)
    i+=1
```
 # **Break and Continue**
__code__
```python
i=0
while i<=5:
    if(i==3):
       i+=1
       continue #skip
    print(i)#0,1,2,4,5
    i+=1
```
__code__
```python
i=0
while i<=10:
    if(i%2==0):
        i+=1
        continue #skip 
    print(i)#1,3,5,7,9
    i+=1
```
__code__
```python
i=0
while i<10:
    if(i%2 != 0):
        i+=1
        continue
    print(i)#0,2,4,6,8
    i+=1
```
# **For loop**
__code__
```python
nums=[1,2,3,3,4,5]
for val in  nums:# for loop initilize syntax
    print(val)
```
__code__
```python
vegitables=["potato","brinjle","pea","lady's-finger","tomato"]
for val in vegitables:
    print(val)
```
### number in tuple 
__code__
```python
tup=(0,1,2,3,4,5,6,7,8,9)
for num in tup:
    print(num)
```
__code__
```python
str="apnabihar"
for char in str:
    print(char) 
```
__code__
```python
str="apnacollege"
for char in str:
    if(char == 'i'):
        print(" o found")
        break
    print(char)
else:
    print("end")
```

__Question__ Print the elements of the following list using a loop:<br>
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
__code__
```python
list=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for ele in list:
    print(ele)
```
__Question__ Search for a number x in this tuple using loop:<br>
(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
__code__
```python
tup=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
num=int(input("search: "))
i=0
for el in tup:
    if(el==num):
        print("num fond at index ",i)
        break  
    i+=1
else:
         print("not found")  
```
# Range()
-Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.<br>
-range( start?, stop, step?)
__code__
```python
seq=range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])
```
__code__
```python
seq = range(10)
for el in seq:
    print(el)
```
__code__
```python
for el in range(10):#range(stop)
    print(el)
```
__code__
```python
for el in range(3,10):#range(start,stop)
    print(el)
```
__code__
```python
for el in range(3,10,2):#range(start,stop,step)
    print(el) 
```
__Question__ Even number using range under 100<br>
__code__
```python
for el in range(0,101,2):#range(start,stop,step)
    print(el)
```
__Question__ odd number using range under 100.<br>
__code__
```python
for el in range(1,100,2):#range(start,stop,step)
    print(el)
```
# Practice Question
-using for & range( )<br>
__Question 1.__ Print numbers from 1 to 100.<br>
__code__
```python
for el in range(1,101):#range(start,stop)
    print(el)
```
__Question 2.__ Print numbers from 100 to 1.<br>
__code__
```python
for el in range(100,0,-1): #range(start,stop)
    print(el)
```
__Question 3.__ Print the multiplication table of a number n.<br>
__code__
```python
n=int(input("table: "))
for el in range(1,11):
    print(el*n)
```
# Pass Statement
-pass is a null statement that does nothing. It is used as a placeholder for future code.<br>
__code__
```python
for el in range(10):
 #empty
 print("some useful work")#gives error as we can't skip we have to write for that loop but by using pass we can skip
 ```
__code__
```python
for el in range(10):
    pass
print("some useful work") 
```
__code__
```python
if 1>5:
    pass
print("work is useful")
```
# Practice Question
__Question 1.__ WAP to find the sum of first n numbers. (using for and range())<br>
__code__
```python
n=int(input("number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print("Total sum: ",sum)
```
__Question 2.__WAP to find the sum of first n numbers. (using while)<br>
__code__
```python
n=int(input("number:"))
sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print("Total sum: ",sum)
```
__Question 3.__ WAP to find the factorial of first n numbers. (using for)<br>
__code__
```python
n=int(input("number:"))
# i=1
fact=1
for i in range(1, n+1):
    fact*=i
    # i+=1
print("Factorial is:",fact)
```


__Question 4.__ WAP to find the factorial of first n numbers. (using while)<br>
__code__
```python
n=int(input("number:"))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("Factorial is: ",fact)
```
# __Lesson 6__
# Function & Recursion
# _Function_
- Block of statements that perform a specific task.<br>
__code__
```python
def cal_sum(a,b):#parameters
    sum=a+b
    print(sum)
    return sum
cal_sum(4,20)#funtion call
cal_sum(23,87)#funtion call
cal_sum(47,53)  #funtion call 
```
__code__
```python
def print_hello():
    print("hello!")
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()
```
__code__
```python
def print_hello():
    print("hello!")

output=print_hello()
print(output) #none
```
# Average of 3 numbers
__code__
```python
def cal_avg(a,b,c):
    avg=(a+b+c)/3
    print(avg)
    return avg
cal_avg(4,6,5)
cal_avg(20,47,67)
```
__code__
```python
print("Gaurav","Kumar")#seperate

print("Gaurav")#seperate
print("kumar")#end "\n"

print("Guarav",end=" ")
print("kumar")
```
__code__
```python
def cal_product(a=2,b=3): #method1
    print(a*b)
    return a*b
cal_product()

def cal_product(a,b=9): #method2
    print(a*b)
    return a*b
cal_product(8)
```
__Question 1.__ WAF to print the length of a list. ( list is the parameter)
__code__
```python
cities={"patna","delhi","kolkata","mumbai"}
# num=(1,2,3,4,5,6,7)
heroes=("Thor","captain america","iron man","doctor strange")
def list_length():
    print(len(cities))
    print(len(heroes)) 
list_length()
```
__Question 2.__ WAF to print the elements of a list in a single line. ( list is the parameter)
__code__
```python
cities={"Patna","kolkata","hajipur","mumbai","delhi","banglore"}
heroes=("Thor","captain america","iron man","doctor strange")
def list_print(list):
    for item in list:
        # print(cities)
        print(item,end=" ")
        
list_print(heroes)
```
__Question 3.__ WAF to find the factorial of n. (n is the parameter)
__code__
```python
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("factorial: ",fact)
    return fact
fact(5)
```
__Question 4.__ WAF to convert USD to INR.
__code__
```python
def convert_dollar(dollar):
    inr=dollar*80.89
    print(dollar,"USD = ",inr,"indianrupees")
convert_dollar(5)
```
__code__
```python
def cal_even_odd(num):
    if(num%2==0):
        print("even")
    else:
        print("odd")
cal_even_odd(5)
```
# _Recursion_
- When a function calls itself repeatedly.<br>
__code__
```python
def show(n):
    if(n == 0):
        return 
    print(n)
    show(n-1)
show(5)
```
__code__
```python
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
print(fact(5))
```
__question 1.__ Write a recursive function to calculate the sum of first n natural numbers.<br>
__code__
```python
def sum(n):
    if(n==0):
        return 0
    # else:
    return  sum(n-1)+n
calsum=sum(5)
print(calsum)
```
__Question 2.__ Write a recursive function to print all elements in a list.
(Hint : use list & index as parameters)<br>
__code__
```python
def city(list, idx=0):
    if(idx==len(list)):
        return 
    print(list[idx])
    city(list, idx+1)
cities=["Patna","kolkata","hajipur","mumbai","delhi","banglore"]
city(cities)
```
