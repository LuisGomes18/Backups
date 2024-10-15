from config.opcoes_menu import backup_manual
from config.opcoes_menu_secundario import escolher_pastas_backup, escolher_pasta_destino, escolher_argendamento, escolher_email_destinatario


def menu():
    while True:
        escolha_menu = int(input('''
        1 - Configurar backup automatico
        2 - Criar backup (manual)
        3 - Listar backups
        4 - Apagar backup
        5 - Menu Secundario
        0 - Sair
        -> '''))

        if not isinstance(escolha_menu, int):
            print('Opcão invalida')
            menu()

        match escolha_menu:
            case 1:
                print('Configurar backup automatico')
            case 2:
                print('Criar backup (manual)')
                backup_manual()
            case 3:
                print('Listar backups')
            case 4:
                print('Apagar backup')
            case 5:
                print('Menu Secundario')
                menu_secundario()
            case 0:
                print('Saindo...')
                exit()
            case _:
                print('Opcão invalida')
                menu()

def menu_secundario():
    while True:
        escolha_menu_secundario = int(input('''
        1 - Escolher pasta para fazer backup
        2 - Escolhe a pasta do destino (PC)
        3 - Escolhe a pasta da nuvem
        4 - Escolhe o agendamento
        5 - Escolhe o email de notificação
        6 - Voltar
        0 - Sair
        -> '''))

        if not isinstance(escolha_menu_secundario, int):
            print('Opcão invalida')
            menu_secundario()

        match escolha_menu_secundario:
            case 1:
                print('Escolher pastas para fazer backup')
                escolher_pastas_backup()
            case 2:
                print('Escolher pasta do destino (PC)')
                escolher_pasta_destino()
            case 3:
                # print('Escolhe a pasta da nuvem')
                print('Nao implementado')
            case 4:
                print('Escolhe o agendamento')
                escolher_argendamento()
            case 5:
                print('Escolhe o email de notificação')
                escolher_email_destinatario()
            case 6:
                print('Voltando...')
                menu()
            case 0:
                print('Saindo...')
                exit()
            case _:
                print('Opcão invalida')
                menu_secundario()


menu()