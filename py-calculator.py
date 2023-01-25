def welcome():
    print('''\n
              ___😊 Welcome to py-calculator 😊___\n
                      By Abass Dev With ❤
        ''')

def calculator():
    num1 = int(input('First number '))
    operation = input('Select operation (+, -, *, % ) ')

    if operation == '+':
        num2 = int(input('Second number '))
        print('{} + {} ='.format(num1, num2), num1 + num2)

    elif operation == '-':
          num2 = int(input('Second number '))
          print('{} - {} ='.format(num1, num2), num1 - num2)
    
    elif operation == '*':
          num2 = int(input('Second number '))
          print('{} * {} ='.format(num1, num2), num1 * num2)

    elif operation == '*':
          num2 = int(input('Second number '))
          print('{} % {} ='.format(num1, num2), num1 % num2)

    else:
        print('Invalid operation')
    again()

def again():
    checkAgain = input('Do you want to continue? (Y/N)')
    if checkAgain == 'Y':
        calculator()
    else:
        print('See you again.')

welcome()
calculator()
