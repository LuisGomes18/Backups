import os
import zipfile
from datetime import datetime
from config.json_handler import carregar_configuracao, guardar_configuracao
from config.send_email import mandar_email


def backup_manual():
    config = carregar_configuracao()
    pasta_destino = config["pasta_destino"]
    if not os.path.exists(pasta_destino):
        raise ValueError(f"A pasta de destino {pasta_destino} não existe.")
    if not pasta_destino:
        raise ValueError(f"A pasta de destino {pasta_destino} não pode estar vazia.")

    pastas_backup = config["pastas_backup"]
    if not pastas_backup:
        raise ValueError(f"A pasta de destino {pasta_destino} não pode estar vazia.")
    for pasta in pastas_backup:
        if not os.path.exists(pasta):
            raise ValueError(f"A pasta {pasta} não existe.")

    data_hora = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    nome_arquivo = os.path.join(pasta_destino, f"Backup-{data_hora}.zip")

    mandar_email("comecar")
    with zipfile.ZipFile(nome_arquivo, "w", zipfile.ZIP_DEFLATED) as zipf:
        for pasta in pastas_backup:
            for raiz, diretorios, arquivos in os.walk(pasta):
                for arquivo in arquivos:
                    caminho_arquivo = os.path.join(raiz, arquivo)
                    zipf.write(caminho_arquivo, os.path.relpath(caminho_arquivo, pasta))

    config["ultimo_backup_manual"] = data_hora
    guardar_configuracao(config)
    mandar_email("finalizar")
    print(f"Backup concluído: {nome_arquivo}")
