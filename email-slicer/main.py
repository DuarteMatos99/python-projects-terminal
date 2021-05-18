import re
import sys


email = input('Type an email to give you details. ')
valid_email = bool(re.search("\w+@\w+\.[a-z]{2,4}$", email))

if not valid_email:
    print("You typed a wrong email. D:")
    sys.exit()

username = re.findall('(\w+)@', email)[0]
provider = re.findall('@(\w+)\.', email)[0]
domain = re.findall("@\w+\.(\w+)", email)[0]

print(f"\n[*] Info [*]\n"
      f"Username: {username}\n"
      f"Provider: {provider}\n"
      f"Domain: {domain}")