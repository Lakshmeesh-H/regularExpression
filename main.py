import re

string = 'Search this inside of this text please!'

pattern = re.compile('this')

# result = re.search('this', string)
# result = pattern.search(string)
# result = pattern.findall(string)
# result = pattern.fullmatch(string)
result = pattern.match(string)

# print(result.span())
# print(result.start())
print(result)