import os, time, sys

# tela inicial


titulo = '''
  ___   ___  ___    _   _____  ___   ___        ___     _        _____  ___    _  __   __ ___  ___   ___  ___    _ 
 |   \ | __|/ __|  /_\  | |_  |_ _| / _ \      |   \   /_\      |_   _|| _ \  /_\ \ \ / /| __|/ __| / __||_ _|  /_\ 
 | |) || _| \__ \ / _ \ | __|  | | | (_) |     | |) | / _ \       | |  |   / / _ \ \ V / | _| \__ \ \__ \ | |  / _ \   
 |___/ |___||___//_/ \_\|_|   |___| \___/      |___/ /_/ \_\      |_|  |_|_\/_/ \_\ \_/  |___||___/ |___/|___|/_/ \_\  
                                                                                                                           

'''

print(titulo)
com = input(f'{"Aperte Enter para continuar":^120}')
os.system('cls') or None

# cadastro e login

nome = input("Qual o nome do usuário? " ).strip().lower()
os.system('cls') or None
while nome == '':
    print("Campo de digitação vazio. Insira algum nome de usuário.")
    nome = input("Qual o nome do usuário? " ).strip().lower()
    os.system('cls') or None

print("Olá", nome)
print("O seu nome de usuário será utilizado como login do jogo.")
time.sleep(3)
os.system('cls') or None

lista = ['pai', 'mae', 'joao', 'luiz', 'thaisa', 'camila', 'guarda', 'detento', 'mãe', 'joão', 'luis']
os.system('cls') or None

personagem = input("Qual o nome do personagem? ").strip().lower()
while personagem == '':
    print("Campo de digitação vazio. Insira algum nome para o personagem.")
    personagem = input("Qual o nome do personagem? ").strip().lower()
    os.system('cls') or None
while personagem in lista:
    print("Esse nome não está disponível.")
    personagem = input("Insira outro nome para o personagem:").strip().lower()
    os.system('cls') or None
    while personagem == '':
        print("Campo de digitação vazio. Insira algum nome para o personagem.")
        personagem = input("Qual o nome do personagem? ").strip().lower()
        os.system('cls') or None
    
if personagem not in lista:
    os.system('cls') or None
    
    senha = input("Informe a sua senha: " ).strip().lower()
    os.system('cls') or None
    while senha == '':
        print("Campo de digitação vazio. Insira alguma senha.")
        senha = input("Informe a sua senha: " ).strip().lower()
        os.system('cls') or None
    senha2 = input("Confirme a sua senha: " ).strip().lower()
    while senha != senha2:
        os.system('cls') or None
        print("A confirmação da senha falhou, informe a senha novamente.")
        senha = input("Informe a sua senha: " ).strip().lower()
        os.system('cls') or None
        while senha == '':
            print("Campo de digitação vazio. Insira alguma senha.")
            senha = input("Informe a sua senha: " ).strip().lower()
            os.system('cls') or None
        senha2 = input("Confirme a sua senha: " ).strip().lower()
        os.system('cls') or None
if senha == senha2:
    print("Parabéns", personagem, "você está cadastrado.")
    time.sleep(3)
    os.system('cls') or None

# menu


print(f'{"MENU":^120}')
print("Bem vindo(a) ao Desafio da travessia", personagem, "!")
print("Se deseja ver um pequeno tutorial do desafio, digite 1 e aperte Enter.")
print("Se deseja ir direto ao desafio, digite 2 e aperte Enter.")

intr = input()
os.system('cls') or None

while intr != '1' and intr != '2':
    print(f'{"MENU":^120}')
    print("O caractere que você digitou é diferente das opções ofertadas.")
    print("Se deseja ver um pequeno tutorial do desafio, digite 1 e aperte Enter.")
    print("Se deseja ir direto ao desafio, digite 2 e aperte Enter.")
    intr = input()
    os.system('cls') or None
while intr == '1':
    os.system('cls') or None
    print(f'{"VISÃO GERAL":^120}')
    print("O objetivo desse jogo é atravessar todas as pessoas de uma margem até a outra do rio,") 
    print("Mas você deve obedecer a todas as regras estabelecidas:")
    print("- Somente o pai, a mãe e o Guarda sabem pilotar o barco;")
    print("- A mãe não pode ficar sozinha com os filhos joao e luiz, ou seja, sem a presença do pai;")
    print("- O pai não pode ficar sozinho com as filhas camila e thaisa, ou seja, sem a presença da mãe;")
    print("- O detento não pode ficar sozinho com nenhum integrante da família;")
    print("- O barco só pode transportar 2 pessoas por vez;")
    print("- Você só terá uma oportunidade para achar a sequencia certa.")
    cont = input(f'{"Aperte Enter para continuar ":^120}')
    os.system('cls') or None
    print(f'{"COMO JOGAR":^120}')
    print("Para selecionar qual o personagem subirá ao barco, utilize os seguintes comandos:")
    print("(P)ai", "\n(M)ãe", "\n(J)oao", "\n(L)uis", "\n(C)amila", "\n(T)haisa", "\n(G)uarda", "\n(D)etento")
    print("Selecione 1 ou 2 personagens e aperte Enter.")
    vol = input(f'{"Aperte Enter para voltar":^120}')
    
    os.system('cls') or None

    print(f'{"MENU":^120}')
    print("Bem vindo(a) ao Desafio da travessia", personagem, "!")
    print("Se deseja ver um pequeno tutorial do desafio, digite 1 e aperte Enter.")
    print("Se deseja ir direto ao desafio, digite 2 e aperte Enter.")
    intr = input()
    os.system('cls') or None
    while intr != '1' and intr != '2':
        os.system('cls') or None
        print(f'{"MENU":^120}')
        print("O caractere que você digitou é diferente das opções ofertadas.")
        print("Se deseja ver um pequeno tutorial do desafio, digite 1 e aperte Enter.")
        print("Se deseja ir direto ao desafio, digite 2 e aperte Enter.")
        intr = input()
        os.system('cls') or None
   

if intr == '2':
    os.system('cls') or None
    print("Muito bem", personagem, ".")
    print("Vamos começar o desafio!")
    time.sleep(2)
    os.system('cls') or None

# jogo

fim = '''
    ___    _     __  __  ___      __   __   __  ___  ___
   / __|  /_\   |  \/  || __|    / _ \ \ \ / / | __|| _ \  
  | (_ | / _ \  | |\/| || _|    | (_) | \ V /  | _| |   /  
   \___|/_/ \_\ |_|  |_||___|    \___/   \_/   |___||_|_\  
                                                        
                        (✖╭╮✖)

'''
congratulations = '''
      ___     _     ___     _     ___  ___  _  _  ___     _
     | _ \   /_\   | _ \   /_\   | _ )| __|| \| |/ __|   | |     
     |  _/  / _ \  |   /  / _ \  | _ \| _| | .` |\__ \   | |    
     |_|   /_/ \_\ |_|_\ /_/ \_\ |___/|___||_|\_||___/   (_) 
                                                           
__   __  ___    ___  ___     __   __  ___  _  _   ___  ___  _   _    _
\ \ / / / _ \  / __|| __|    \ \ / / | __|| \| | / __|| __|| | | |  | |
 \ V / | (_) || (__ | _|      \ V /  | _| | .` || (__ | _| | |_| |  |_|
  \_/   \___/  \___||___|      \_/   |___||_|\_| \___||___| \___/   (_)

             ＼(^o^)／                       ＼(^o^)／
'''


while True:
    print(f'{"Escolha quem vai atravessar":^120}')
    print(f'{"Obs: lembre-se que não precisa obrigatoriamente preencher os dois espaços":^120}')
    print("(P)ai", "(M)ãe", "(J)oao", "(L)uis", "(C)amila", "(T)haisa", "(G)uarda", "(D)etento")
    lista = ['Pai', 'Mãe', 'Joao', 'Luis', 'Camila', 'Thaisa', 'Guarda', 'Detento']
    p1 = input("1º Personagem: " ).upper().strip()
    p2 = input("2º Personagem: " ).upper().strip()
    if p1 == 'D' and p2 == 'G' or p1 == 'G' and p2 == 'D':
        os.system('cls') or None
        print("O guarda e o detento atravesseram o rio. Escolha quem vai voltar.")
        print("Opçôes: (G)uarda e (D)etento.")
        pv1 = input("1º Personagem: ").upper().strip()
        os.system('cls') or None
        if pv1 == 'G':
            os.system('cls') or None
            print("O guarda voltou. Escolha mais dois personagens.")
            print("Opções:(P)ai, (M)ãe, (J)oao, (L)uis, (C)amila, (T)haisa e (G)uarda.")
            p3 = input("1º Personagem: " ).upper().strip()
            p4 = input("2º Personagem: " ).upper().strip()
            os.system('cls') or None
            if p3 == 'G' and p4 == 'C' or p3 == 'C' and p4 == 'G':
                print("O guarda atravessou o rio com a filha Camila. Escolha quem vai voltar.")
                print("Opções: (C)amila,(G)uarda e (D)etento.")
                pv2 = input("1º personagem: ").upper().strip()
                pv3 = input("2º personagem: ").upper().strip()
                os.system('cls') or None
                if pv2 == 'G' and pv3 == 'D' or pv2 == 'D' and pv3 == 'G':
                    print("O guarda voltou com o detento, escolha mais dois personagens.")
                    print("Opções: (P)ai, (M)ãe, (J)oao, (L)uis, (T)haisa, (G)uarda e (D)etento.")
                    p5 = input("1º Personagem: " ).upper().strip()
                    p6 = input("2º Personagem: " ).upper().strip()
                    os.system('cls') or None
                    if p5 == 'M' and p6 == 'T' or p5 == 'T' and p6 == 'M':
                        print("A mãe atravessou o rio com a filha Thaisa. Escolha quem vai voltar.")
                        print("Opções:(M)ãe, (T)haisa e (C)amila.")
                        pv4 = input("1º personagem: ").upper().strip()
                        os.system('cls') or None
                        if pv4 == 'M':
                            os.system('cls') or None
                            print("A mãe voltou. Escolha mais dois personagens.")
                            print("Opções:(P)ai, (M)ãe, (J)oao, (L)uis, (G)uarda e (D)etento.")
                            p7 = input("1º Personagem: " ).upper().strip()
                            p8 = input("2º Personagem: " ).upper().strip()
                            os.system('cls') or None
                            if p7 == 'M' and p8 == 'P' or p7 == 'P' and p8 == 'M':
                                print("A mãe atravessou o rio com o pai. Escolha quem vai voltar.")
                                print("Opções:(P)ai, (M)ãe,(T)haisa e (C)amila.")
                                pv5 = input("1º personagem: ").upper().strip()
                                os.system('cls') or None
                                if pv5 == 'P':
                                    os.system('cls') or None
                                    print("O pai voltou, escolha mais dois personagens.")
                                    print("Opções:(P)ai, (J)oao, (L)uis, (G)uarda e (D)etento.")
                                    p9 = input("1º Personagem: " ).upper().strip()
                                    p10 = input("2º Personagem: " ).upper().strip()
                                    os.system('cls') or None
                                    if p9 == 'D' and p10 == 'G' or p9 == 'G' and p10 == 'D':
                                        os.system('cls') or None
                                        print("O guarda e o detento atravesseram o rio. Escolha quem vai voltar.")
                                        print("Opções:(G)uarda, (D)etento, (M)ãe,(T)haisa e (C)amila.")
                                        pv6 = input("Escolha quem vai voltar: ").upper().strip()
                                        os.system('cls') or None
                                        if pv6 == 'M':
                                            os.system('cls') or None
                                            print("A mãe voltou. Escolha mais dois personagens.")
                                            print("Opções:(P)ai, (J)oao, (L)uis e (M)ãe.")
                                            p11 = input("1º Personagem: " ).upper().strip()
                                            p12 = input("2º Personagem: " ).upper().strip()
                                            os.system('cls') or None
                                            if p11 == 'M' and p12 == 'P' or p11 == 'P' and p12 == 'M':
                                                print("A mãe atravessou o rio com o pai. Escolha quem vai voltar.")
                                                print("Opções:(G)uarda, (P)ai, (D)etento, (M)ãe,(T)haisa e (C)amila.")
                                                pv7 = input("1º personagem: ").upper().strip()
                                                os.system('cls') or None
                                                if pv7 == 'P':
                                                    os.system('cls') or None
                                                    print("O pai voltou. Escolha mais dois personagens.")
                                                    print("Opções:(P)ai, (J)oao e (L)uis.")
                                                    p13 = input("1º Personagem: " ).upper().strip()
                                                    p14 = input("2º Personagem: " ).upper().strip()
                                                    os.system('cls') or None
                                                    if p13 == 'J' and p14 == 'P' or p13 == 'P' and p14 == 'J':
                                                        print("O pai atravessou o rio com  o filho João. Escolha quem vai voltar")
                                                        print("Opções: (G)uarda, (D)etento, (M)ãe, (P)ai, (T)haisa, (C)amila e (J)oao")
                                                        pv8 = input("1º personagem: ").upper().strip()
                                                        pv9 = input("2º personagem: ").upper().strip()
                                                        os.system('cls') or None
                                                        if pv8 == 'G' and pv9 == 'D' or pv8 == 'D' and pv9 == 'G':
                                                            print("O guarda voltou com o detento. Escolha mais dois personagens.")
                                                            print("Opções:(G)uarda, (D)etento e (L)uis.")
                                                            p15 = input("1º Personagem: " ).upper().strip()
                                                            p16 = input("2º Personagem: " ).upper().strip()
                                                            os.system('cls') or None
                                                            if p15 == 'G' and p16 == 'L' or p15 == 'L' and p16 == 'T':
                                                                print("O guarda atravessou o rio com o filho Luis. Escolha quem vai voltar")
                                                                print("Opções: (G)uarda, (P)ai, (M)ae, (C)amila, (T)haisa, (J)oao e (L)uis")
                                                                pv10 = input("1º personagem: ").upper().strip()
                                                                os.system('cls') or None
                                                                if pv10 == 'G':
                                                                    os.system('cls') or None
                                                                    print("O guarda voltou escolha mais dois personagens.")
                                                                    print("Opções:(G)uarda e (D)etento.")
                                                                    p17 = input("1º Personagem: " ).upper().strip()
                                                                    p18 = input("2º Personagem: " ).upper().strip()
                                                                    os.system('cls') or None
                                                                    if p17 == 'D' and p18 == 'G' or p17 == 'G' and p18 == 'D':
                                                                        os.system('cls') or None
                                                                        print("Todos os personagens atravesseram o rio.")
                                                                        time.sleep(2)
                                                                        os.system('cls') or None
                                                                        print(congratulations)
                                                                        time.sleep(3)
                                                                        cong = input("Você deseja jogar o jogo novamente? [S/N]").upper().strip()
                                                                        if cong == 'S':
                                                                            os.system('cls') or None
                                                                            continue
                                                                        elif cong == 'N':
                                                                            os.system('cls') or None
                                                                            print("Obrigado por jogar o nosso jogo!")
                                                                            time.sleep(2)
                                                                            raise SystemExit
                                                                        while cong != 'S' and cong != 'N':
                                                                            os.system('cls') or None
                                                                            print("O caractere que você digitou é diferente das opções ofertadas.")
                                                                            cong = input("Você deseja jogar o jogo novamente? [S/N]").upper().strip()
                                                                            os.system('cls') or None
                                                                            if cong == 'S':
                                                                                os.system('cls') or None
                                                                                continue
                                                                            elif cong == 'N':
                                                                                os.system('cls') or None
                                                                                print("Obrigado por jogar o nosso jogo!")
                                                                                time.sleep(2)
                                                                                raise SystemExit
                                                                    else:
                                                                        os.system('cls') or None
                                                                        print("Você não acertou a sequencia.")
                                                                        time.sleep(2)
                                                                        print(fim)
                                                                        vol = input("Aperte Enter para jogar novamente.")
                                                                        os.system('cls') or None
                                                                        continue
                                                                else:
                                                                    os.system('cls') or None
                                                                    print("Você não acertou a sequencia.")
                                                                    time.sleep(2)
                                                                    print(fim)
                                                                    vol = input("Aperte Enter para jogar novamente.")
                                                                    os.system('cls') or None
                                                                    continue
                                                            else:
                                                                os.system('cls') or None
                                                                print("Você não acertou a sequencia.")
                                                                time.sleep(2)
                                                                print(fim)
                                                                vol = input("Aperte Enter para jogar novamente.")
                                                                os.system('cls') or None
                                                                continue
                                                        else:
                                                            os.system('cls') or None
                                                            print("Você não acertou a sequencia.")
                                                            time.sleep(2)
                                                            print(fim)
                                                            vol = input("Aperte Enter para jogar novamente.")
                                                            os.system('cls') or None
                                                            continue
                                                    else:
                                                        os.system('cls') or None
                                                        print("Você não acertou a sequencia.")
                                                        time.sleep(2)
                                                        print(fim)
                                                        vol = input("Aperte Enter para jogar novamente.")
                                                        os.system('cls') or None
                                                        continue
                                                else:
                                                    os.system('cls') or None
                                                    print("Você não acertou a sequencia.")
                                                    time.sleep(2)
                                                    print(fim)
                                                    vol = input("Aperte Enter para jogar novamente.")
                                                    os.system('cls') or None
                                                    continue
                                            else:
                                                os.system('cls') or None
                                                print("Você não acertou a sequencia.")
                                                time.sleep(2)
                                                print(fim)
                                                vol = input("Aperte Enter para jogar novamente.")
                                                os.system('cls') or None
                                                continue
                                        else:
                                            os.system('cls') or None
                                            print("Você não acertou a sequencia.")
                                            time.sleep(2)
                                            print(fim)
                                            vol = input("Aperte Enter para jogar novamente.")
                                            os.system('cls') or None
                                            continue
                                    else:
                                        os.system('cls') or None
                                        print("Você não acertou a sequencia.")
                                        time.sleep(2)
                                        print(fim)
                                        vol = input("Aperte Enter para jogar novamente.")
                                        os.system('cls') or None 
                                        continue
                                else:
                                    os.system('cls') or None
                                    print("Você não acertou a sequencia.")
                                    time.sleep(2)
                                    print(fim)
                                    vol = input("Aperte Enter para jogar novamente.")
                                    os.system('cls') or None
                                    continue
                            else:
                                os.system('cls') or None
                                print("Você não acertou a sequencia.")
                                time.sleep(2)
                                print(fim)
                                vol = input("Aperte Enter para jogar novamente.")
                                os.system('cls') or None
                                continue
                        else:
                            os.system('cls') or None
                            print("Você não acertou a sequencia.")
                            time.sleep(2)
                            print(fim)
                            vol = input("Aperte Enter para jogar novamente.")
                            os.system('cls') or None
                            continue
                    else:
                        os.system('cls') or None
                        print("Você não acertou a sequencia.")
                        time.sleep(2)
                        print(fim)
                        vol = input("Aperte Enter para jogar novamente.")
                        os.system('cls') or None
                        continue
                else:
                    os.system('cls') or None
                    print("Você não acertou a sequencia.")
                    time.sleep(2)
                    print(fim)
                    vol = input("Aperte Enter para jogar novamente.")
                    os.system('cls') or None
                    continue
            else:
                os.system('cls') or None
                print("Você não acertou a sequencia.")
                time.sleep(2)
                print(fim)
                vol = input("Aperte Enter para jogar novamente.")
                os.system('cls') or None
                continue
        else:
            os.system('cls') or None
            print("Você não acertou a sequencia.")
            time.sleep(2)
            print(fim)
            vol = input("Aperte Enter para jogar novamente.")
            os.system('cls') or None
            continue 
    else:
        os.system('cls') or None
        print("Você não acertou a sequencia.")
        time.sleep(2)
        print(fim)
        vol = input("Aperte Enter para jogar novamente.")
        os.system('cls') or None 
        continue