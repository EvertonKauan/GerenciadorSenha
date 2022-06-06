import pymysql
#Criar conexão
conexao = pymysql.connect(host='localhost',port=3308,database='gerenciador_senhas',
                          user='root',password='root',autocommit=True)
#cursor
cursor = conexao.cursor()
print('-' + '==-' * 8)
print('  \033[1mGERENCIADOR DE SENHAS')
desejo = 'n'


while True:
    print('-' + '==-' * 8)
    menu = '''      MENU INICIAL
-==-==-==-==-==-==-==-==-
[1] Adicionar nova senha
[2] Acessar senhas
[3] Deletar senha
[4] Sair'''
    print(f'\033[1m{menu}') #Exibição de opções
    print('-' + '==-' * 8)
    print('\033[;1m')
    c = 0

    escolha = int(input("O que você deseja fazer? "))
    while True:
        if escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4:
            break
        #Caso o usuário tente fugir das possibilidades
            escolha = int(input("Digite uma opção válida: "))
        print()

    #Dentro de um bloco Try, para tratar os erros
    try:
        #CRIAR NOVA SENHA
        if escolha == 1:
            descricao = str(input("Digite o nome da plataforma: ").upper())
            password_user = str(input("Digite a senha: "))
            comando = ("INSERT INTO table_user (description, password) values (%s, %s)") #INSERIR NA TABELA A PLATAFORMA E SUA SENHA
            val = (descricao, password_user) #criada tupla, para inserir dados na coluna
            cursor.execute(comando,val) #execução
            print('\n\033[;32mSeu novo cadastro obteve sucesso.\033[;1m\n') #Confirmação de cadastro

        #VISUALIZAR OU EXCLUIR SENHAS JÁ CADASTRADAS
        if escolha ==2 or escolha == 3:
            consulta = ("select * from table_user")  # selecionar a tabela, para poder visualiza-la
            cursor.execute(consulta)
            linhas = cursor.fetchall()  # contar quantas linhas existem nas colunas
            contador_linhas = 0
            for quantidade_linhas in linhas:
                contador_linhas += 1
            if contador_linhas < 1: #Se for menor que 1, é porque não possui nenhum registro no banco de dados
                print()
                print("\033[;31mVocê ainda não possui senhas! Volte ao menu para cadastrar!\033[;1m") #CASO NÃO TENHA SENHAS ELE NÃO CONTINUA
                print()
            else:
                print("\nPLATAFORMAS DISPONÍVEIS:\n") #Exibição das possibilidades
                for linha in linhas:
                    print(f"[{linha[2]}]", linha[0])
                print()
                consulta = ("select * from table_user")
                cursor.execute(consulta)
                linhas = cursor.fetchall()
                if escolha == 2:
                    plataforma_desejada = int(input("Qual você quer acessar? "))
                    for linha2 in linhas:
                        if plataforma_desejada == linha2[2]: #Comparando, para quando o valor varrido for o desejado pelo usuário, exibir após o if
                            print()
                            print("Plataforma:", linha2[0])
                            print("Senha:", linha2[1])
                            print()
                else:
                    plataforma_desejada = int(input("Qual você quer deletar? "))
                    confirmacao = str(input("\033[;31mRealmente deseja deletar o registro? A ação será permanente: [s/n] \033[;1m"))
                    confirmacao = confirmacao.lower()
                    if confirmacao == "s":
                        for linha2 in linhas:
                            if plataforma_desejada == linha2[2]: #Comparando, para quando o valor varrido for o desejado pelo usuário
                                excluir = ('DELETE FROM table_user where id_description = (%s)')
                                valor_excluir = linha2[2]
                                cursor.execute(excluir, valor_excluir)
                                print('\n\033[;32mDeletado com sucesso!\033[;1m\n')

                                for quantidade_linhas in linhas:
                                    contador_linhas +=1
                                if contador_linhas > 1:
                                    resetar_id = ('ALTER TABLE table_user AUTO_INCREMENT = 1') #Resetar o ID, quando não houver mais senhas
                                    cursor.execute(resetar_id)
        elif escolha == 4:
            print('\n\033[;32mAté breve!') #Encerrar programa
            break

    except Exception as e:
        print(f"Erro: {e}")
    desejo = str(input("Deseja voltar ao menu inicial? [s/n] ").lower())
    print()

    if desejo == "n":
        print("\033[;32mAté breve!") #Encerrar programa
        conexao.close() #fechar conexão
        break