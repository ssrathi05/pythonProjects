#collect user prefersnses
# - length
# - should contain uppercase
# - should contain digits

#create all availible characters
#randomly pick c hars up to the length
#ensure we have at lease on of each character type
#ensure length is valid

import random
import string

def generate_password():
  length = int(input("Enter the desired password length: ").strip())
  include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
  include_special = input("Include special characters letters? (yes/no): ").strip().lower()
  include_digits = input("Include digits letters? (yes/no): ").strip().lower()

  if length < 4:
    print("Password length must be at least 4 characters.")
    return
  
  lower = string.ascii_lowercase
  uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
  special = string.punctuation if include_special == "yes" else ""
  digits = string.digits if include_digits == "yes" else ""

  all_characters = lower + uppercase + special + digits

  required_characters = []
  if include_uppercase == "yes":
    required_characters.append(random.choice(uppercase))
  if include_digits == "yes":
    required_characters.append(random.choice(digits))
  if include_special == "yes":
    required_characters.append(random.choice(special))

  remaining_length = length - len(required_characters)
  password = required_characters

  for _ in range(remaining_length):
    password.append(random.choice(all_characters))
  
  random.shuffle(password)
  

  str_password = "".join(password)
  return str_password
  


password = generate_password()
print(password)