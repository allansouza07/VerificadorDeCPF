# SOBRE 

## Este projeto foi desenvolvido em Python com o objetivo de aplicar conceitos de lógica de programação, estruturas de repetição, funções, tratamento de exceções e manipulação de strings.

 O sistema trabalha com CPF e faz 3 coisas: 

- Descobre os 2 últimos dígitos do CPF
- Verifica se o CPF digitado pelo usuário é válido
- Gera uma quantidada (escolhida pelo usuário) de CPFs válidos

### Observação: O programa valida a estrutura matemática do CPF, mas não confirma a quem ele pertence. 

# TECNOLOGIAS UTILIZADAS

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

BIBLIOTECA "RANDOM"

<HR>

# ALGORÍTIMO DO SISTEMA

<h4> O programa utiliza o seguinte algorítimo matemático para descobrir os dois últimos números do CPF: 

<h4> exemplo de CPF: 746.824.890-70
  
<h4> O algorítimo coleta a soma dos 9 primeiros dígitos do CPF,
multiplicando cada um dos valores por uma
contagem regressiva começando de 10 </h4>

<h5> Ex.:  746.824.890-70 = 7 x 10 - 4 x 9 - 6 x 8 - 8 x 7 - 2 x 6 - 4 x 5 - 8 x 4 - 9 x 3 - 0 x 2
</h5>

<h4> Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301 </h4>

<h4> Multiplicar o resultado anterior por 10 - 
301 * 10 = 3010 </h4>

<h4>Obter o resto da divisão da conta anterior por 11 -
3010 % 11 = 7 </h4> 

<h4> Se o resultado anterior for maior que 9:
    resultado é 0 </h4>
    
<h4> contrário disso:
    resultado é o valor da conta  </h4>

<h3> Para descobrir o 2° digito, apenas adicione o resultado do 1° digito na parte de multiplicação dos dígitos do CPF </h3>

<hr>

# COMO EXECUTAR O CÓDIGO

1. Clone este repositório:

```bash
git clone https://github.com/allansouza07/VerificadorDeCPF.git
```

2. Acesse a pasta do projeto:

```bash
cd VerificadorDeCPF
```

3. Execute o arquivo:

```bash
python cpf.py
```

# MENU DO PROGRAMA

Ao iniciar o programa, o usuário poderá escolher uma das seguintes opções:

```
[1] Descobrir os dois últimos dígitos do CPF
[2] Validar um CPF
[3] Gerar um CPF aleatório
```

# OBJETIVO DO PROJETO

Este projeto foi desenvolvido para praticar conceitos fundamentais de programação em Python, como:

- Funções
- Laços de repetição (`for` e `while`)
- Condicionais (`if`)
- Tratamento de exceções (`try`/`except`)
- Manipulação de strings
- Listas
- Geração de números aleatórios
- Lógica matemática aplicada ao algoritmo oficial do CPF


# DESENVOLVEDOR

Allan de Souza - Estudante de ADS no IFSP.

[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/allansouzagg) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/allan-de-souza-2917622b9?utm_source=share_via&utm_content=profile&utm_medium=member_ios/?locale=en)
