"""
Type Hinting 
    - What type of data type u eant the variable to be.

"""

def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")