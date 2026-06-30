'''
4. Explain why strings are immutable in Python.
What happens internally when you modify a string variable
'''

str = "pratik"
str1 = "pratik"

message = "hello"
print(message)
message = message + " world"
print(message)


print(type(str))
print(id(str))
print(len(str))

print(type(str1))
print(id(str1))

