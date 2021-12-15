from random import randint
from time import sleep

# Fazer o computador pensar
pc = randint(0, 5)
print('Vou pensar em um numero 0 e 5. Tente advinhar')
# jogar tente advinhar
eu = int(input('Em que numero eu pensei? '))

print('processando...')
sleep(2)
if eu == pc:
    print('PAREBÉNS! Você acertou.')
else:
    print(f'ERROU! Peseni no numero {pc}')
        
