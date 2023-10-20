from art import logo


# Add
def add(num1, num2):
    return (num1 + num2)

# Subtract
def subtract(num1, num2):
  return num1 - num2

# Multiply
def multiply(num1, num2):
  return num1 * num2

# Division
def divide(num1, num2):
  return num1 / num2


print(logo)

operation = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide 
}


num1 = float(input("What's the first number?: "))

for symbol in operation:
  print(symbol)

num2 = float(input("What's the next number?: "))
operation_symbol = input("Pick an operation from the line above: ")
  
user_symbol = operation[operation_symbol]
answer = user_symbol(num1, num2)
  
print(f"{num1} {operation_symbol} {num2} = {answer}")

again = True
while again:
  
  if input(f"Type 'y' to continue calculating {answer}, or type 'n' to exit: ").lower() == "y" :
    operation_symbol = input("Pick an operation: ")
    num2 = int(input("What's the next number?: "))
    answer = user_symbol(answer, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  else:
    again = False