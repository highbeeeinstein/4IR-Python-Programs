import re

txt = input('Enter your email address ')
x = re.search("^@*.com$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")




print(re.findall('ab', 'abacadraba'))

print(re.match('@', 'wahab@'))

print(re.sub('old', 'new', 'old baby sitting on a old couch'))

print(re.split(''))