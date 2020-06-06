import re

# string = 'Search this inside of this text please!'

# pattern = re.compile('this')

# result = re.search('this', string)
# result = pattern.search(string)
# result = pattern.findall(string)
# result = pattern.fullmatch(string)
# result = pattern.match(string)

# print(result.span())
# print(result.start())
# print(result)

password = 'hoadahqehqh8%'
pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
check = pattern.fullmatch(password)
print(check)

# At least 8 characters long 
# contains any letter, digits and $%#@
# has to end with a number 