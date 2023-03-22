num = int(input("Quantos numeros voce vai digitar? "))
vet = [0 for x in range(num)]
soma = 0


for i in range (0, num):
    vet[i] = float(input("Digite um numero: "))
    soma = soma + vet[i]
    media = soma / num

print()
for i in range (0, num):
    print(vet[i])


print("SOMA = ", soma)
print("MEDIA = ", media)