option = int(input("Choose an option:\n1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\n5. Average\nEnter your choice (1-5): "))

if option == 1:

    # Addition
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
elif option == 2:
    
    
    # Subtraction
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
elif option == 3:
    
    
    # Division
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 != 0:
        result = num1 / num2
    else:
        print("Cannot divide by zero.")
        exit()
elif option == 4:
    
    
    # Multiplication
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
elif option == 5:
    
    
    # Average
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    result = (first + second) / 2
else:
    print("Invalid option.")
    exit()


# Check if the result is negative
if result < 0:
    print("NEGATIVE")
    
print("Result:", result)
