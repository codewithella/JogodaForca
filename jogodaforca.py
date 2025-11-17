import random 

def escolherpalavra(lista):
    palavra = [ "lua", "banana", "caneca", "morango", "pato", "uva", "sujo",
    "python", "taylor", "swift", "amora", "coelho", "chuva", "girassol",
    "computador", "lugar", "teclado", "janela", "cadeira", "caneta",
    "livro", "escola", "professor", "fisica", "cidade", "paisagem",
    "amar", "floresta", "paz", "familia"]

    return random.choice(palavra)


def mascara(palavra):
    return "-" * len(palavra)

def atualizar_mascara(palavra, mascara, letra):
    return "".join(
        letra if palavra[i] == letra else mascara[i]
        for i in range(len(palavra)) #ve se a letra ta na posição certa
    )

def jogar():
    palavra = escolherpalavra([])
    estado = mascara(palavra)
    tentativas = 8 
    letras_tentadas = set()

    print("Bem-vindo ao Jogo da Forca!")

    while tentativas > 0 and "-" in estado:
        print(f"\nTentativas restantes: {tentativas}")

        if letras_tentadas:
            print("Letras tentadas:", " ".join(sorted(letras_tentadas)))
        else:
            print("Letras tentadas: -") #mostra as letras tentadas 

       
        print("Palavra:", " ".join(estado))

        tentativa = input("Digite uma letra: ").strip().lower() #padroniza as tentativas

        if not tentativa or not tentativa.isalpha(): #se não for letra 
            print("Inválido, tente novamente.")
            continue

        if len(tentativa) != 1: #se tentarem colocar uma palavra inteira ou mais que uma letra
            print("Digite apenas uma letra!")
            continue
        
        letra = tentativa
        if letra in letras_tentadas:    
            print("Você já tentou essa letra, tente outra.")
            continue
        letras_tentadas.add(letra)
        if letra in palavra:
            estado = atualizar_mascara(palavra, estado, letra) #atualiza a mascara revelando a letra certa
            print("\nParabéns! Letra correta.")
            tentativas -=1
        else: 
            tentativas -= 1
            print("\nLetra incorreta :(")
    if "-" not in estado:
        print("Parabéns! Você venceu!")
        print("\nA palavra era:", palavra)
    else:
        print("Você foi enforcado.")
        print("\nA palavra correta era:", palavra)


if __name__ == "__main__":
    jogar()