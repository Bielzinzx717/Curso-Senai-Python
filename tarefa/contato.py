class contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        


    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"
    


class Agenda:
    def __init__ (self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print("contato adicionado com sucesso!")

    def listar_contato(self):
        if not self.contatos:
            print("agenda vazia.")
        
        else:
            for i, contato in enumerate(self.contatos, 1):
                print(f"{i}. {contato}")


    def editar_contato(self, indice, novo_nome, novo_telefone, novo_email):
        if 0 <= indice < len(self.contatos):
            self.contatos[indice].nome = novo_nome
            self.contatos[indice].telefone = novo_telefone
            self.contatos[indice].email = novo_email
            print("contato atualizado com sucesso!")
        
        else:
            print("indice invalido.")

    

    def deletar_contato(self, indice):
        if 0 <= indice <len(self.contatos):
            removido = self.contatos.pop(indice)
            print(f"contato '{removido.nome}' removido com sucesso!")

        else:
            print("indice invalido.")