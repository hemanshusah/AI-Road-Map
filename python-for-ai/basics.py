from _typeshed import importlib
name = "Himanshu"

name.upper()

age = 30

name = "ayush"

age = 18


# we can use if else loop for this

"""
This is a multi line comment

"""


if age >= 18:
    print ("you are eligible for voting")
else:
    print("you are not eligible for voting")


print(5+5)

power = 10**2
print(power)

print(100**4)

multi_line = """
    This is a multi line 
    This is the second Line
    """
print(multi_line)


first_name = "Himanshu"
last_name = "Sah"


full_name = first_name + " " + last_name
print(full_name)


len(full_name)
len(first_name)

logged_on = False


if logged_on:
    print("You are logged in")
else:
    print("You are logged out")
    

#dictionary practice    


human = {
    "name": "Himanshu",
    "age": 25,
    "city": "Delhi",
    "isStudent": False,
    
}

human["name"]

human["name"] = "Ayush"

print(human["name"])

del human["isStudent"]

print(human["name"])

print(human.items())
print(human.values())
print(human.keys())


print(human["age"])
print(human["city"])
print(human["isStudent"])



#Tuples
