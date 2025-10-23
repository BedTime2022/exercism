def square(number):
 value = 2 ** (number - 1)
 if number <= 64 and number >= 1: 
     return value
 else:
     raise ValueError("square must be between 1 and 64")
def total():
 return (2 ** 64) - 1
    
