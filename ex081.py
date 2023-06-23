r = 'S'
valores = []
print('=' * 80)
while r == 'S':
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    r = str(input('Quer continuar adicionando valores? [S/N] ')).upper().strip()
    print('=' * 80)
    if r == 'S':
        print('Ok. ', end = '')
    if r == 'N':
        print('=' * 80)
print(f'Foram adicionados {len(valores)} valores à lista.')
valores.sort(reverse=True)
print(f'A ordem decrescente da lista é {valores}.')
if 5 in valores:
    print('Foi digitado o valor 5.')
else:
    print('Não foi digitado o valor 5.')
