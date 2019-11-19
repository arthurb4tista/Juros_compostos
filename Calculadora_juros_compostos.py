#calculadora de juros compostos
print ('Em quantos anos voce quer se aposentar?')
anos = int(input('Anos: '))
print (' ')
print('Quanto dinheiro voce tem disponivel em sua conta?')
disponivel = float(input('Insira o valor atual em sua conta: '))
print (' ')
print('Quanto voce ira investir mensalmente ?')
invmen = float(input('Insira o valor mensal a investir: '))
print (' ')
print('Quanto voce estima desse investimento?')
anualmente = float(input('Insira em um numero decimal(10% = 0.1): '))

print (' ')

invmen = invmen * 12
total_acumu = 0

for i in range(0, anos):
    if total_acumu == 0:
        total_acumu = disponivel
    
    total_acumu = (total_acumu + invmen) * (1 + anualmente)

print('Valor que estara em sua conta depois de {} anos: '.format(anos) + str(total_acumu))