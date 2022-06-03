import array
a1 = []
a1.append(int(input('Digite um valor: ')))
a1.append(int(input('Digite um valor: ')))
a1.append(int(input('Digite um valor: ')))
a1.append(int(input('Digite um valor: ')))
print(a1)

a2 = []
a2.append(int(input('Digite um valor: ')))
a2.append(int(input('Digite um valor: ')))
a2.append(int(input('Digite um valor: ')))
a2.append(int(input('Digite um valor: ')))
print(a2)

soma = [a1 + a2 for a1, a2 in zip(a1, a2)]
print(soma)