

name = "talha Rana" # string value
age = 33            # int number value
heighht = 5.6       # float number value


print(name, age, heighht)


# Taking value from users with input function
user_name = input("Enter your name ")


# Display value result with output function
print(f"My name is {user_name}")


 Input functions take user value 
first_name = input("Enter your name")
email = input("Enter your email")
age = int(input("Enter your age"))
height = float(input("Enter your height"))

Display user value
print(f"My Name is {first_name}, email is {email}, and I'm {age} years old, and total height is {height} ")


num1 = int(input("Enter num 1 :"))
num2 = int(input("Enter num  2 :"))


print(f"\nTotal sum of {num1} and {num2} is = {num1 + num2}")
print(f"\nTotal sum of {num1} and {num2} is = {num1 - num2}")
print(f"\nTotal sum of {num1} and {num2} is = {num1 / num2}")
print(f"\nTotal sum of {num1} and {num2} is = {num1 % num2}")
print(f"\nTotal sum of {num1} and {num2} is = {num1 * num2}")
print(f"\nTotal sum of {num1} and {num2} is = {num1 ** num2}")


Simple function
def welcome():
  print("Welcome to DSA in Python 2025")
  
welcome()

Simple function with return
def welcome():
  return f"Welcome to DSA in Python 2025"
  
functiona_store = welcome()
print(functiona_store)


def sum(a, b):
  sum = a + b
  return sum

result = sum(10, 20)
print(result)



age = 20

age = int(input("Enter your age : "))

if age >= 18:
  print("eligible for vote")
else:
  print("Not eligible for vote")

i = 1
table = 2

while i<=10:
  # print(i, end=" ")
  print(f"{table} x {i} = {table*i}")
  i+=1


for x in range(1, 11):
  print(x)


for x in range(1,11):
  print(x, end=" ")

for x in range(1,11,2):
  print(x, end=" ")

for x in range(20,0,-1):
  print(x, end=" ")
