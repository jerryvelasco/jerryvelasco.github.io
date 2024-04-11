#addition function
def add(n1, n2):
  return n1 + n2

#subtract function 
def subtract(n1, n2):
  return n1 - n2

#multiply function 
def multiply(n1, n2):
  return n1 * n2

#divide function 
def divide(n1, n2):
 return n1 / n2

"""
create a dictionary with the operation symbols as the key and their respective names as the value
"""
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

from art import logo

def calculator():
  
  print(logo)
  num1 = float(input("whats the first number?: "))

  #loops through the dictionary and prints out the symbos(keys)
  for symbol in operations:
    print(symbol)
  
  continue_calculation = True 

  #checks if the user wants to continue current calculations 
  while continue_calculation:
    
    operation_symbol = input("Pick another operation: ")
    
    num2 = float(input("whats the next number?: "))

    #based on the symbol input from the user, grabs the value from the operations dictionary 
    #using the key, and assigns that value to calculation function
    calculation_function = operations[operation_symbol]

    #uses the predefined functions add, subtract to do the calculations on the 2 num inputs 
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    choice = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation.: ")

    #assigns num1 with the answer to allow calcultion to continue with the previous answer
    if choice == 'y':
      num1 = answer

    #if the user doesnt want to continue the calculation continue calculation turns false breaking while loop 
    else: 
        continue_calculation = False

        #using recurssion we call the calculator function allowing us to start the function from the beginning 
        calculator()


calculator()
