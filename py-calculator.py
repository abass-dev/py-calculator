def welcome():
    print('''\n
              ___😊 Welcome to py-calculator 😊___\n
                      By Abass Dev With ❤
        ''')

def calculator():
    num1 = int(input('First number '))
    operator = input('Select operator (+, -, *, % ) ')

    if operator == '+':
        num2 = int(input('Second number '))
        print('{} + {} ='.format(num1, num2), num1 + num2)

    elif operator == '-':
          num2 = int(input('Second number '))
          print('{} - {} ='.format(num1, num2), num1 - num2)
    
    elif operator == '*':
          num2 = int(input('Second number '))
          print('{} * {} ='.format(num1, num2), num1 * num2)

    elif operator == '*':
          num2 = int(input('Second number '))
          print('{} % {} ='.format(num1, num2), num1 % num2)

    else:
        print('Invalid operator')
    again()

def again():
    checkAgain = input('Do you want to continue? (Y/N)')
    if checkAgain == 'Y':
        calculator()
    else:
        print('See you again.')

welcome()
calculator()
