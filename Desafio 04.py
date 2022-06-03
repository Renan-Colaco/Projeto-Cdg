import sys
av1 = float(input('Digite sua nota: '))
av2 = float(input('Digite sua outra nota: '))
resultado = (av1 + av2)/2
if resultado >= 8:
        print ('Parabéns! Você passou de ano.')
        sys.exit(0)        
elif resultado < 4:
        print ('Você foi reprovado!')
        sys.exit(0)
else:
        print ('Você vai precisar da prova final ')
af = float(input('Digite a nota da sua prova final: '))
nf = (av1 + av2 + af)/3
if nf >=5:
        print('Parabéns! Você passou de ano.')
else:
        print('Você foi reprovado!')                        