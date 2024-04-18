import random, time
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
    # Caso seja Windows
    if name == 'nt':
        _ = system('cls')
    
    # Mac ou Linux
    else:
        _ = system('clear')
        
# Função principal do jogo
def game():
    
    limpa_tela()
    print("\nOlá, seja bem vindo(a) ao jogo da forca com Python!!")
    print("\nObs: Não use letras acentuadas")
    print("\nAdivinhe a palavra abaixo\n")
    
    # Lista de palavras para o jogo
    palavras = ['banana', 'limao', 'uva', 'abacate', 'pera', 'morango']
    
    # Escolher uma palavra automaticamente
    palavra = random.choice(palavras)
    
    # Loop para definir um tracinho para cada letra da palavra (List Comprehesion)
    letras_descobertas = ['_' for letra in palavra]
    
    # Numero de chances
    chances = 6
    
    # Lista para as letras erradas
    letras_erradas = []
    
    # Loop para acontecer enquanto o número de chances for maior que 0
    while chances > 0:
        
        print(" ".join(letras_descobertas))
        print("\nChances Restantes:", chances)
        print("Letras Erradas:", " ".join(letras_erradas))
        
        # Tentativas
        tentativa = input("\nDigite uma letra: ").lower()
        
        # Analisar a letra e ver se ela está na palavra
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else: 
            chances -= 1
            letras_erradas.append(tentativa)
            
        if '_' not in letras_descobertas:
            _ = system('cls')
            time.sleep(1)
            print("\nVocê venceu, a palavra era: ", palavra)
            repetir = int(input('Deseja continuar? DIGITE 1 PARA SIM E 2 PARA NÃO: '))
            if repetir == 1:
                game()
            else:
                print("\nVocê perdeu! A palavra era", palavra)
                repetir = int(input('Deseja continuar? DIGITE 1 PARA SIM E 2 PARA NÃO: '))
                if repetir == 1:
                    game()
                else:
                    return

game()
