import os
import random

def carregar_palavras(caminho=None):
    if caminho is None:
        # Caminho absoluto para o arquivo 'palavras.txt' dentro da pasta 'tests'
        caminho = os.path.join(os.path.dirname(__file__), '..', 'tests', 'palavras.txt')
        caminho = os.path.abspath(caminho)

    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return [linha.strip() for linha in arquivo if linha.strip()]

def escolher_palavra(lista_palavras):
    return random.choice(lista_palavras).lower()

def exibir_palavra(palavra, letras_acertadas):
    return ''.join(letra if letra in letras_acertadas else '_' for letra in palavra)

def jogar():
    lista_palavras = carregar_palavras()
    palavra = escolher_palavra(lista_palavras)
    letras_acertadas = set()
    letras_erradas = set()
    tentativas = 6  

    print("🎮 Bem-vindo ao Jogo da Forca!")

    while tentativas > 0:
        print(f"\nPalavra: {exibir_palavra(palavra, letras_acertadas)}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Erros: {', '.join(sorted(letras_erradas))}")

        if set(palavra) <= letras_acertadas:
            print(f"🎉 Parabéns! Você acertou a palavra: {palavra}")
            return

        letra = input("Digite uma letra: ").lower() 

        if len(letra) != 1 or not letra.isalpha():
            print("⚠️ Por favor, digite apenas uma letra.")
            continue

        if letra in letras_acertadas or letra in letras_erradas:
            print("⚠️ Você já tentou essa letra.")
            continue

        if letra in palavra:
            letras_acertadas.add(letra)
            print(f"✅ Boa! A letra '{letra}' está na palavra.")
        else:
            letras_erradas.add(letra)
            tentativas -= 1
            print(f"❌ A letra '{letra}' não está na palavra.")

    print(f"\n💀 Você perdeu! A palavra era: {palavra}")

if __name__ == "__main__":
    jogar()
