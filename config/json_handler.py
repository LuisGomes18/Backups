from json import load, dump, JSONDecodeError


def carregar_configuracao():
    '''
    Carrega a configuração do programa.
    
    - Tenta abrir o arquivo 'config/config.json' em modo de leitura.
    - Se o arquivo não for encontrado, lança um erro de FileNotFoundError.
    - Se o arquivo for encontrado, mas o seu conteúdo for inválido (ou seja, não for um JSON), lança um erro de JSONDecodeError.
    - Se o arquivo for encontrado e o seu conteúdo for válido, o seu conteúdo é lido e retornado.
    - Se ocorrer qualquer outro erro inesperado, lança um erro de Exception.
    '''
    try:
        with open('config/config.json', 'r', encoding='utf-8') as config:
            return load(config)
    except FileNotFoundError:
        raise FileNotFoundError('Arquivo de configuração não encontrado!')
    except JSONDecodeError:
        raise JSONDecodeError('Arquivo de configuração inválido!')
    except Exception as error:
        raise Exception(f'Erro inesperado ao carregar o arquivo de configuração: {error}')


def guardar_configuracao(config):
    '''
    Guarda a configuração do programa.
    
    - Tenta abrir o arquivo 'config/config.json' em modo de escrita.
    - Se o arquivo não for encontrado, lança um erro de FileNotFoundError.
    - Se o arquivo for encontrado, o seu conteúdo é substituído com o conteúdo do parâmetro 'config'.
    - Se ocorrer qualquer outro erro inesperado, lança um erro de Exception.
    '''
    try:
        with open('config/config.json', 'w', encoding='utf-8') as config_file:
            dump(config, config_file, ensure_ascii=False, indent=4)
    except Exception as error:
        raise Exception(f'Erro inesperado ao salvar o arquivo de configuração: {error}')
