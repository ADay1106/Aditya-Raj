def  calculate(num1,num2,operation):
    if operation=='1':
        return num1+num2
    elif operation=='2':
        return num1-num2
    elif operation=='3':
        return num1*num2
    elif operation=='4':
        if num2!=0:
            return num1/num2
        else:
            return "Error Division by zero"
    elif operation=='5':
        if num2!=0:
            return num1%num2
        else:
            return "Error Module by zero!"
    elif operation=='6':
        return num1**num2
    else:
        return "Invalid operation selected!"
try:
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
except ValueError:
    print("Error: Please enter valid numbers. ")
    exit()

print("\nSelect Operation: ")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division(/)")
print("5. Modulus(%)")
print("6. Exponentiation(^)")

operation=input("enyer your choice(1/2/3/4/5/6): ")

result=calculate(num1,num2,operation)
print(f"\nResult: {result}")