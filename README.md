# 🎯 Jogo da Forca em Python

Um jogo clássico da forca feito em Python, onde o jogador tenta adivinhar o nome de uma fruta sorteada. O projeto foi desenvolvido com foco em aprendizado de lógica de programação, manipulação de arquivos e testes automatizados.
Ensina conceitos básicos de programação de forma divertida: controle de fluxo, listas, strings e entrada de dados. 
---

## 🚀 Funcionalidades

- ✅ Sorteio aleatório de uma palavra do arquivo `palavras.txt`
- ✅ Exibição da palavra com letras ocultas
- ✅ Contagem de tentativas restantes
- ✅ Validação de letras já digitadas
- ✅ Mensagens de vitória ou derrota
- ✅ Testes unitários com `unittest`

---

## 🧰 Tecnologias utilizadas

- Python 3.12
- `random` (biblioteca padrão)
- `unittest` para testes automatizados
- VS Code + Terminal integrado

---

## ⚙ Como rodar o projeto

1. Clone o repositório:
git clone https://github.com/Rw110299/jogo-da-forca.git
cd jogo-da-forca
2. rode o jogo
 python cod/forc.py


# 🧪 Executar os testes
1. Vá até a raiz do projeto:
 
  python -m unittest discover tests

os testes garantem que a logica do jogo e a escolha de palavras funcionam corretamente

## ▶️ Como Jogar

1. Execute o script principal (ex: via terminal):
   python cod/forc.py

# 👤 Autor
Richard Souza

GitHub: @Rw110299

Email: richardwillianmirandadesouza@gmail.com

# 📄 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE.

# 📂 Estrutura do Projeto

jogo_da_forca/
│
├── cod/                    # Código-fonte
│   ├── forc.py
│   └── __init__.py
│
├── tests/                  # Testes automatizados
│   ├── test_forca.py
│   ├── palavras.txt
│   └── __init__.py
│
├── docs/                   # Documentação
│   └── README.md
│
├── .github/                # Configuração do GitHub Actions
│   └── workflows/
│       └── python.yml
│
├── README.md
└── pyproject.toml          # Configuração do projeto (ou requirements.txt)
