import os
from config.json_handler import carregar_configuracao, guardar_configuracao


def verificacao_pasta(pasta):
    '''
    Verifica se a pasta existe.

    - 'pasta' é o caminho da pasta a ser verificada.
    - A pasta existe se o caminho for verdadeiro e o caminho existir no sistema de arquivos.
    - A função retorna um booleano (True ou False) indicando se a pasta existe ou não.
    '''
    return bool(pasta and os.path.exists(pasta))


def escolher_pastas_backup():
    '''
    Pergunta ao usuario quais as pastas que ele deseja fazer backup.

    - O usuario pode digitar uma ou mais pastas separadas por vírgula.
    - A função verifica se as pastas existem no sistema de arquivos.
    - Se uma pasta nao existe, um aviso é impresso.
    - As pastas validas são adicionadas a lista de pastas validas.
    - A lista de pastas validas é salva na configuracao do programa.
    '''
    # Pergunta ao usuario quais as pastas que ele deseja fazer backup.
    pasta_input = input('Pasta para fazer backup (separadas por vírgula): ')

    # Separa as pastas em uma lista, removendo os espaços em branco.
    pastas = [pasta.strip() for pasta in pasta_input.split(',')]

    # Cria uma lista de pastas validas, ou seja, que existem no sistema de arquivos.
    pastas_validas = []
    for pasta in pastas:
        # Verifica se a pasta existe.
        if verificacao_pasta(pasta):
            # Se a pasta existe, adiciona ela a lista de pastas validas.
            pastas_validas.append(pasta)
        else:
            # Se a pasta nao existe, imprime um aviso.
            print(f'Pasta: {pasta} não pode ser encontrada!')

    # Carrega a configuracao do programa.
    config = carregar_configuracao()

    # Substitui a lista de pastas validas na configuracao.
    config["pastas_backup"] = pastas_validas

    # Salva a configuracao.
    guardar_configuracao(config)

    # Imprime as pastas selecionadas.
    print('Pastas selecionadas:', pastas_validas)


def escolher_pasta_destino():
    '''
    Pergunta ao usuario qual a pasta de destino para os backups.

    - Se o usuario nao digitar nada, assume que ele quer usar a pasta atual como destino.
    - A pasta digitada e verificada se existe no sistema de arquivos.
    - Se a pasta existe, a configuracao do programa e atualizada com a pasta de destino.
    - Se a pasta nao existe, um aviso e impresso.
    '''
    # Pergunta ao usuario qual a pasta de destino para os backups.
    pasta_input = input('Pasta do destino (PC): ')

    # Se o usuario nao digitar nada, assume que ele quer usar a pasta atual como destino.
    if not pasta_input:
        print('A escolher pasta padrao')
        # Pega a pasta atual como a pasta de destino.
        pasta_input = os.getcwd()

    # Remove os espaços em branco da pasta digitada.
    pasta = pasta_input.strip()

    # Verifica se a pasta existe no sistema de arquivos.
    if verificacao_pasta(pasta):
        # Carrega a configuracao do programa.
        config = carregar_configuracao()

        # Substitui a pasta de destino na configuracao.
        config["pasta_destino"] = pasta

        # Salva a configuracao.
        guardar_configuracao(config)

        # Imprime a pasta selecionada.
        print('Pasta selecionada:', pasta)
    else:
        # Se a pasta nao existe, imprime um aviso.
        print(f'Pasta: {pasta} não pode ser encontrada!')


def escolher_argendamento():
    '''
    Pergunta ao usuario quando ele deseja que o backup seja feito.

    - As opcoes sao: 'semanal', 'diário', 'mensal'.
    - A funcao verifica se o usuario digitou uma opcao valida e salva a configuracao.
    '''
    # Pergunta ao usuario quando ele deseja que o backup seja feito.
    # As opcoes sao: 'semanal', 'diário', 'mensal'.
    argendamento = str(input('Quando e que deve ser feito o backup (semanal, diário, mensal): '))

    # Verifica se o usuario digitou uma opcao valida.
    while argendamento not in ['semanal', 'diário', 'mensal'] or not argendamento:
        # Se a opcao for invalida, imprime um aviso.
        print('Valor Invalido')
        # Pergunta novamente ao usuario.
        argendamento = str(input('Quando e que deve ser feito o backup (semanal, diário, mensal): '))

    # Carrega a configuracao do programa.
    config = carregar_configuracao()

    # Substitui o agendamento na configuracao com o valor digitado pelo usuario.
    config["argendamento"] = argendamento

    # Salva a configuracao.
    guardar_configuracao(config)

    # Imprime o agendamento selecionado.
    print(f'Agendamento selecionado: {argendamento}')


def escolher_email_destinatario():
    """
    Pergunta ao usuario qual e o email que ele deseja que seja usado para enviar
    notificacoes de backup.

    - A funcao verifica se o usuario digitou um email valido e salva a configuracao.
    """
    # Pergunta ao usuario qual e o email que ele deseja que seja usado para enviar
    # notificacoes de backup.
    email = str(input('Email de notificação: '))

    # Verifica se o usuario digitou um email valido.
    while not email:
        # Se o email for invalido, imprime um aviso.
        print('Email Invalido')
        # Pergunta novamente ao usuario.
        email = str(input('Email de notificação: '))

    # Carrega a configuracao do programa.
    config = carregar_configuracao()

    # Substitui o email na configuracao com o valor digitado pelo usuario.
    config["email_destinatario"] = email

    # Salva a configuracao.
    guardar_configuracao(config)

    # Imprime o email selecionado.
    print(f'Email selecionado: {email}')
