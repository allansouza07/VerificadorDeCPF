"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""



"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)


##FUNÇÃO QUE DESCOBRE OS ÚLTIMOS 2 DÍGITOS DO CPF
def ultimos_dois ():
    cpf = None
    cpf_lista = []
    digito_um = 0
    print()
    print("------------DESCOBRIR OS 2 ÚLTIMOS DÍGITOS DO CPF --------------")
    print()

    while True:
        #COLETA DO CPF
        try: 
            cpf =(input("Digite aqui os 9 primeiros digitos do cpf")).replace(' ','').replace('-','').replace('.','')
            print()
        except ValueError:
            print("Digite número, não strings!")
        else:
            if len(cpf) != 9:
                print("Digite 9 números!")

                continue
            else:
                cpf_lista.append(cpf)
                break
    acumulador = 0
    indice=-1

    #MULTIPLICANDO OS DIGITOS DO CPF EM UMA SEQUÊNCIA DE 9 DIGITOS
    for c in range(10,1, -1):
        indice +=1
        acumulador = acumulador + c * int(cpf_lista[0][indice])

    #MULTIPLICANDO A SOMA DESSES NÚMEROS POR 10 E PEGANDO O RESTO DA DIVISÃO POR 11
    resto_divisao= (acumulador * 10) % 11

    if resto_divisao > 9:
        digito_um = 0
    else :
        digito_um = resto_divisao

    cpf_completo = (f"{cpf}-{digito_um}" )


    ##SEGUNDO DIGITO
    cpf_nmr = [str(cpf) + str(digito_um) ]
    segundo_digito = None

    indice_2 = -1
    acumulador_2 =0
    #MULTIPLICANDO OS DIGITOS DO CPF EM UMA SEQUÊNCIA DE 10 DIGITOS
    for c in range (11,1, -1):
        indice_2 +=1
        acumulador_2 = acumulador_2 + c * int(cpf_nmr[0][indice_2])
        
    #MULTIPLICANDO A SOMA DESSES NÚMEROS POR 10 E PEGANDO O RESTO DA DIVISÃO POR 11
    resto_divisao_2 = (acumulador_2 * 10) % 11

    if resto_divisao_2 > 9:
        segundo_digito = 0
    else :
        segundo_digito= resto_divisao_2

    cpf_completo = (f"{cpf}-{digito_um}{segundo_digito}" )
    print(f"Seu cpf completo: {cpf_completo}")

def validador():
    cpf = None
    cpf_lista = []
    digito_um = 0
    print()
    print("---------- VALIDADOR DE CPF -----------")
    print()
    while True:
        try:
            cpf =(input("Digite aqui o cpf"))
        except ValueError:
            print("Digite número, não strings!")
        else:
            cpf_formatado = cpf.replace(' ','').replace('-','').replace('.','')
            if len(cpf_formatado) != 11:
                print("Digite 11 números!")

                continue
            else:
                cpf_lista.append(cpf_formatado)
                break
    acumulador = 0
    indice=-1
    #MULTIPLICANDO OS DIGITOS DO CPF EM UMA SEQUÊNCIA DE 10 DIGITOS
    for c in range(10,1, -1):
        indice +=1
        acumulador = acumulador + c * int(cpf_lista[0][indice])
    
    #MULTIPLICANDO A SOMA DESSES NÚMEROS POR 10 E PEGANDO O RESTO DA DIVISÃO POR 11
    resto_divisao= (acumulador * 10) % 11

    if resto_divisao > 9:
        digito_um = 0
    else :
        digito_um = resto_divisao

    cpf_completo = (f"{cpf_formatado[:9]}-{digito_um}" )


    ##SEGUNDO DIGITO
    cpf_nmr = [str(cpf_formatado[:9]) + str(digito_um) ]
    segundo_digito = None

    indice_2 = -1
    acumulador_2 =0
    #MULTIPLICANDO OS DIGITOS DO CPF EM UMA SEQUÊNCIA DE 10 DIGITOS
    for c in range (11,1, -1):
        indice_2 +=1
        acumulador_2 = acumulador_2 + c * int(cpf_nmr[0][indice_2])
        
    #MULTIPLICANDO A SOMA DESSES NÚMEROS POR 10 E PEGANDO O RESTO DA DIVISÃO POR 11
    resto_divisao_2 = (acumulador_2 * 10) % 11

    if resto_divisao_2 > 9:
        segundo_digito = 0
    else :
        segundo_digito= resto_divisao_2

    cpf_completo = (f"{cpf_formatado[:9]}{digito_um}{segundo_digito}" )

    #COMPARANDO O CPF DIGITADO PELO USUÁRIO COM O CPF CALCULADO PELO ALGORÍTIMO
    if cpf_formatado == cpf_completo:
        print()
        print(f"O CPF {cpf} é válido!")
    else:
        print()
        print(f"O CPF {cpf} é inválido!")
   

print("Escolha o que você deseja fazer:")
while True:
    try:
        escolha = int(input("[1] Descobrir os dois últimos dígitos do cpf \n [2] Descobrir se tal CPF é válido [3] Gerar um CPF aleatório"))
    except ValueError:
        print("Digite um número!")
        continue
    else:
        if escolha > 3 or escolha <1:
            print("Digite um valor entre 1 e 3!")
            continue
        break
if escolha == 1:
    ultimos_dois()
if escolha == 2:
    validador()

