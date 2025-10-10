# nome = input("digite seu nome: ")
# idade = input("digite sua idade: ")
# with open("usuarios.txt", "a") as arq:
#     arq.write(f"{nome};{idade}\n")
    





# import requests

# resposta = requests.get("https://jsonplaceholder.typicode.com/users/3")

# print("Status code:", resposta.status_code)
# print("\n Cabeçalhos: ", resposta.content)
# print("\nBody: ", resposta.json())



# import requests

# url = "https://httpbin.org/post"
# dados = {"usuario": "marcelo", "curso": "backend Python"}

# resposta = requests.post(url, json=dados)

# print("metodo:" , resposta.request.method)
# print("codigo de status: " , resposta.status_code)
# print("corpo: " , resposta.json())


# import requests


# url = "https://jsonplaceholder.typicode.com/posts"


# novo_post = {
#     "title": "meu primeiro post via python" , 
#     "body": "estou aprendendo sobre HTTP" ,
#     "userld": 1
# }


# resposta = requests.post(url, json=novo_post)
# print("status code:", resposta.status_code)
# print("corpo da resposta:", resposta.json())




# import requests

# url = "https://httpbin.org/post"


# Post = {
#     "Nome": "Gabriel",
#     "Cidade": "Mogi Guaçu",
#     "Curso": "Back-end",
#     "Idade": "17",

# }

# resposta = requests.post(url, json=Post)

# print("Metodo:", resposta.request.method)
# print("status code:", resposta.status_code)
# print("Conteudo:", resposta.json())
# print("URL:", resposta.url)



# import requests

# url = "https://jsonplaceholder.typicode.com/posts/1"


# dados_atualizados = {
#     "id": 1,
#     "title": "titulo att",
#     "body": "body att",
#     "userId": 1

# }



# respostas = requests.put(url, json=dados_atualizados)


# print("Status code:", respostas.status_code)
# print("Corpo da resposta:", respostas.json())





# import requests


# URL = "https://httpbin.org/put"

# novo_dados = { 
#     "id": 7,
#     "nome": "Gabriel",
#     "curso": "back-end",

# }
# respostas = requests.put(URL, json=novo_dados)


# print("Metodo:", respostas.request.method)
# print("Status Code:", respostas.status_code)
# print("Corpo:", respostas.json())




# import requests


# URL = "https://jsonplaceholder.typicode.com/posts/1"

# resposta = requests.delete(URL)

# print("Status Code:", resposta.status_code)
# print("Corpo:", resposta.text)



# import requests


# url = "https://jsonplaceholder.typicode.com/posts/1"

# dados_parciais = {
#     "title": "titulo parcialment atualizado"
# }


# resposta = requests.patch(url, json=dados_parciais)

# print("status Code:", resposta.status_code)
# print("Corpo da resposta:", resposta.json())



############################################################################################







# import json

# texto = '{"curso": "backend", "modulo": "HTTP"}'
# dados = json.loads(texto)
# print(dados["curso"])


# novo_json = json.dumps(dados, indent=2)
# print(novo_json)



# import requests


# url = "https://httpbin.org/bearer"


# token = "abcd1234"


# Headers = {
#     "Authorization":  f"Bearer {token}"
# }


# resposta = requests.get(url, headers=Headers)


# print("Status Code:", resposta.status_code)
# print("Corpo da resposta:, resposta.text")
# print(resposta.json())






# import requests

# url = "https://httpbin.org/bearer"
# token = "abcd1234"

# headers = {
#     "Authorization": f"Bearer {token}"
# }

                                                                    #chat gpt
# resposta = requests.get(url, headers=headers)

# print("Status Code:", resposta.status_code)
# print("Corpo da resposta:", resposta.text)

# try:
#     print("JSON:", resposta.json())
# except ValueError:
#     print("Erro: a resposta não está em formato JSON válido.")





from flask import Flask
import os

app = Flask(__name__)
@app.route("/")
def home():
    soma = 30 + 57
    mult = 15 * 7
    div = 25 / 4
    resto = 37 % 5
    potencia = 6 ** 4

    resposta = f"""
    <h1> Operadores Aritmeticos<h1>
    <ul>
        <li> 1. calcule a soma de 30 + 57: {soma}</li>
        <li> 2. multiplique 15 por 7: {mult}</li>
        <li> 3. divida 25 por 4 e veja o resultado: {div}</li>
        <li> 4. descubra o resto da divisao de 37 por 5: {resto}</li>
        <li> 5. ele 6 a potencia de 4: {potencia}</li>

    </ul>
    """

    return resposta

if __name__ == "__main__":
    app.run(debug=True)







