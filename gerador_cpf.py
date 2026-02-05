# Bibliotecas
import random

# Cálculo CPF
# Seja um CPF 698.412.140-xy
# Dígito x:
# 1. Deve-se multiplicar os 9 primeiros dígitos por uma contagem regressiva que começa em 10
# 2. No exemplo acima: 6*10 9*9 8*8 4*7 1*6 2*5 1*4 4*3 0*2
# 3. Em seguida soma-se o resultado obtido no passo 2: 60 + 81 + 64 + 28 + 6 + 10 + 4 + 12 + 0 = 265
# 4. Multiplica-se o resultado do passo 3 por 10: 265*10 = 2650
# 5. Calcula-se o resto da divisão do resultado do passo 4 por 11: 2650 % 11 = 10
# 6. Se o resultado do passo 5 for maior que 9, x = 0
# 7. Se o resultado do passo 5 for menor ou igual a 9, x = resultado passo 5
# 8. No exemplo presente x = 0 porque o resultado do passo 5 foi igual a 10

# Dígito y:
# 1. Deve-se multiplicar os 10 primeiros dígitos por uma contagem regressiva que começa em 11
# 2. No exemplo acima: 6*11 9*10 8*9 4*8 1*7 2*6 1*5 4*4 0*3 0*2
# 3-7. Mesma lógica usada para calcular o dígito x

# Funções

# Função para calcular os dois últimos dígitos do cpf
def calcular_digito(cpf_limpo,num_digitos):
    if num_digitos == 9:
        i = 10
    elif num_digitos == 10:
        i = 11
    
    # Loop para calcular a soma das multiplicações
    soma_multiplicacoes = 0
    for valor in cpf_limpo:
        soma_multiplicacoes += int(valor)*i
        i -= 1
        if i < 2:
            break

    # Multiplicando o resultado anterior por 10
    soma_multiplicacoes_vezes10 = soma_multiplicacoes*10

    # Resto da divisão do resultado anterior por 11
    resto_divisao11 = soma_multiplicacoes_vezes10 % 11

    # Primeiro digito do cpf
    digito = 0 if resto_divisao11 > 9 else resto_divisao11

    return digito

# Início do software

# Variáveis
finalizar_programa = False

while(not finalizar_programa):
    
    cpf = ""

    # Gerando os 9 primeiros digitos do cpf
    for valor in range(9):

        n = random.randint(0,9)
        cpf += str(n)
        
    # Calculando os dois últimos dígitos do cpf
    primeiro_digito = calcular_digito(cpf,9)
    segundo_digito = calcular_digito(cpf,10)

    # Transformando de inteiro para string
    primeiro_digito = str(primeiro_digito)
    segundo_digito = str(segundo_digito)

    # CPF completo
    cpf += primeiro_digito + segundo_digito
    
    # Gerando a sequência de um número. Ex: 111111111
    cpf_nao_valido = cpf[0]*11

    # Verificando se o CPF é uma repetição do primeiro número
    if (cpf != cpf_nao_valido):

        # Imprimindo o CPF na tela
        print(f'CPF limpo: {cpf}')
        print(f'CPF formal: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9]}{cpf[10]}')
        finalizar_programa = True

    else:
        continue
