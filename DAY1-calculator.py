print("A simple calculator")


while True:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))

    op=input("Enter operation (+, -, *, /): ")
    match op:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2   
        case '*':
            result = num1 * num2    
        case '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
    print(f"The result is: {result}")
    print("Do you want to perform another calculation? (yes/no)")
    cont = input().lower()
    if cont != 'yes':

        break
