import random
randNum=random.randint(1,10)

def lucky_number(name):
    number = len(name) * randNum
    print("Hello " + name + ". Your lucky number is " + str(number))
    
lucky_number("Joaquin")
lucky_number("Shania")
lucky_number("Emily")
