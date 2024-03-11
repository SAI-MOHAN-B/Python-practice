our_strings = "hello world"
print(our_strings*3)

# Slicing
print(our_strings[7:9])
# reversing the strings
print(our_strings[:-2])
print(our_strings.upper())
print(our_strings.lower())
print(our_strings.endswith("Hello"))
print(our_strings.startswith("hello"))

# formatting the strings
name = "guvi"
age = "geek iitm researchh park"
print("Hello {} i'm from {}".format(name,age))
print(f"hello i'm {name} and my {age} is 40")
