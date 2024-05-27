import random

pass_length=int(input("Enter the length of password:"))
s="abcdefgihjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*"
password="".join(random.sample(s,pass_length))

print(password)