import random
import string

def generate_string(length=5):
    
  characters = string.ascii_letters + string.digits
  result = ''.join(random.choice(characters) for _ in range(length * 5))
  return ' '.join([result[i:i+length] for i in range(0, len(result), length)])

my_string = generate_string()
while 0 < 10:
    my_string = generate_string()
    wait = input(my_string)