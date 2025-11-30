a = 15
b = 25
c = 30

if (b<a>c):
  print('a is the greatest number')
elif (a<b>c):
  print('b is the greatest number')
else:
  print('c is the greatest number')


# nested if-else statements
if (a>b):
  if (a>c):
    print('a is the greatest number')
  else:
    print('c is the greatest number')
else:
  if (b>c):
    print('b is the greatest number')
  else:
    print('c is the greatest number') 