import pymysql
#Criar conexão
conexao = pymysql.connect(host='localhost',port=3308,database='gerenciador_senhas',
                          user='root',password='root',autocommit=True)
#cursor
cursor = conexao.cursor()

#input
desejo = 'n'
while True:
    print("NOVA SENHA [1] VISUALIZAR PLATAFORMAS JÁ CADASTRADAS [2]")
    c = 0

    escolha = int(input("O QUE VOCÊ DESEJA FAZER? "))
    while True:

        if escolha == 1 or escolha == 2:
            break

        escolha = int(input("Digite uma das alternativas mencionadas([1] [2]): "))
    print()
    try:
        if escolha == 1:
            descricao = str(input("Digite a rede social: "))
            password_user = str(input("Digite a senha: "))
            comando = ("INSERT INTO table_user (description, password) values (%s, %s)")
            val = (descricao, password_user)
            cursor.execute(comando,val)
        if escolha ==2:
            consulta = ("select * from table_user")
            cursor.execute(consulta)
            linhas = cursor.fetchall()
            print("Número total de plataformas cadastradas:", cursor.rowcount)
            for linha in linhas:
                print("Plataforma:", linha[0])
                print("ID:", linha[2], "\n")

            consulta = ("select * from table_user")
            cursor.execute(consulta)
            linhas = cursor.fetchall()
            plataforma_desejada = int(input("Digite qual ID você quer visualizar: "))
            for linha2 in linhas:
                if plataforma_desejada == linha2[2]:
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
