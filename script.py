import os
import shutil

caminho = input("Digite o caminho: ")

diretorio_pdf = caminho


for filename in os.listdir(diretorio_pdf):
    if filename.endswith('.pdf'):

        nome_arquivo = os.path.splitext(filename)[0]

        nova_pasta = os.path.join(diretorio_pdf, nome_arquivo)

        if not os.path.exists(nova_pasta):
            os.makedirs(nova_pasta)

        shutil.move(os.path.join(diretorio_pdf, filename), nova_pasta)
