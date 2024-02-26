import random
import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# print(random.choice("hello"))



# val= random.choice(['a','b','c','d'])
# print(val)

pass_len=14
charvalues = string.ascii_letters + string.digits + string.punctuation


# list comprehension [function for i in range(n)]
password ="".join([random.choice(charvalues) for i in range(pass_len)])


# password=""
# for i in range(pass_len):
#     password += (random.choice(charvalues))

print("Your Random Password is: ",password)