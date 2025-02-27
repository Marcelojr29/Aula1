# idade = 15

# if idade >= 18:
#     print("Você é maior de idade")
# elif idade >= 16:
#     print("Você pode votar, mas não pode dirigir")
# else:
#     print("Você é menor de idade")

# for, while, break, continue

# for i in range(5): # vai de 0 a 4
#     print(f"Iteração {i}")

# contador = 1
# while contador <= 5:
#     print(f"Contador {contador}")
#     contador += 1

# for i in range(1, 10):
#     if i == 9:
#         break # Para o loop quando i for 5
#     print(i)
    
# print(f"Loop interrompido no {i}")

# for i in range(1, 10):
#     if i == 5:
#         continue # Pula a iteração quando i for 5
#     print(i)
# print(f"Loop com continue {i}")

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")