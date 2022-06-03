import pymysql

#Conexão criada
conexao = pymysql.connect(host="localhost", port=3308, database="gerenciador_senhas",
                          user="root",password="root",autocommit=True)

#Cursor
cursor = conexao.cursor()

#Insercao
desejo = 'n'
while True:
    print("TIKTOK [1] FACEBOOK [2] INSTAGRAM [3]")
    c = 0

    escolha = int(input("QUAL SENHA VOCÊ DESEJA ARMAZENAR? "))
    while True:

        if escolha == 1 or escolha == 2 or escolha == 3:
            break

        escolha = int(input("Digite uma das alternativas mencionadas([1] [2] [3]): "))
    print()
    try:
        if escolha == 1:
            senhatiktok = str(input("Digita ai a senha do tiktok: "))
            comando = ("INSERT INTO senha_tiktok (senhadotiktok) values (%s)")
            valor = senhatiktok
            cursor.execute(comando,valor)
            print("Senha guardada com sucesso!")
        elif escolha == 2:
            senhaface = str(input("Digita ai a senha do facebook: "))
            comando = ("INSERT INTO senha_facebook (senhadoface) values (%s)")
            valor = senhaface
            cursor.execute(comando,valor)
            print("Senha guardada com sucesso!")
        elif escolha == 3:
            senhainsta = str(input("Digita ai a senha do Instagram: "))
            comando = ("INSERT INTO senha_insta (senhadoinsta) values (%s)")
            valor = senhainsta
            cursor.execute(comando, valor)
            print("Senha guardada com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")

    desejo = str(input("Deseja inserir outra senha? [s/n] "))
    desejo = desejo.lower()

    if desejo == "n":
        print("Programa encerrado.")
        conexao.close()
        break