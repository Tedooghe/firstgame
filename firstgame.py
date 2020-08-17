print('welcome to my first game!')
name = input('What is your name? ')
age = input('How old are you? ')

print('Hello,', name, '.  You are', age, 'years old.')

if age >= 18:
  print('You are old enough.')
  wantplay = input('Do you want to play? ').lower()
  if wantplay == 'no':
    print('Fine, whatever!')
  else:
    print("let's play!")
    Log_or_Int = print('Which makes the best choices, A-Logic or B-Intuition (A/B)? ').upper()
    if Log_or_Int == 'A':
      print('Cognition researchers have named over 350 different ways that all humans make choices based on bias, heuristics, and fallacy instead of logic.')
      Human_or_not = input('Are you a Human (yes/no)? ').upper()
      if Human_or_not == 'YES':
        print('How can you know that your preference of logic over intuition is not based on one or more of these cognitive errors?')
        exception = input('Are you an exceptionally logical person (yes/no)? ').upper()
        if exception == 'YES':
          print('Look up "the exceptionalist fallacy"')
        else:
          print("Neither am I.")
      else:
        print('This game is not for you!')


    else:
      print('Every tyrant intuitively believes that they are destined to rule and will do whatever it takes to achieve this including slaughter and slavery. God has told them to trust themself.')
      destiny = input('Are they right (yes/no)? ')  .upper()
      if destiny == 'YES':
        print('I intuitively decide that I should hunt you down and kill you.')
      else:
        print('Intuition is completely subjective and common-sense is an application of culturally normal bias. Rationalization seems like logic when "A man hears what he wants to hear and disreguards the rest"')
else:
  print('Sorry, you are too young to play.')
