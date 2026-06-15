''''2. What is the difference between:
a = 10
b = 10
and
a = [10]
b = [10]
Explain using id().'''

a = 10
b = 10

print(type(a))          #class <'int'>  id = 0x100
print(type(b))          #class <'int'>  id = 0x100
print(id(a))
print(id(b))

a = [10]
b = [10]

print(type(a))          #class <'list'>  id = 0x200     mutable
print(type(b))          #class <'list'>  id = 0x300     mutable
print(id(a))    
print(id(b))

#need to study 