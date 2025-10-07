# nome = input("digite seu nome: ")
# idade = input("digite sua idade: ")
# with open("usuarios.txt", "a") as arq:
#     arq.write(f"{nome};{idade}\n")
    





# import requests

# resposta = requests.get("https://jsonplaceholder.typicode.com/users/3")

# print("Status code:", resposta.status_code)
# print("\n Cabeçalhos: ", resposta.content)
# print("\nBody: ", resposta.json())



import requests

url = "https://httpbin.org/post"
dados = {"usuario": "marcelo", "curso": "backend Python"}

resposta = requests.post(url, json=dados)

print("metodo:" , resposta.request.method)
print("codigo de status: " , resposta.status_code)
print("corpo: " , resposta.json())