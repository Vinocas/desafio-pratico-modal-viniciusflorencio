'''
2) A ModalGR possui um arquivo texto contendo o nome completo, e-mail e data de 
nascimento de seus consultores, separados por pipeline (|). O time de RH deseja que todo 
início de cada mês seja gerado um novo arquivo texto com apenas os dados dos 
aniversariantes do mês corrente, para assim, enviarem uma mensagem personalizada de 
felicitações. Você foi escolhido para criar uma solução que atenda esses quesitos.
'''

import datetime

#Essa função verifica a data de nascimento do consultor e compara o mês de aniversário com o mês atual. Retorna verdadeiro ou falso
def verificar_aniversario(data_nascimento):
    data_atual = datetime.datetime.now()
    return data_nascimento.month == data_atual.month

if __name__ == "__main__":
    #Abre o arquivo 'consultores.txt' em modo leitura, conta quantas linhas existem e guarda na variável 'cont_linhas'
    with open('consultores.txt', 'r') as consultores:
        cont_linhas = consultores.readlines()

    #Abre o arquivo 'aniversariantes.txt' em modo de escrita e roda um laço de repetição na variável 'cont_linhas'. 
    #Para cada linha é aplicada uma condição: se a função 'verificar_aniversario' retornar VERDADEIRA deve-se inserir a linha em questão no arquivo 'aniversariantes.txt'.
    with open('aniversariantes.txt', 'w') as aniversariantes:
        for linha in cont_linhas:
            dados = linha.strip().split('|')
            nome_completo, email, data_nascimento = dados
            data_nascimento = datetime.datetime.strptime(data_nascimento, '%d/%m/%Y')
            if verificar_aniversario(data_nascimento):
                aniversariantes.write(f"{nome_completo} | {email} | {data_nascimento.strftime('%d/%m/%Y')}\n")

    print("Os aniversariantes do mês foram inseridos no arquivo 'aniversariantes.txt'.")