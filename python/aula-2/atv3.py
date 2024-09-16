age = int(input("Digite a sua idade: "))
cnh = input("Você tem CNH? ").lower()

if age > 18 and cnh == "sim":
  print("Voce pode dirigir")
else:
  print("voce não pode dirigir")