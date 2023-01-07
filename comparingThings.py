print(10>1) #True
print("cat" == "dog") #False
print(1 != 2) #True
print(1 < "1") #TypeError because integer and strings
print(1 == "1") #False

print("Yellow" > "Cyan" and "Brown" > "Magenta") #False
print(25 > 50 or 1 != 2) #True
print(not 42 == "Answer") #True


#When a return statement is executed, the function exits, so that the code that follows doesn't get executed.
def is_even(number):
  if number % 2 == 0
    return True
  return False
