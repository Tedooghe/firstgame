print('welcome to my first game!')
name = input('What is your name? ')
age = input('How old are you? ')

print('Hello,', name, '.  You are', age, 'years old.')

if age >= 18:
  print('You are old enough.')
  wantplay = input('Do you want to play? ')
  if wantplay == 'yes':
    print("let's play!")
else:
  print('Sorry, you are too young to play.')
