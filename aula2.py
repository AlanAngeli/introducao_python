a = int(input("Digite um valor: "))
b = int(input("Digite um segundo valor: "))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print("valores:", a,"e", b)
print("soma:", soma)
print()
print("subtração:",subtracao)
print()
print("multiplicação:",multiplicacao)
print()
print("divisão:",int(divisao))
print()
print("resto:",resto)
print()
x = "1"
x = int(x)
soma2 = x + 1
print(soma2)
print()
print('Soma: {} Subtração: {}'.format(soma, subtracao))
#ou:

print(f'Soma: {soma} Subtração: {subtracao}'.format(soma=soma, subtracao=subtracao))
print()
#ou:

print(f'Soma: {soma} '
      f'\nSubtração: {subtracao}'
      f'\nDivisão: {int(divisao)}'
      f'\nMultiplicação: {multiplicacao}'
      f'\nResto:{resto}'.format(soma=soma,
                                subtracao=subtracao,
                                divisao=divisao,
                                multiplicacao=multiplicacao,
                                resto=resto)) #\n pra pular linha
print()