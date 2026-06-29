import string
import secrets


def gerar_senha(comprimento=16):
    # Define os grupos de caracteres recomendados para segurança
    letras_minusculas = string.ascii_lowercase
    letras_maiusculas = string.ascii_uppercase
    digitos = string.digits
    especiais = string.punctuation

    # Garante que a senha terá pelo menos um caractere de cada tipo
    senha_obrigatoria = [
        secrets.choice(letras_minusculas),
        secrets.choice(letras_maiusculas),
        secrets.choice(digitos),
        secrets.choice(especiais),
    ]

    # Junta todos os caracteres possíveis para o restante da senha
    todos_os_caracteres = (
        letras_minusculas + letras_maiusculas + digitos + especiais
    )

    # Preenche o restante do comprimento escolhido de forma aleatória e segura
    caracteres_restantes = [
        secrets.choice(todos_os_caracteres)
        for _ in range(comprimento - len(senha_obrigatoria))
    ]

    # Combina os caracteres obrigatórios com os restantes
    lista_senha = senha_obrigatoria + caracteres_restantes

    # Embaralha a lista de forma criptograficamente segura
    secrets.SystemRandom().shuffle(lista_senha)

    # Transforma a lista de volta em uma string (texto)
    senha_final = "".join(lista_senha)

    return senha_final


# Execução do programa
if __name__ == "__main__":
    print("--- GERADOR DE SENHAS SEGURAS ---")
    tamanho = int(
        input("Digite o tamanho desejado para a senha (mínimo de 12 recomendado): ")
    )

    if tamanho < 8:
        print("Erro: O tamanho mínimo permitido por segurança é 8 caracteres.")
    else:
        senha_gerada = gerar_senha(tamanho)
        print(f"\nSua senha gerada com segurança é: {senha_gerada}")
       
