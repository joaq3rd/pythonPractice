#Return the Sum of all divisors of a number without the number itself. User provides value at the beginning of the program.
def sum_div(number):

  if number <= 1: #if statement ensures for loop works correctly
    return number
  
  divisor [1]
  for i in range (2,number):
    if(number % i == 0):
      divisor.append(i)
  return sum(divisor)

print("Your result is: ",sum_div(number = int(input("Enter the value: "))))
