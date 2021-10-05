import os
import datetime
import configparser

# Leitura do arquivo de configuracao
cfg = configparser.ConfigParser()
cfg.read("config.ini")
caminhos = cfg.get("armazenamento", "caminhos")
caminhos = caminhos.split(";")

total_mega_bytes = 0

for caminho in caminhos:
    if os.path.isdir(caminho):
        for arquivo in os.listdir(caminho):
            if(arquivo.find("server-") >= 0 and (arquivo.find(".log") >= 0 or arquivo.find(".zip") >= 0)):
                caminho_arquivo = os.path.join(caminho, arquivo)
                tamanho_mega_bytes = os.path.getsize(caminho_arquivo) / (1024 ** 2)
                total_mega_bytes += tamanho_mega_bytes
                data = datetime.datetime.now().strftime("%Y-%m-%d")
                print(data + ";" + caminho_arquivo + ";" + str(round(tamanho_mega_bytes, 2)) + " MB")
                os.remove(caminho_arquivo)

print("Tamanho total em MB dos arquivos excluidos: " + str(round(total_mega_bytes, 2)))