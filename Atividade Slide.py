def inserir_item(lista):
    item = input("Digite o item a ser inserido: ")
    lista.append(item)
    print("Item inserido com sucesso!")

def apagar_item(lista):
    item = input("Digite o item a ser apagado: ")
    if item in lista:
        lista.remove(item)
        print("Item apagado com sucesso!")
    else:
        print("Item não encontrado na lista.")

def listar_itens(lista):
    print("Itens na lista:")
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item}")

def editar_item(lista):
    item_antigo = input("Digite o item a ser editado: ")
    if item_antigo in lista:
        index = lista.index(item_antigo)
        novo_item = input("Digite o novo valor para o item: ")
        lista[index] = novo_item
        print("Item editado com sucesso!")
    else:
        print("Item não encontrado na lista.")

def main():
    lista_de_itens = []
    
    while True:
        opcao = input("[i]nserir [a]pagar [l]istar [e]ditar [s]air: ").lower()

        if opcao == 'i':
            inserir_item(lista_de_itens)
        elif opcao == 'a':
            apagar_item(lista_de_itens)
        elif opcao == 'l':
            listar_itens(lista_de_itens)
        elif opcao == 'e':
            editar_item(lista_de_itens)
        elif opcao == 's':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()