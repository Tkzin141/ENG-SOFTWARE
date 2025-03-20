num = int(input('Digite aqui uma nota de 0 a 10:'))
while num < 0 or num > 10:
    print('Nota Incorreta')
    num = int(input('Digite aqui uma nota de 0 a 10:'))
print(f'Nota valida:{num}')

