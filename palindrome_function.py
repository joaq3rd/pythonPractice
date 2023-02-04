def is_palindrome(input_string):
  new_string = ""
  reverse_string = ""
  
  for string in input_string.lower():
    if string.replace(" ", ""):
      new_string = string + new_string
      reverse_string = string + reverse_string
    
  if new_string[::-1]==reverse_string:
    return True
  return False
  
print(is_palindrome("Bob")
print(is_palindrome("dog go d")
print(is_palindrome("Hello lle h")
print(is_palindrome("This is not True")
print(is_palindrome("Bob")
