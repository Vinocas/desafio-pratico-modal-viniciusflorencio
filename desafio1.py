'''
1) A ModalGR possui um cofre eletrônico que precisa estar protegido por 3 senhas, sendo 
essas criptografadas e armazenadas numa base de dados SQL. Cada uma dessas senhas deve 
possuir uma regra/método de criptografia distinta, mas ambas devem utilizar uma única 
chave secreta. Para isso, você foi escolhido para criar o sistema de criptografia dessas senhas.
Chave secreta:
#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista
Observação: Codificar apenas a parte responsável pela criptografia das senhas, sem a 
necessidade da codificação de inclusão na base SQL.
'''

def cripto(senha, chave):
    #Função de criptografia principal
    criptografado = ""

    #Esse loop percorre cada caracter da string 'senha'
    for i, c in enumerate(senha):
        #Da o valor do modulo do índice pelo comprimento da variável 'chave' para a variável 'chave_char' 
        #Isso garante que a chave se repita caso o comprimento da senha seja maior que 56 caracteres.
        chave_char = chave[i % len(chave)]
        
        #Faz uma operação XOR entre os valores ASCII dos caracteres da senha e da chave
        xor_resultado = ord(c) ^ ord(chave_char)

        #Converte o resultado da operação anterior para char e adiciona na variável 'criptografado'
        criptografado += chr(xor_resultado)
        
    return criptografado


def criptografia1(senha, chave):
    #Retorna a criptografia padrão
    return [
        cripto(senha, chave),
    ]
    
def criptografia2(senha, chave):
    #Retorna a criptografia na ordem inversa
    return [
        cripto(senha[::-1], chave[::-1]),
    ]
    
def criptografia3(senha, chave):
    #Realiza a criptografia com os caracteres em caixa alta e retorna
    return [
        cripto(senha.upper(), chave.upper()),
    ]

if __name__ == "__main__":
    chave = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"
    senha1 = input('Insira a primeira senha que ser criptografada: ')
    senha2 = input('Insira a segunda senha que será criptografada: ')
    senha3 = input('Insira a terceira senha que será criptografada: ')

    senha1Cripto = criptografia1(senha1, chave)
    senha2Cripto = criptografia2(senha2, chave)
    senha3Cripto = criptografia3(senha3, chave)

    print("Primeira senha criptograda:", senha1Cripto)
    print("Segunda senha criptograda:", senha2Cripto)
    print("Terceira senha criptograda:", senha3Cripto)