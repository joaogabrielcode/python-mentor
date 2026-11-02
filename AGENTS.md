# Idioma e registros da versão inicial

Na `main` e nas branches de estudo derivadas dela, os exercícios estão separados
em `exercises/pt/` e `exercises/en/`. Cada idioma tem 43 exercícios e registros
independentes. Use o idioma indicado pelo aluno; sem indicação, use o idioma da
conversa. Não some as duas traduções como se fossem 86 exercícios diferentes.

- Português: `README.md`, `PROGRESSO.md` e `PROGRESSO_PYTHON.md`.
- Inglês: `README.en.md`, `PROGRESS.en.md` e `MENTORING.en.md`.

Esses caminhos substituem as referências fixas de progresso na skill conforme
o idioma escolhido. Revise no idioma do aluno, preserve os resultados reais e
mantenha o ponto de retomada no histórico correspondente.
Para concluir em inglês, use `python3 progresso.py --language en complete caminho`;
para português, use `python3 progresso.py concluir caminho`.
O script também identifica o idioma pelo caminho do exercício quando a opção
`--language` não é informada. Ao fazer commit de uma conclusão, inclua somente
o exercício e os registros do idioma correspondente.

A `main` publicada deve continuar com enunciados sem soluções e progresso zerado.
Antes de salvar soluções de um novo estudante, crie ou use uma branch própria,
como `my-study`. A prática pessoal do autor permanece em `my-practice`, com a
estrutura original e exercícios em português. Evite trazer o progresso de uma
branch para outra. Não edite exercícios sem autorização explícita.

# Mentoria de Python

Ao receber “Terminei”, “Pronto”, “Concluí”, “Corrige meu exercício”,
“Revise meu código”, “Avalie meu código” ou outra expressão que indique um
pedido de revisão após finalizar ou ajustar um exercício, leia e aplique a skill
[python-mentor](.agents/skills/python-mentor/SKILL.md).
Isso inclui “Fiz” e “E agora?” quando o contexto indicar uma nova revisão.
Use a skill também para “marcar como concluído” e para confirmar uma conclusão.

A skill orienta a avaliação no nível Trainee, o formato da revisão com nota,
as pistas graduais e o registro breve em `PROGRESSO_PYTHON.md`.
Nunca altere os exercícios sem autorização explícita do usuário.
Mantenha as regras de acompanhamento e orientação abaixo.

# Acompanhamento dos exercícios

Quando verificar que a solução está correta, informe a aprovação e pergunte se
o usuário deseja marcá-la como concluída, explicando que isso inclui commit e
push. “Terminei”, “Pronto” e “Concluí” iniciam a revisão, sem concluir automaticamente.

Após a confirmação, marque o exercício aprovado como concluído executando:

```sh
python3 progresso.py concluir caminho/do/exercicio.py
```

O comando atualiza PROGRESSO.md e README.md. Atualize também PROGRESSO_PYTHON.md,
crie um commit Conventional Commits em inglês com resumo real do aprendizado
e faça push, seguindo o escopo e as verificações da skill.

O pedido direto “marcar como concluído” autoriza esse fluxo sem segunda
confirmação, desde que o exercício esteja aprovado. Não inclua mudanças alheias
no commit nem altere a solução sem autorização explícita.

Consulte o exercício atual em PROGRESSO.md. Dúvidas sem indicação explícita de
outro exercício se referem a ele. Ao concluir um exercício, considere que o usuário
vai começar o próximo pendente na ordem do README. O script progresso.py atualiza
esse registro automaticamente; informe qual é o próximo exercício ao usuário.

# Títulos dos commits

Nos próximos commits de exercícios, use Conventional Commits em inglês com
um título que descreva a ação concreta implementada e seu resultado. Exemplo:
`feat(variables): calculate sales bonuses and remaining revenue`.
Escreva o escopo, o título e o corpo do commit em inglês; preserve os caminhos
reais dos arquivos citados.
Evite títulos genéricos como “registrar exercício” ou “concluir exercício”.
Descreva os conceitos praticados no corpo do commit, conforme o código real.
Para arquivos que contêm apenas enunciados, informe somente a adição do enunciado.
Esta preferência de título prevalece sobre o modelo de título da skill
`python-mentor`.

# Orientação durante o aprendizado

Quando o usuário disser que não está entendendo ou que está com dificuldade,
não apresente imediatamente a resposta pronta nem implemente a solução por ele.
Explique o conceito com linguagem simples, exemplos diferentes do exercício e
pistas graduais. Ajude-o a dividir o problema em pequenos passos e incentive uma
tentativa própria antes de avançar. Apresente a solução completa apenas se ele
a pedir explicitamente.

# Branches de estudo

A branch `main` é a versão inicial para estudantes: preserve os enunciados e o
progresso zerado. A branch `my-practice` guarda as soluções e o histórico pessoal
do autor. Continue os exercícios pessoais nessa branch e publique as conclusões
nela; não leve as respostas para `main`.

Quem clonar para estudar deve criar uma branch própria, como `my-study`, e
registrar nela suas soluções e revisões. Antes de concluir e publicar exercícios,
confira a branch ativa e o upstream. A manutenção de enunciados e orientações
compartilhados pode ser feita nas duas versões sem copiar respostas ou progresso
pessoal para a versão inicial.
