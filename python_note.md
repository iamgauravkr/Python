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
# __Lesson 7__

The argument mode points to a string beginning with one of the following
 sequences (Additional characters may follow these sequences.):

 ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.<br>
__Code__
```python
f = open("demo.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()
```
__Code__
```python
f = open("demo.txt","r")
data=f.read(13)#gives text till 13
print(data)
f.close()
```
__Code__
```python
f = open("demo.txt","r")
line1=f.readline() #gives one line
print(line1)
f.close()
```
__Code__
```python
f = open("demo.txt","r")
data=f.read()
print(data)
f.close()

f = open("demo.txt","r")
line1=f.readline() #gives one line
print(line1)
f.close()

f = open("demo.txt","r")
line2=f.readline() #gives one line
print(line2)
f.close()
```
__Code__
```python
f = open("demo.txt","r")

data=f.read()
print(data) # print all text

line1=f.readline() #gives empty space
print(line1)

line2=f.readline() #gives empty space
print(line2)
f.close()
```
__Code__
```python
f=open("demo.txt","w")
f.write("i want to learn javascript next time")#write in given file and remove previous text
f.close()
```
__Code__
```python
f=open("demo.txt","a")
f.write("\nthen i will to learn nodejs") #write in given file 
f.close()
```
__Code__
```python
f=open("demo.txt","r+")
f.write("\n next") # r+ overwrites from starting
print(f.read())#read data from where it left to write
f.close()
```
### By using With 
__Code__
```python
with open("demo.txt","r") as f:
    data=f.read()
    print(data)

with open("demo.txt","w") as f:
    f.write("next to learn javascript/n then react react js\n then nodejs")
```

## Deleting a file
__Code__
```python
import os
os.remove("sample.txt")
```
# __Practice Question__
__Question 1.__  Create a new file “practice.txt” using python. Add the following data in it:<br>
 Hi everyone<br>
 we are learning File I/O<br>
 using Java.<br>
 I like programming in Java.<br>
__Code__
```python
f=open("practice.txt","w")
f.write("Hi everyone \n"
     "we are learning File I/O \n"
     "using Java. \n"
     "I like programming in Java.")
f.close()
```

__Question 2.__ WAF that replace all occurrences of “java” with “python” in above file.<br>
__Code__
```python
with open("practice.txt","r") as f:
    data = f.read()
new_data = data.replace("Java","python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)
```
__Question 3.__ Search if the word “learning” exists in the file or not.<br>
__Code__
```python
word="learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word)!=-1):
        print("exist")
    else:
        print("not exist")
```
- Solution by using with function<br>
__Code__
```python
def check_for_word():
    word="wlearning"
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word)!=-1):
            print("exist")
        else:
            print("not exist")
check_for_word()        
```
__Question 4.__ WAF to find in which line of the file does the word “learning”occur first.<br>
Print -1 if word not found <br>
__Code__
```python
def check_for_word():
    word="programming"
    with open("practice.txt","r") as f:
        data=True
        line_no = 1
        with open("practice.txt","r") as f:
            while data:
                data=f.readline()
                if(word in data):
                    print(line_no)
                    return 
                line_no+=1
    return -1            
print(check_for_word())          
```
__Question 5.__ From a file containing numbers separated by comma, print the count of even numbers<br>
__Code__
```python
with open("practice1.txt","r") as f:
    data=f.read()
    print(data)

    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            num=""
        else:
            num+=data[i]
```
__Solution__ <br>
__Code__
```python
count=1
with open("practice1.txt","r") as f:
    data=f.read()

    nums = data.split(",")
    for val in nums:
        if(int(val) %2 ==0):
            count+=1
print(count)
```
# __Lesson 8__
# OOP in Python
To map with real world scenarios, we started using objects in code.
This is called object oriented programming.

## Class & Object in Python
 Class is a blueprint for creating objects.<br>
 __Code__
 ```python
 # Creating class
 class Student:
     name = “karan kumar”

# creating object (instance)
 s1 = Student( )
 print( s1.name )
 ```
 __Code__
 ```python
class Student:
    name="Saurav"

s1=Student()
print(s1.name)

s2=Student()
print(s2.name)
```
 __Code__
 ```python
class car:
    engine="1205cc"
    type="mercedes-gls-maybech"
    color="black"
car1=car()
print(car1.type)
print(car1.color)
```
# _ _init_ _ Function
## Constructor
 All classes have a function called __init__(), which is always executed when the object is being
 initiated.<br>
  __Code__
 ```python
 # Creating class
 class Student:
 def __init__(self, fullname ):
 self.name = fullname
 #creating object
 s1 = Student( “karan” )
 print( s1.name )
```
 __Note__ : The  parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.<br>
 __Code__
 ```python
class Student:
    name="karan"
    def __init__():
       print("adding new database in student..")
s1= Student()
```
 __Code__
 ```python
class Student:
    college_name ="DU"
    #default constructor
    def __init__():
        print("adding new database in student..")
        #parameterized constructor
    def __init__(,fullname,marks):
        .name=fullname
        .marks=marks
        print("adding new database in student..")
s1= Student("samar",98)
s2= Student("DON",95)
print(s1.name,s1.marks)
print(s2.name,s2.marks)
print(Student.college_name)
```
# Class & Instance Attributes
## i) Class.attr
## ii) obj.attr
 __Code__
 ```python
class Student:
    college_name ="DU"
    name="anonymous" #class attribute of same name as object attribute
    #default constructor
    def __init__():
        print("adding new database in student..")
        #parameterized constructor
    def __init__(,fullname,marks):
        .name=fullname #object attribute > class attribute
        .marks=marks
        print("adding new database in student..")
s1= Student("samar",98)
s2= Student("DON",95)
print(s1.name,s1.marks)
print(s2.name,s2.marks)
```
# Methods
 Methods are functions that belong to objects.<br>
  __Code__
 ```python
#creating class
 class Student:
 def __init__(self, fullname ):
 self.name = fullname
 def hello(self):
 print(“hello”, self.name)

#creating object

 s1 = Student(“karan”)
 s1.hello()
```
 __Code__
 ```python
class Student:
    college_name ="DU"
    def __init__(,fullname,marks):
        .name=fullname 
        .marks=marks

    def welcome():#if we don't write  inside () then it throws error
        print("Welcome Student-", .name)

    def getmarks():
        return .marks
s1= Student("samar",98)
s1.welcome()
print(s1.getmarks())
```

# Practice Question
__Question__ Create student class that takes name & marks of 3 subjects as arguments in constructor.<br>
Then create a method to print the average
 __Code__
 ```python
class student:
        def __init__(,s_name,sub_marks):
            .std_name = s_name
            .subject_marks = sub_marks

        def print_info():
            print("Names: ",.std_name)
            print("Marks: ",.subject_marks)

        def avg_marks():
            sum=0
            for val in .subject_marks:
                sum += val
            print("Your average score is: ",sum/3)

s1 = student("Sonu",[85,90,58])
s1.print_info()
s1.avg_marks()
```
# Static Methods
 Methods that don’t use the self parameter (work at class level)<br>
  __Code__
 ```python
 class Student:
 @staticmethod #decorator
 def college( ):
 print( “ABC College” )
```
__Note__ : Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.<br>
 __Code__
 ```python
class student:
        def __init__(self,s_name,sub_marks):
            self.std_name = s_name
            self.subject_marks = sub_marks

        def print_info(self):
            print("Names: ",self.std_name)
            print("Marks: ",self.subject_marks)

        @staticmethod #decorator
        def clg():# here we didn't write self inside() and also gives no error because we use decorator(@staticmethod)
            print("semester score")

        def avg_marks(self):
            sum=0
            for val in self.subject_marks:
                sum += val
            print("Your average score is: ",sum/3)

s1 = student("sonu",[85,90,58])
s1.print_info()
s1.clg()
s1.avg_marks()
```
# Abstraction
 Hiding the implementation details of a class and only showing the essential features to the user.<br>
 __Code__
 ```python
class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def start(self):
        self.clutch=True
        self.acc=True
        print("Started...")

car1=car()
car1.start()
```
# Encapsulation
 Wrapping data and functions into a single unit (object).

# Practice Question
__Question 1.__ Create Account class with 2 attributes - balance & account no.<br>
Create methods for debit, credit & printing the balance.<br>
 __Code__
 ```python
class Account:
    def __init__(self, bal, acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited.")
        print("Total Balance is: ", self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited.")
        print("Total Balance is: ", self.get_balance())
    def get_balance(self):
        return self.balance

acc1 = Account(100000, 7322000100000888)
acc1.debit(1000)
acc1.credit(5000)
```
# Delete keyword
 del is used to delete object properties or object itself.<br>
 __Code__
 ```python
class student:
    def __init__(self,name):
        self.name = name

s1=student("sayan")#print sayan
print(s1.name)
del s1.name # del is used to delete object properties or object itself
print(s1.name) #throws error
```

# Private and Public
 __Code__
 ```python
class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    
    def reset_pass(self):
        print(self.__acc_pass) #acc_pass is private cannot access it outside the class

acc1=account("7322004562458","1235658")
print(acc1.acc_no)
```
 __Code__
 ```python
class person:
    __name="anonymous"

p1=person()
print(p1.__name) #we cannot access because it declared as private
```
 __Code__
 ```python
class person:
    __name="Anonyous"
    def __hello(self,name):
        print("hello person!")
    
p1=person()
print(p1.__hello)
```
 __Code__
 ```python
class person:
    __name="Anonyous"
    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1=person()
print(p1.welcome()) # call welcome and welcome calls hello but hello declared as private but we can access private within the class 
```

# Inheritance
## Types of inheritance
 i) single inheritance<br>
 ii) multi-level inheritance<br>
 iii) multiple inheritance<br>
 __Code__
 ```python
class car:
    color="Black"
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stoped...")

class toyota(car):
    def __init__(self,name):
        self.name=name

car1=toyota("Fortuner Legender")
car2=toyota("Hilux")
print(car1.name)
print(car1.color)
```

## Examples of multi-level inheritance
 __Code__
 ```python
class car:
    color="Black"
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stoped...")

class toyota(car):
    def __init__(self,type):
        self.type=type

class Fortuner(toyota):
    def __init__(self,type):
        self.type=type

car1=Fortuner("Diesel")
car1.start()
```
## Examples of multiple inheritance
 __Code__
 ```python
class A:
    varA="Welcome to class A"

class B:
    varB="Welcome to class B"

class C(A, B):
    varC="Welcome to class C"

c1=C()
print(c1.varA)
print(c1.varB)
print(c1.varC)
```

# Super Method
super() is used to access methods of the parent class
 __Code__
 ```python
class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stoped...")

class toyota(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()

car1=toyota("pirus","electric")
print(car1.type)
```

# class method 
 __Code__
 ```python
class person:
    name="anonymous"

    def changename(self,name):
        self.name=name

p1=person()
p1.changename("Rahul kumar")
print(p1.name)
print(person.name)
# output??
```
 __Code__
 ```python
class person:
    name="anonymous"

    def changename(self,name):
        self.person=name

p1=person()
p1.changename("Rahul kumar")
print(p1.name)
print(person.name)
```
## 1st method of class method to change name
 __Code__
 ```python
class person:
    name="anonymous"

    def changename(self,name):
        person.name=name

p1=person()
p1.changename("Rahul kumar")
print(p1.name)
print(person.name)
```
## 2nd method of class method to change name
 __Code__
 ```python
class person:
    name="anonymous"

    def changename(self,name):
        self.__class__.name="sayan"

p1=person()
p1.changename("Rahul kumar")
print(p1.name)
print(person.name)
```
## 3rd method of class method to change name using @classmethod
 __Code__
 ```python
class person:
    name="anonymous"
    
    @classmethod
    def changename(cls,name):
        cls.name = name

p1=person()
p1.changename("Anish kumar")
print(p1.name)
print(person.name)
```
# Property Decorator
__Normally__<br>
 __Code__
 ```python
class student:
    def __init__(self,maths,chem,phys):
        self.maths=maths
        self.chem=chem
        self.phys=phys
        self.percentage=str((self.maths+self.chem+self.phys)/3)+"%"

    def cal_percentage(self):
        self.percentage=str((self.maths+self.chem+self.phys)/3)+"%"

stud1=student(90,80,85)
print(stud1.percentage)
# by mistake teacher gives wrong marks of phys
stud1.phys=70
stud1.cal_percentage()
print(stud1.phys) # here teacher change the sub marks but percentage is still remain same so we create cal_percentage and update then print
print(stud1.percentage) 
```
## using property decorator
 __Code__
 ```python
class student:
    def __init__(self,maths,chem,phys):
        self.maths=maths
        self.chem=chem
        self.phys=phys
        # self.percentage=str((self.maths+self.chem+self.phys)/3)+"%"

    # def cal_percentage(self):
    #     self.percentage=str((self.maths+self.chem+self.phys)/3)+"%"

    @property
    def percentage(self):
        return str((self.maths+self.chem+self.phys)/3)+"%"

stud1=student(90,80,85)
print(stud1.percentage)

stud1.phys=70
print(stud1.percentage) 
```
__Note__: Read about getter() and setter()

# Polymorphism : operator overloading
## implicit  overloading
 __Code__
 ```python
print(2+3)#5
print("vande"+"bharat")#concatenate
print([1,2,3]+[4,5,6])#merge
```
 __Code__
 ```python
class complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    def shownumber(self):
        print(self.real,"i +",self.imaginary,"j")

    def add(self,num2):
        NewReal=self.real+num2.real
        NewImaginary=self.imaginary+num2.imaginary
        return complex(NewReal , NewImaginary)

num1=complex(4,5)
num1.shownumber()

num2=complex(8,9)
num2.shownumber()

num3=num1.add(num2)
num3.shownumber()
```
## using Operators & Dunder Functions
## Add
 __Code__
 ```python
class complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    def shownumber(self):
        print(self.real,"i +",self.imaginary,"j")

    def __add__(self,num2):
        NewReal=self.real + num2.real
        NewImaginary=self.imaginary + num2.imaginary
        return complex(NewReal , NewImaginary)

num1=complex(4,5)
num1.shownumber()

num2=complex(8,9)
num2.shownumber()

num3=num1+num2
num3.shownumber()
```
## Subtract using dunder
 __Code__
 ```python
class complex:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary

    def shownumber(self):
        print(self.real,"i +",self.imaginary,"j")

    def __sub__(self,num2):
        NewReal=self.real - num2.real
        NewImaginary=self.imaginary - num2.imaginary
        return complex(NewReal , NewImaginary)

num1=complex(4,5)
num1.shownumber()

num2=complex(8,9)
num2.shownumber()

num3=num1-num2
num3.shownumber()
```
__link__ add,sub,mul,... (https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)

# Practice Question
__Question:__ Define a Circle class to create a circle with radius r using the constructor<br>
 Define an Area() method of the class which calculates the area of the circle.<br>
 Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
 __Code__
 ```python
class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

c1=circle(4)
print(c1.area())
print(c1.perimeter())
```
__Question:__ Define a Employee class with attributes role, department & salary. This showDetails() method.<br>
Create an Engineer class that inherits properties from Employee & attributes B name & age.
 __Code__
 ```python
class Employee:
    def __init__(self,role,dept,sal):
        self.role = role
        self.dept = dept
        self.sal = sal
        
    def showdetails(self):
        print("Role: ",self.role)
        print("Dept: ",self.dept)
        print("Salary: ",self.sal)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("engineer","software-developer","12,00,000")

eng1=Engineer("Gaurav",25)
eng1.showdetails()
```
__Question:__ Create a class called Order which stores item & its price.<br>
Use Dunder function _ gt _( ) to convey that:
order1 > order2 if price of order1 > price of order2 <br>
 __Code__
 ```python
class order():
    def __init__(self,item,price):
        self.item = item
        self.price = price 

    def __gt__(self, ord2):
        return self.price > ord2.price

ord1=order("chips",20)
ord2=order("biscuit",10)

print(ord1>ord2)#true
```
