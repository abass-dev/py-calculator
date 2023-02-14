
from termcolor import colored


def welcome():
    print('''\n
😊 Welcome to py-calculator 😊\n
      By Abass Dev With ❤
        ''')


def calculator():
    num1 = int(input(colored('First number ', 'green')))
    operator = input(colored('Select operator (+, -, *, / ) ', 'yellow'))
    num2_text = colored('Second number ', 'green')

    if operator == '+':
        num2 = int(input(num2_text))
        print('{}: {} + {} ='.format(colored('RESULT', 'red'), num1, num2), num1 + num2)

    elif operator == '-':
        num2 = int(input(num2_text))
        print('{}: {} - {} ='.format(colored('RESULT', 'red'), num1, num2), num1 - num2)

    elif operator == '*':
        num2 = int(input(num2_text))
        print('{}: {} * {} ='.format(colored('RESULT', 'red'), num1, num2), num1 * num2)

    elif operator == '/':
        num2 = int(input(num2_text))
        print('{}: {} / {} ='.format(colored('RESULT', 'red'), num1, num2), num1 / num2)

    else:
        print('Invalid operator')
    again()


def again():
    check_again = input('\nDo you want to continue? (Y/N)\n')
    if check_again == 'Y':
        calculator()
    else:
        print(colored('See you again 👋\n', 'green'))
        exit(1)


welcome()
calculator()
