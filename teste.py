

def validador():
    cpf = None
    cpf_lista = []
    digito_um = 0


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
    for c in range(10,1, -1):
        indice +=1
        print(f"{c} x {cpf_lista[0][indice]} = {c * int(cpf_lista[0][indice])}")
        acumulador = acumulador + c * int(cpf_lista[0][indice])


    print(f"soma: {acumulador}")

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
    for c in range (11,1, -1):
        indice_2 +=1
        print(f"{c} x {str(cpf_nmr[0][indice_2])} = {c * int(cpf_nmr[0][indice_2])}")
        acumulador_2 = acumulador_2 + c * int(cpf_nmr[0][indice_2])
        
    resto_divisao_2 = (acumulador_2 * 10) % 11

    if resto_divisao_2 > 9:
        segundo_digito = 0
    else :
        segundo_digito= resto_divisao_2

    cpf_completo = (f"{cpf_formatado[:9]}-{digito_um}{segundo_digito}" )
    print(f"Seu cpf completo: {cpf_completo}")

validador()
