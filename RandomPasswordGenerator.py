import random
alphabets= "abcdefghijklmnopqrstuvwxyz"
numbers="1234567890"
special="!@#$%&*"
a=int(input("Enter the Number of Alphabets:"))
n=int(input("Enter the Number of Digits:"))
s=int(input("Enter the Number of Symbols:"))
password = ''
for _ in range(a):
    password += random.choice(alphabets)
for _ in range(n):
    password += random.choice(numbers)
for _ in range(s):
    password += random.choice(special)
password=''.join(random.sample(password,len(password)))
print("----------------------------------------------")
print("Generated Password:",password)
print("----------------------------------------------")
