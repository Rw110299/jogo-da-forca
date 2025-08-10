# Jogo da Forca

## 🎯 Objetivo
Adivinhar a palavra oculta chutando uma letra por vez, antes de atingir o número máximo de erros.

---

## 📜 Regras
- O jogador vê apenas os espaços e letras já acertadas.
- A cada letra errada, perde uma "vida".
- O jogo termina ao adivinhar toda a palavra ou ao atingir o número máximo de erros.

---

## 🕹️ Como jogar

### Terminal
Execute o arquivo principal:
```bash
python cod/forc.py

você verá algo como: 
em yaml
Palavra: _ _ _ _ _
Tentativas restantes: 6
Digite uma letra: 
# teste
para rodar os testes: 
python -m unittest discover tests/

#📚 Exemplos de Palavras
Veja o arquivo tests/palavras.txt para a lista de palavras usadas.

#🤝 Contribuindo
Faça um fork

Crie uma branch: git checkout -b minha-feature

Commit: git commit -m "Nova feature"

Push: git push origin minha-feature

Abra um Pull Request

---

### ✅ **3. Adicionar ao repositório e commitar**

```bash
git add docs/README.md
git commit -m "Adiciona documentação inicial do jogo da forca"
git push

#✅ 4. Alternativa: Usar o GitHub Wiki (opcional)
Se quiser usar o GitHub Wiki:

Vá até a aba "Wiki" do repositório no GitHub.

Clique em "Create the first page".

Escreva a documentação lá, em Markdown também.

