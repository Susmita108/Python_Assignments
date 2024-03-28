'''
1- write a program which takes 2 inputs from the user : weight(kg) and height(meter) and prints the
BMI in the output.
BMI = weight / (square of height)
'''

# weight = int(input("enter your age in kg: "))
# height = float(input("Enter your height in meter: "))
# BMI = weight/(height * height)
# print(f"your BMI: {BMI}")

'''
2- write a program which takes the name of the user as input and replace all the occurence of character 'a'
in the name to 'b' and print it.

'''
# name = input("Enter your name:")
# result = name.lower().replace('a','b')
# print(f"final name is :{result}")
    
'''
3- write a program which takes 2 inputs from user as principle amount (int) and rate of annual interest
(float) and print the expected total amount  after  2 years.
example : principle : 100 , interest percent 10  then amount after 2 years will be : 100*1.1*1.1 = 121

'''
# principal = int(input("Enter the principal amount: "))
# interest_rate = float(input("Enter the annual interest rate: "))

# total_amount = principal * (1 + (interest_rate / 100)) ** 2

# print("Expected total amount after 2 years:", total_amount)

'''
4- write a program which takes city name from user input. irrespective of in which case user enters the
city name, print the city name in camel case meaning first letter should be capital and rest in small.
example : input : MYSORE ,  print - > Mysore
'''
# c = input("City Name: ")
# d = c.lower().capitalize()
# print(f"Camel case of {c} is {d}")

'''
5- write a program which takes the name of the user as input and print the index of character
'a' in the string. if 'a' is not there then return -1.
'''
# name = input("Enter your name: ")
# c = name.find('a')
# if c >= 0:
#     c1 = name.index('a')
#     print(f"index of character 'a' in the {name} is {c1}")
# else:
#     print("-1")
    
'''
6-  Display the number of letters in the below string
my_word = "antidisestablishmentarianism"
'''
# my_word = "antidisestablishmentarianism"
# t = len(my_word)
# print(f"length of given word is {t}")

'''
7- take 3 inputs from user : first name , last name and age .Display the information in below format 
exmaple -->
first name : MOhit
last name : sharma 
age 32
Display : my name is Mohit Sharma and I am 32 years old.
'''
# f = input("first name: ").capitalize()
# l = input("last name: ").capitalize()
# a = int(input("age "))
# print(f"my name is {f} {l} and I am {a} years old.")

'''
8-take 3 inputs from user : first name , last name and company name. create the email alias for the user 
and display it.  Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
example 
first name : MOhit
last name : sharma 
company : infosys
Display : morma@infosys.com 
'''
# f = input("Enter your first name: ").lower()
# l = input("Enter your last name: ").lower()
# c = input("Enter your company name: ").lower()
# f1 = f[:2]
# l1 = l[-3:]
# print(f"{f1}{l1}@{c}.com")


