from termcolor import colored
import os

def welcome():
    print('''\n
😊 Welcome to py-calculator 😊\n
      By Abass Dev With ❤
        ''')
         
def calculator():
    num1 = int(input(colored('First number ','green')))
    operator = input(colored('Select operator (+, -, *, / ) ','yellow'))
    num2Text = colored('Second number ','green')
    
    if operator == '+':
        num2 = int(input(num2Text))
        print('{}: {} + {} ='.format(colored('RESULT', 'red'), num1, num2), num1 + num2)

    elif operator == '-':
          num2 = int(input(num2Text))
          print('{}: {} - {} ='.format(colored('RESULT', 'red'), num1, num2), num1 - num2)
    
    elif operator == '*':
          num2 = int(input(num2Text))
          print('{}: {} * {} ='.format(colored('RESULT', 'red'), num1, num2), num1 * num2)

    elif operator == '/':
          num2 = int(input(num2Text))
          print('{}: {} / {} ='.format(colored('RESULT', 'red'), num1, num2), num1 / num2)

    else:
        print('Invalid operator')
    again()

def again():
    checkAgain = input('\nDo you want to continue? (Y/N)\n')
    if checkAgain == 'Y':
        calculator()
    else:
        print(colored('See you again 👋\n', 'green'))
        os._exit(1)
        
welcome()
calculator()
