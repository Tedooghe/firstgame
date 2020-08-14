print('welcome to my first game!')
name = input('What is your name? ')
age = input('How old are you? ')

print('Hello,', name, '.  You are', age, 'years old.')

if age >= 18:
  print('You are old enough.')
  wantplay = input('Do you want to play? ').lower()
  if wantplay == 'yes':
    print("let's play!")
    Log_or_Int = print('Which makes the best choices, A-Logic or B-Intuition (A/B)? ').upper()
    if Log_or_Int == 'A':
      print('"Argument from Ignorance" is a classic fallacy -google it- It is illogical to make choices based on God, or any other unsupportable idea.    ?')

    if Log_or_Int == 'B':
      Print('If your were ')
else:
  print('Sorry, you are too young to play.')
