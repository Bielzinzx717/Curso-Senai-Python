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





# import PyPDF2
# from PyPDF2.errors import PdfReadError

# def ler_pdf(caminho_arquivo):
#     try:
#         with open(caminho_arquivo, 'rb') as arquivo_pdf:
#             pdf = PyPDF2.PdReader(arquivo_pdf)
#             texto_primeira_pagina = pdf.pages[0].extract_text()
#             return texto_primeira_pagina
        

#     except FileNotFoundError:
#         print("Arquivo não encontrado")
#         return None
    
#     except PdfReadError:
#         print("erro ao ler o arquivo PDF ")
#         return None
    

# caminho = input("digite o caminho do arquivo:  ").strip('"')
# conteudo = ler_pdf(caminho)

# if  conteudo:
#     print("conteudo da primeira pagina")
#     print(conteudo)








# import pyautogui
# import time

# pyautogui.PAUSE = 1
# pyautogui.FAILSAFE =True

# pyautogui.press('win')
# pyautogui.write('chrome')
# pyautogui.press('enter')


# pyautogui.click(x=679, y=418)

# pyautogui.click(x=298, y=59)
# pyautogui.write('https://capitalapex.com.br')
# pyautogui.press('enter')





import requests


url = "https://jsonplaceholder.typicode.con/posts"


novo_post = {
    "title": "meu primeiro post via python" , 
    "body": "estou aprendendo sobre HTTP" ,
    "userld": 1
}


resposta = requests.post(url, json=novo_post)
print("status code:", resposta.status_code)
print("corpo da resposta:", resposta.json())
