import os

def carregar_inicio():
    diretorio_projeto = os.getcwd()
    diretorio_templates = os.path.join(diretorio_projeto, 'templates')
    try:
        with open(f'{diretorio_templates}/inicio_backup.html', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError('Arquivo de configuração nao encontrado!')
    except Exception as error:
        raise Exception(f'Erro inesperado ao carregar o arquivo de configuração: {error}')


def carregar_finalizar():
    diretorio_projeto = os.getcwd()
    diretorio_templates = os.path.join(diretorio_projeto, 'templates')
    try:
        with open(f'{diretorio_templates}/finalizar_backup.html', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError('Arquivo de configuração nao encontrado!')
    except Exception as error:
        raise Exception(f'Erro inesperado ao carregar o arquivo de configuração: {error}')


def escolher_template_email(estado):
    if not estado or estado not in ['comecar', 'finalizar']:
        raise ValueError(f'Estado inválido: {estado}')

    if estado == 'comecar':
        return carregar_inicio()
    else:
        return carregar_finalizar()
