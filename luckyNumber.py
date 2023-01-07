import random
randNum=random.randint(1,10)

def lucky_number(name):
    number = len(name) * randNum
    message = "Hello " + name + ". Your lucky number is " + str(number)
    return message
    
print(lucky_number("Joaquin"))
print(lucky_number("Shania"))
print(lucky_number("Emily"))
