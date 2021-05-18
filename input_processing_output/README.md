# Input, Processing, and Output

1.  [Displaying output to the user](#displaying-output-to-the-user)
1.  [Getting input from the user](#getting-input-from-the-user)
1.  [Using variables](using-variables)
1.  [Basic mathematical operations](#basic-mathematical-operations)
1.  [Basic string operations](#basic-string-operations)

## Comments in your code
```
# here is a python comment
print("Any line that starts with a hash is a comment in python")
```

## Displaying output to the user
```
print("My String")
# My String

print("My", "String")
# My String
```

## Getting input from the user
```
inputString = input("Input a value: ")
print("You entered: ", inputString)
```

## Using variables
```
x="Here is a string"
x=str("Here is a string")

x=1
x=int(1)

x=["item 1", "item 2", "item 3"]
```

## Basic mathematical operations
```
#addition
x = 1 + 1 
print(x) #--> 2

#subtraction
x = 1 - 1
print(x) #--> 0

#division
x = 1 / 2
print(x) #--> 0.5

#multiplication
x = 2 * 2
print(x) #--> 4

#modular division (result is the remainder)
x = 1 % 2 
print(x) #--> 1

x = 1 % 3 
print(x) #--> 2

#exponentiation: x ** y where y is the power
x = 2 ** 2 
print(x) #--> 4

#floor division: truncate the remainder
x = 1 // 3
print(x) #--> 0

x = 3 // 2 
print(x) #--> 1

```

## Basic string operations
```
x = "Here is a string"

x = """ Here is 
a multiline 
string
"""

# strings are arrays, so x[1] would give the character in the string, at position 1
x = "My String"
print(x[0]) #--> M
print(x[1]) #--> y

# length of string
stringLength = len("My String")
print(stringLength)

# check if a substring exists in a string
x = "My String"
test = "My" in x
print(test) # --> true
test = "Some" in x
print(test) # --> false

# check if a substring does not exist in a string
x = "My String"
test = "My" not in x
print(test) # --> false
test = "Some" not in x
print(test) # --> true

# template
x = "hello {name}"
print(x.format(name="John"))

```

