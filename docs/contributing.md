# 🤝 Guia de Contribuição

Obrigado por querer contribuir com este projeto! Este documento orienta como você pode participar de forma organizada e produtiva.

---

## 📋 Regras Básicas

- Seja respeitoso e claro na comunicação.
- Sempre abra uma **issue** antes de grandes mudanças.
- Siga os padrões abaixo para manter o código e o histórico limpos.

---

## 🌿 Fluxo de Trabalho com Git

1. **Fork** do repositório.
2. Clone o seu fork:
   
   git clone https://github.com/Rw110299/jogo-da-forca

   Crie uma branch para a sua contribuição:

git checkout -b feat/adiciona-nova-palavra

Faça suas alterações.

Adicione e commit suas mudanças:


git add .
git commit -m "feat: adiciona verificação de letras repetidas"
Suba para seu fork:


git push origin feat/adiciona-nova-palavra
Abra um Pull Request.

# 🌳 Convenção de Nomes de Branches

Prefixo	Descrição
feat/	Nova funcionalidade
fix/	Correção de bug
docs/	Atualização de documentação
test/	Testes
chore/	Tarefas de manutenção

Exemplos:

feat/adiciona-regras-jogo

fix/bug-exibir-palavra

docs/update-readme

# ✍️ Padrão de Commits (Conventional Commits)
Use a seguinte estrutura:

bash
Copiar código
<tipo>: <mensagem curta no imperativo>
Tipos válidos:
feat: nova funcionalidade

fix: correção de bug

docs: documentação

test: testes

refactor: refatoração sem alterar comportamento

chore: tarefas sem impacto no código (ex: CI)

Exemplos:

feat: adiciona verificação de letras repetidas

fix: corrige erro ao exibir palavra

docs: adiciona instruções de execução

test: adiciona teste para escolher_palavra

# 🧪 Rodando os Testes
Antes de enviar seu PR, execute os testes:

bash
Copiar código
python -m unittest discover -s tests

# 🔁 CI/CD
Pull requests acionam automaticamente os testes via GitHub Actions.

# 💬 Dúvidas?
Abra uma issue ou fale nos comentários do Pull Request.

Obrigado por contribuir! 🎉



