'''
3) A ModalGR criará um programa de empréstimo para os colaboradores que possuem tempo 
de casa superior a 5 anos. O colaborador poderá simular um empréstimo de até 2 vezes o valor 
de seu respectivo salário, desde que esse valor seja múltiplo de 2. Esse programa dará a 
possibilidade de retirada em dinheiro vivo, de acordo com as seguintes opções:
➢ Notas de maior valor: considerando primeiramente as notas de 100 e 50 reais, e em 
seguida, as inferiores;
➢ Notas de menor valor: considerando as notas de 20, 10, 5 e 2 reais.
➢ Notas meio a meio: metade do valor em notas maiores e a outra metade em notas 
menores.

Essas opções deverão ser exibidas ao colaborador, para assim, realizar a escolha de acordo com 
sua necessidade.
Visando atender esse quesito, você foi escolhido para nos ajudar nessa solução! 
A ideia é ter os seguintes campos para inserção: do nome do colaborador, data de admissão, 
salário atual, valor de empréstimo, e em seguida, exibir as opções de retirada, por exemplo:
Valor empréstimo: 8.550 reais

Notas de maior valor: 
➢ 85 x 100 reais;
➢ 1 x 50 reais.

Notas de menor valor: 
➢ 427 x 20 reais;
➢ 1 x 10 reais.

Notas meio a meio:
4.275 reais em notas de maior valor:
➢ 42 x 100 reais;
➢ 1 x 50 reais;
➢ 1 x 20 reais;
➢ 1 x 5 reais.

4.275 reais em notas de menor valor:
➢ 213 x 20 reais;
➢ 1 x 10 reais;
➢ 1 x 5 reais.

Observações: 
➢ Caso o colaborador não se enquadre nos requisitos mínimos de adesão ao programa 
de empréstimo, exiba a mensagem: Agradecemos seu interesse, mas você não atende 
os requisitos mínimos do programa.
➢ Caso o colaborador insira um valor de empréstimo que não seja múltiplo de 2, exiba a 
mensagem: Insira um valor válido
'''

import datetime

def pagamento_maior_valor():
    #Essa função retorna as notas de maior valor
    valor_maior = valor_emprestimo
    notas_100 = valor_maior // 100
    valor_maior %= 100
    
    notas_50 = valor_maior // 50
    valor_maior %= 50
    
    notas_20 = valor_maior // 20 
    valor_maior %= 20
    
    notas_10 = valor_maior // 10 
    valor_maior %= 10
    
    notas_5 = valor_maior // 5 
    valor_maior %= 5
    
    notas_2 = valor_maior // 2 
    
    print("\nNotas de maior valor:")
    print(f"➢ {notas_100} x 100 reais;")
    print(f"➢ {notas_50} x 50 reais;")
    print(f"➢ {notas_20} x 20 reais;")
    print(f"➢ {notas_10} x 10 reais;")
    print(f"➢ {notas_5} x 5 reais;")
    print(f"➢ {notas_2} x 2 reais;")

def pagamento_menor_valor():
    #Essa função retorna as notas de menor valor
    valor_menor = valor_emprestimo
    notas_20 = valor_menor // 20 
    valor_menor %= 20
    
    notas_10 = valor_menor // 10 
    valor_menor %= 10
    
    notas_5 = valor_menor // 5 
    valor_menor %= 5
    
    notas_2 = valor_menor // 2 
    
    print("\nNotas de menor valor:")
    print(f"➢ {notas_20} x 20 reais;")
    print(f"➢ {notas_10} x 10 reais;")
    print(f"➢ {notas_5} x 5 reais;")
    print(f"➢ {notas_2} x 2 reais;")

def pagamento_meio_a_meio():
    #Lógica de maior valor
    valor_metade = valor_emprestimo // 2
    
    valor_maior = valor_metade
    notas_100 = valor_maior // 100
    valor_maior %= 100
    
    notas_50 = valor_maior // 50
    valor_maior %= 50
    
    notas_20 = valor_maior // 20 
    valor_maior %= 20
    
    notas_10 = valor_maior // 10 
    valor_maior %= 10
    
    notas_5 = valor_maior // 5 
    valor_maior %= 5
    
    notas_2 = valor_maior // 2 

    #Lógica de menor valor
    valor_menor = valor_metade
    notas_20_menor = valor_menor // 20 
    valor_menor %= 20
    
    notas_10_menor = valor_menor // 10 
    valor_menor %= 10
    
    notas_5_menor = valor_menor // 5 
    valor_menor %= 5
    
    notas_2_menor = valor_menor // 2 
 
    print("\nNotas meio a meio:")
    print(f"{valor_metade} reais em notas de maior valor:")
    print(f"➢ {notas_100} x 100 reais;")
    print(f"➢ {notas_50} x 50 reais;")
    print(f"➢ {notas_20} x 20 reais;")
    print(f"➢ {notas_10} x 10 reais;")
    print(f"➢ {notas_5} x 5 reais;")
    print(f"➢ {notas_2} x 2 reais;")
    print(f"\n{valor_metade} reais em notas de menor valor:")
    print(f"➢ {notas_20_menor} x 20 reais;")
    print(f"➢ {notas_10_menor} x 10 reais;")
    print(f"➢ {notas_5_menor} x 5 reais;")
    print(f"➢ {notas_2_menor} x 2 reais;")

if __name__ == "__main__":
    print("Bem-vindo ao Programa de Empréstimo da ModalGR!")
    print("\nCondições do empréstimo: apenas para colaboradores com mais de 5 anos de empresa, valor do empréstimo precisa ser múltiplo de 2 e não pode ultrapassar o dobro do seu salário atual.")
    nome = input("\nNome do colaborador: ")
    data_admissao = int(input("Ano de admissão: "))
    salario_atual = float(input("Salário atual: "))
    print(f"\nLimite de empréstimo concedido: {int(salario_atual) * 2}")
    valor_emprestimo = int(input("Valor do empréstimo desejado: "))
    
    #Atribui valor na função 'anos_trabalhados' de acordo com a data_admissao
    anos_trabalhados = datetime.datetime.now().year - data_admissao

    #Condição de múltiplo de 2
    while valor_emprestimo % 2 != 0:
        valor_emprestimo = int(input("Insira um valor válido: "))
        
    if anos_trabalhados > 5 and valor_emprestimo <= salario_atual * 2 and valor_emprestimo % 2 == 0:
        print(f'\n{nome}, você pode sacar o valor do empréstimo nas seguintes condições:')
        pagamento_maior_valor()
        pagamento_menor_valor()
        pagamento_meio_a_meio()

    else:
        print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa")