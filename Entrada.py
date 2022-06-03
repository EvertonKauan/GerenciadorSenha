import pymysql
#Criar conexão
conexao = pymysql.connect(host='localhost',port=3308,database='gerenciador_senhas',
                          user='root',password='root',autocommit=True)
#cursor
cursor = conexao.cursor()

desejo = 'n'
while True:
    print("NOVA SENHA [1] VISUALIZAR PLATAFORMAS JÁ CADASTRADAS [2]")
    c = 0

    escolha = int(input("O QUE VOCÊ DESEJA FAZER? "))
    while True:
        if escolha == 1 or escolha == 2:
            break
        #Caso o usuário tente fugir das possibilidades
        escolha = int(input("Digite uma das alternativas mencionadas([1] [2]): "))
    print()

    #Dentro de um bloco Try, para tratar os erros
    try:
        #CRIAR NOVA SENHA evertonkauan
        if escolha == 1:
            descricao = str(input("Digite a rede social: "))
            password_user = str(input("Digite a senha: "))
            comando = ("INSERT INTO table_user (description, password) values (%s, %s)") #INSERIR NA TABELA A PLATAFORMA E SUA SENHA
            val = (descricao, password_user) #criada tupla, para inserir dados na coluna
            cursor.execute(comando,val) #execução

        #VISUALIZAR SENHAS JÁ CADASTRADAS
        if escolha ==2:
            consulta = ("select * from table_user") #selecionar a tabela, para poder visualiza-la
            cursor.execute(consulta)
            linhas = cursor.fetchall() #contar quantas linhas existem nas colunas
            print("Número total de plataformas cadastradas:", cursor.rowcount)
            for linha in linhas:
                print("Plataforma:", linha[0])
                print("ID:", linha[2], "\n")

            consulta = ("select * from table_user")
            cursor.execute(consulta)
            linhas = cursor.fetchall()
            plataforma_desejada = int(input("Digite qual ID você quer visualizar: "))
            for linha2 in linhas:
                if plataforma_desejada == linha2[2]: #Comparando, para quando o valor varrido for o desejado pelo usuário, exibir após o if
                    print()
                    print("Plataforma escolhida foi", linha2[0])
                    print("Senha:", linha2[1])
                    print()

    except Exception as e:
        print(f"Erro: {e}")

    desejo = str(input("Deseja voltar ao menu? [s/n] "))
    desejo = desejo.lower()

    if desejo == "n":
        print("Programa encerrado.")
        conexao.close() #fechar conexão
        break
