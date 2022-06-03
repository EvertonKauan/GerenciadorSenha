import pymysql
#Criar conexão
conexao = pymysql.connect(host='localhost',port=3308,database='gerenciador_senhas',
                          user='root',password='root',autocommit=True)
#cursor
cursor = conexao.cursor()

#input
desejo = 'n'
while True:
    print("FACEBOOK [1] INSTAGRAM [2] NOVA SENHA [3]")
    c = 0

    escolha = int(input("O QUE VOCÊ DESEJA FAZER? "))
    while True:

        if escolha == 1 or escolha == 2 or escolha == 3:
            break

        escolha = int(input("Digite uma das alternativas mencionadas([1] [2] [3]): "))
    print()
    try:
        if escolha == 1:
            senhaface = str(input("Digita ai a senha do facebook: "))
            comando = ("INSERT INTO senha_facebook (senha_do_face) values (%s)")
            valor = senhaface
            cursor.execute(comando,valor)
            print("Senha guardada com sucesso!")
        elif escolha == 2:
            senhainsta = str(input("Digita ai a senha do Instagram: "))
            comando = ("INSERT INTO senha_instagram (senha_do_insta) values (%s)")
            valor = senhainsta
            cursor.execute(comando, valor)
            print("Senha guardada com sucesso!")
        elif escolha == 3:
            descricao = str(input("Digite a rede social: "))
            password_user = str(input("Digite a senha: "))
            comando = ("INSERT INTO table_user (description, password) values (%s, %s)")
            val = (descricao, password_user)
            cursor.execute(comando,val)
            #comando_create2 = ("INSERT INTO table_user (password) value (%s)")
            #cursor.execute(comando_create, descricao, password_user)
            #cursor.execute(comando_create2, password_user)

    except Exception as e:
        print(f"Erro: {e}")

    desejo = str(input("Deseja inserir outra senha? [s/n] "))
    desejo = desejo.lower()

    if desejo == "n":
        print("Programa encerrado.")
        conexao.close() #fechar conexão
        break
