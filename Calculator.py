 # Function to perform the calculation
def calculator():
    print("Simple Calculator")
    print("Select Operation:")
    print("1. Addition + ")
    print("2. Subtraction  - ")
    print("3. Multiplication  * ")
    print("4. Division / ")

num1=int(input("enter the value1 : "))
num2=int(input("Enter the Value2 : "))
opr=input("Enter the operations..(+,_,*,/)")

if opr=="+":
    print(num1 + num2)
elif opr=="-":
    print(num1 - num2)
elif opr=="*":
    print(num1 * num2)
elif opr=="/":
    print(num1 / num2)
else:
    print("invalid opr...")

