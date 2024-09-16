number1 = int(input("digite o numero 1: "))
number2 = int(input("Digite o numero 2: "))

if number1 > number2:
  print(f"O numero {number1} é maior que o {number2}")
elif number1 < number2:
  print(f"O numero {number2} é maior que o {number1}")
elif number1 == number2:
  print(f"O numero {number2} é igual ao {number1}")
else:
  print("Erro")