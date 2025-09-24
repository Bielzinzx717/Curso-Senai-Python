# import math

# print(math.sqrt(16))


# import requests
# resposta = requests.get("https://api.github.com")
# print(resposta.status_code)


# from translate import Translator
# text = input("digite o texto a ser traduzido: ")
# Translator = Translator(from_lang="english", to_lang="pt-br")   # to com erro no translate
# result = Translator.translate(text)
# print(result)





import PyPDF2
from PyPDF2.errors import PdfReadError

def ler_pdf(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'rb') as arquivo_pdf:
            pdf = PyPDF2.PdReader(arquivo_pdf)
            texto_primeira_pagina = pdf.pages[0].extract_text()
            return texto_primeira_pagina
        

    except FileNotFoundError:
        print("Arquivo não encontrado")
        return None
    
    except PdfReadError:
        print("erro ao ler o arquivo PDF ")
        return None