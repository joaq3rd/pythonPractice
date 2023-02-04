def replace_ending(sentence, old, new):
  if sentence.endswith(old):
    i = sentence.rfind(old)
    new_sentence = sentence[:i]+new
    return new_sentence
  
  return sentence

print(replace_ending("I don't know you,", "you", ", let's find out together!")
      #Should display "I don't know, let's find out together!"
