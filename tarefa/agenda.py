from contato import contato, Agenda


def menu():
    agenda= Agenda()



    while True:
        print("\n-----AGENDA-----")
        print("1. Adicionar contato")
        print("2. Limpar contatos")
        print("3. Editar contato")
        print("4. Deletar contato")
        print("5. Sair")


        escolha = input("escolha uma opção:  ")


        if escolha == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            contato = contato(nome, telefone, email)
            Agenda.adicionar_contato(contato)


        elif escolha == "2":
            Agenda.listar_contatos()
        
        elif escolha == "3":
            Agenda.listar_contatos()
            try:
                indice = int(input("Numero do contato a editar:  ")) -1
                nome = input("Novo nome:  ")
                telefone = input("Novo telefone:  ")
                email = input("Novo email:  ")
                Agenda.editar_contato(indice,nome,telefone,email)
            except ValueError:
                print("Entrada invalida.")


        elif escolha == "4":
            Agenda.listar_contatos()
            try:
                indice = int(input("Numero do contato a deletar: ")) -1
                Agenda.deletar_contato(indice)
            except ValueError:
                print("Entrada invalida.")


        elif escolha == "5":
            print("saindo da agenda...")
            break

        else:
            print("Opção invalida.")



if __name__ == "__main__":
    menu()