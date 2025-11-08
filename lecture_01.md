

# Today's Agende

1. What is a Programming Language?
2. High Level Programming Language vs Low Level Programming Language
3. Complier vs Interpreter
4. Introduction to Python
5. Varibles/Keywords/Identifiers/Comments/Operators/Data Types
6. Input and Output in Python 
7. Control Statements
8. Loops
9. Functions
10. Problems on Control Statements and Loops
11. Problems on Functions 
12. Assignments


# 1. What is Programming Language?

A prgramming language us a formal language that prvides instructions for a computers to execute. It's how humans communicate with computers to create software, applications, and other technology.


# 2. High Level Language Vs Low level Programming Language

**Low Level** : Machine only understand binary language / assembly language / low level language.  01010101

**High Level Language** Humans can understand like Python, C ++, Java


Computers can not undersatnd **high level language** so we need to convert high level language into **low level lanaguage** or binary language

# 3. Complier and Interoreter 

# Complier 

1. ## **Complier** converts whole code high level language  at a once into low level language.

2. **Errors at once**

3. Slow in analyze
4 . compiled code run fast

# Interpreter
1. ## **Interpreter** converts code line by line.
2. **Errors line by line**

3. Fast in Analyze 


# 4. Introduction to Python

**Python** is a versatile high-level, general-purpose programming language designed for readablity and ease of use.


1. Interpreted
2. High-Level
3. Object-oriented
4. Extensive libraries
5. Beginner-friendly

# 5.  Varibles/Keywords/Identifiers/Comments/


1. **Variables**

Container that store data in computer memory

**Keywords**
Predefined words that having any meaning in Programming Language
1. `while`
2. `def`
3. `for`
4. `if`

**Identifiers**
Name that we provide to variables/functions/class
1. variables names for declaring 
2. functions names
3. class names

**Comments**
you can use comments for understading the codes. its not executable code
1. Single line comments  # This is a single line comments
2. Multi-Line comments  ""This is multi line comments""

**Operators**

Arithemic Operators:
1. Addition `+`
2. Substraction -`
3. Division `/`
4. Mudulus `%`
5. Floor division `//`
6. Exponentiation `**`
7. Muliplication `*`

**Assignment Operators**

Used to assign values to variables.
1. `=` (Assign)
2. `+=` (add and assign)
3. `_=` (Subtract and assign)
4. `*=` (Multiply and assign)

**Comperison Operators**

1. `==` (Equal to)
2. `!=` (not equal to)
3. `">`(Greater than)
4. `>=` (Greater than or equal to)
5. `<=` (Less than or equal to)


**Logical Operators**
Used to combine to conditional statements.

1. `and` (Logical AND)
2. `or` (Logical OR)
3. `not` (Logical Not)


**Membership Operators**

Used to check if a value is a part of a sequence

1. `in` (Returns True if a value is found in the sequence)
2. `not in` (Returns True if a value is  not found in the sequence)



 **Input & Output Python**

 Take values from users through input functions
 ```python
   

  #  Input functions take user value 
   first_name = input("Enter your name")
   email = input("Enter your email")
   age = int(input("Enter your age"))
   height = float(input("Enter your height"))

  # Display user value
   print(f"My Name is {first_name}, email is {emai}, and I'm{age} years old, and total height is {height} ")

 ```

 **Control Satements**

 `if` and `else` statements  to control the flow


 ```python

 age = int(input("Enter your age"))

 if age >= 18:
  print("Englible for vote.)
else:
  print("Not eligible for vote)
 
 
 ```

 **Loops**
 - `for`

 - `while`

 ```python
 
 i = 0

 while i<5:
  print(i, end=" ")
  i+=1

list1 = [1, 2, 3, 4, 5]

for list in list1
  print(list)
 
 ```
# `Range function `

```python
for x in range(1,11):
  print(x, end=" ")

for x in range(1,11,2):
  print(x, end=" ")
  
for x in range(20,0,-1):
  print(x, end=" ")
```




