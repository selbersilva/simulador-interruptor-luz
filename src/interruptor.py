def acender_luz():
    print("A luz está ACESA.")

def apagar_luz():
    print("A luz está APAGADA.")

def mostrar_menu():
    print("\nDigite '1' para ACENDER a luz.")
    print("Digite '2' para APAGAR a luz.")
    print("Digite '0' para SAIR.")

def main():
    estado_luz = False  # False significa que a luz está apagada, True significa que está acesa

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            estado_luz = True
            acender_luz()
        elif escolha == '2':
            estado_luz = False
            apagar_luz()
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
