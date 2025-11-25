#Sujita Moktan

while True:
    try:
      first_num = int(input("Enter the first number::"))
      op = input("Enter the mathematical operation(+,-,*,/,**,%)::")
      second_num =int(input("Enter second number::"))
    except ValueError:
     print("Invalid input. Please enter a number!")
     continue
    
    else:
    #switch case
     match op:
      case '+':
       print(f"Sum:  {first_num + second_num}")     #using formatted string literal to concatenate the results
      case '-':
       print(f"Difference: {first_num-second_num}")
      case '*':
        print(f"Multiplication: {first_num*second_num}")
      case '/':
        if second_num == 0:
          raise ZeroDivisionError("Error: Cannot divide by zero.")
        print(f"Division: {first_num/second_num}")
      case '**':
         print(f"Exponent of first_num: {first_num*first_num}")
         print(f"Exponent of second_num: {second_num*second_num}")
      case '%':
         print(f"Modulus: {first_num % second_num}")
    
      case _:                      #if no match is found, execute the following code   
         print("Please enter valid operation number")

     again = input("Still want to perform calculations?[y/n/exit]:").lower()
     if again in['no', 'exit']:
       break

  