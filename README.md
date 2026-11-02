# Python Mentor

Português | [English](README.en.md)

Criei o Python Mentor para aprender Python do zero, resolvendo exercícios e
usando IA como mentora durante os estudos. Quero desenvolver uma base na
linguagem e aprender a resolver problemas por conta própria, até começar a
estudar Django como meu primeiro framework web em Python.

Os exercícios trabalham situações como calcular comissões, atualizar estoques
e organizar dados de clientes. Este repositório guarda minhas tentativas, as
soluções e o histórico do que aprendi. Vou acrescentar novos exercícios conforme
os estudos avançarem.

## Learning path

Os assuntos seguem esta ordem:

| Pasta | O que praticar |
| --- | --- |
| [01_variables](01_variables/) | Variáveis, operações aritméticas, porcentagens e comparações |
| [02_strings](02_strings/) | Formatação, métodos de texto e fatiamento |
| [03_inputs](03_inputs/) | Entrada de dados e conversão de tipos |
| [04_lists](04_lists/) | Índices, alterações, ordenação e cálculos com listas |
| [05_conditionals](05_conditionals/) | Decisões com `if`, `elif`, `else` e operadores lógicos |
| [06_dictionaries](06_dictionaries/) | Chaves, valores, consultas e atualização de dados |
| [07_for_loops](07_for_loops/) | Repetições, filtros e acumuladores |
| [08_functions](08_functions/) | Parâmetros, retorno e reutilização de código |
| [09_tuples](09_tuples/) | Tuplas, desempacotamento e retornos com múltiplos valores |

Os nomes das pastas e os títulos das seções estão em inglês. Os exercícios
pendentes mantêm os enunciados em português para a leitura inicial. Ao publicar
um exercício resolvido, traduzo o enunciado, os comentários, as variáveis e
as mensagens para inglês. Os nomes dos arquivos e os registros de estudo
continuam em português.

## Choosing a branch

Este repositório tem duas versões:

| Branch | Conteúdo |
| --- | --- |
| `main` | Todos os enunciados, espaço para resolver e progresso zerado |
| `my-practice` | Minhas soluções, revisões e progresso pessoal |

Para começar do zero, acesse a [branch main](https://github.com/joaogabrielcode/python-mentor/tree/main).
Ela contém as versões `exercises/pt/` e `exercises/en/`, com enunciados e
progresso separados por idioma. Siga o guia dessa branch para clonar a versão
inicial ou baixar seu ZIP. O comando abaixo clona minha versão de prática.
As soluções pessoais continuam públicas na branch `my-practice`.

Se quiser salvar e publicar sua própria evolução, faça um fork do repositório
e use o endereço do seu fork no clone. Depois de clonar, crie sua branch de estudo:

```sh
git switch -c my-study
```

Para acompanhar minhas soluções, acesse a
[branch my-practice](https://github.com/joaogabrielcode/python-mentor/tree/my-practice).
Esta branch mantém minha prática nas pastas numeradas da raiz, com seu próprio
checklist e histórico. Os exercícios resolvidos são publicados em inglês; os
pendentes continuam em português até o momento do commit.

## Getting started

Você precisa de Python 3, Git para clonar o repositório, um editor de texto ou
código e um terminal.
Os exercícios atuais usam recursos da própria linguagem, sem bibliotecas
externas para instalar.

Clone o repositório e entre na pasta:

```sh
git clone --single-branch --branch my-practice https://github.com/joaogabrielcode/python-mentor.git
cd python-mentor
```

Confira se o Python está disponível:

```sh
python3 --version
```

Se a instalação do Python 3 usar o comando `python`, substitua `python3` por
`python` nos exemplos abaixo.

## Running an exercise

Abra um arquivo e leia os comentários iniciais: eles contêm o enunciado e os
dados necessários. Nos pendentes, escreva sua tentativa abaixo de
`# Sua solução:`. Os exercícios já publicados usam `# Your solution:`.
Depois, a partir da raiz do projeto, execute o arquivo:

```sh
python3 01_variables/ex01_bonus_vendas.py
```

Nos exercícios com `input`, o programa espera que você digite os dados no
terminal. Para praticar entrada de valores, por exemplo:

```sh
python3 03_inputs/ex03_faturamento_lojas.py
```

Siga o formato pedido no enunciado. Nesse exercício, use ponto para valores
decimais, como `1500.50`. Outros exercícios trabalham especificamente o
tratamento de valores com vírgula e símbolo monetário.

Compare o resultado com o que você calculou antes de executar. Se aparecer um
erro, observe a linha indicada e tente entender a causa antes de alterar o código.

## Using AI as a mentor

Você pode estudar com Codex, Claude ou outra ferramenta de IA que consiga
receber as orientações e o contexto do projeto. O papel da IA é explicar
conceitos, ajudar a dividir o problema em passos e revisar suas tentativas.

### Load the mentoring instructions

As regras de estudo estão em [AGENTS.md](AGENTS.md). A skill
[python-mentor](.agents/skills/python-mentor/SKILL.md) detalha a revisão no nível
iniciante, as pistas graduais e o registro do aprendizado.

Em uma ferramenta com acesso aos arquivos, abra a pasta do projeto e peça que
ela leia esses documentos antes de começar. O carregamento de instruções e
skills depende da ferramenta. Em um chat sem acesso ao repositório, cole ou
anexe o conteúdo dos dois documentos, o enunciado e sua tentativa.

Você pode iniciar a sessão assim:

```text
Quero estudar Python com você como mentor.
Leia AGENTS.md e .agents/skills/python-mentor/SKILL.md.
Consulte PROGRESSO.md e PROGRESSO_PYTHON.md para identificar onde parei.
Explique no nível iniciante e me ajude com pistas graduais.
Deixe que eu tente resolver antes de apresentar uma solução completa.
Peça minha autorização antes de alterar um exercício.
```

Se a IA não conseguir acessar um arquivo, forneça seu conteúdo. Para revisar
uma tentativa, ela precisa conhecer tanto o enunciado quanto o código atual.

### Ask for help while solving

Comece com uma tentativa própria. Quando travar, mostre o trecho e diga qual
parte do raciocínio não ficou clara. Por exemplo:

```text
Não entendi quando usar divisão inteira e resto da divisão.
Explique com um exemplo diferente do exercício e depois me dê uma pista
para que eu tente continuar sozinho.
```

Você também pode pedir que a IA explique uma mensagem de erro ou ajude a
escolher entradas para conferir seu resultado. Na mentoria definida pelo
projeto, a solução completa é apresentada quando você a pede explicitamente.

### Request a review

Depois de executar sua tentativa, peça a revisão indicando o arquivo:

```text
Terminei 08_functions/ex01_padronizar_produtos.py.
Revise meu código seguindo a skill python-mentor.
```

A revisão verifica o enunciado e a lógica e, quando possível, executa a solução.
Ela informa o resultado, uma nota de 0 a 10, os acertos e o que precisa melhorar.
Se houver correções necessárias, faça uma nova tentativa e peça outra revisão.
O histórico fica em [PROGRESSO_PYTHON.md](PROGRESSO_PYTHON.md).

Dizer “Terminei” solicita revisão. Depois da aprovação, a IA pergunta se você
quer marcar o exercício como concluído, explicando que isso inclui commit e
push. Ao confirmar, você autoriza esse fluxo para o exercício aprovado.
Um pedido direto para marcar um exercício aprovado como concluído também
autoriza esse fluxo.

Uma IA com acesso apenas ao chat pode orientar e revisar o conteúdo enviado.
Para editar os registros ou executar Git, a ferramenta precisa ter acesso aos
arquivos e aos comandos; caso contrário, essas etapas ficam com você.

## Tracking progress

| Arquivo | Para que serve |
| --- | --- |
| [README.md](README.md) | Apresentação e checklist dos exercícios |
| [README.en.md](README.en.md) | Versão em inglês deste guia |
| [PROGRESSO.md](PROGRESSO.md) | Resumo das conclusões e próximo exercício pendente |
| [PROGRESSO_PYTHON.md](PROGRESSO_PYTHON.md) | Revisões, dificuldades e ponto de retomada |
| [progresso.py](progresso.py) | Atualização do checklist e dos totais |

O checklist no final deste README é compartilhado pelas duas versões do guia.
Na `main`, o checklist começa zerado. Na `my-practice`, os registros refletem
meu progresso pessoal. Na sua branch de estudo, você acompanha suas próprias
soluções e revisões.

Para sincronizar os totais, sem concluir outro exercício:

```sh
python3 progresso.py
```

Depois de revisar e aprovar uma solução, registre sua conclusão. Exemplo para
o exercício de padronização de produtos, somente quando ele estiver aprovado:

```sh
python3 progresso.py concluir 08_functions/ex01_padronizar_produtos.py
```

Para voltar esse exercício a pendente:

```sh
python3 progresso.py reabrir 08_functions/ex01_padronizar_produtos.py
```

O script atualiza `README.md` e `PROGRESSO.md`. Ele não executa a solução,
não atribui nota nem cria commits. No fluxo com a IA, o histórico de revisão
é atualizado separadamente, seguindo as orientações da mentoria.

Os commits usam inglês e descrevem a ação implementada, como
`feat(variables): calculate sales bonuses and remaining revenue`.
Quando um arquivo contém apenas o enunciado, o commit informa essa adição.
Posso estudar e resolver em português; após a aprovação e a autorização para
publicar, a tradução para inglês é feita e conferida antes do commit. Ela
preserva a lógica e mantém os exercícios pendentes em português.

## Adding exercises

Vou expandir este repositório com novos problemas conforme aprender outros
conceitos. Para adicionar um exercício, crie um arquivo `.py` na pasta do assunto,
escreva o enunciado nos comentários e acrescente um item ao checklist na seção
correspondente. Se for um novo assunto, crie também uma pasta numerada e uma
seção com título `##` no checklist.

Depois de adicionar o item, execute `python3 progresso.py` para atualizar os
totais. O script lê os exercícios desse checklist e verifica se os arquivos
indicados existem. A próxima etapa de estudos continua sendo o primeiro
exercício pendente na ordem do checklist.

## Variables

- [x] [01 — Bônus de vendas](01_variables/ex01_bonus_vendas.py)
- [x] [02 — Controle de estoque](01_variables/ex02_controle_estoque.py)
- [x] [03 — Divisão de cargas](01_variables/ex03_divisao_cargas.py)
- [x] [04 — Margem de lucro](01_variables/ex04_margem_lucro.py)
- [x] [05 — Tempo de contrato](01_variables/ex05_tempo_contrato.py)

## Strings

- [x] [01 — Relatório de lucro](02_strings/ex01_relatorio_lucro.py)
- [x] [02 — Padronização de cadastro](02_strings/ex02_padronizar_cadastro.py)
- [x] [03 — Troca de domínio](02_strings/ex03_trocar_dominio.py)
- [x] [04 — Extração de usuário](02_strings/ex04_extrair_usuario.py)
- [x] [05 — Saudação ao cliente](02_strings/ex05_saudacao_cliente.py)

## User input

- [x] [01 — Imposto sobre vendas](03_inputs/ex01_imposto_vendas.py)
- [x] [02 — Cadastro de colaborador](03_inputs/ex02_cadastro_colaborador.py)
- [x] [03 — Faturamento das lojas](03_inputs/ex03_faturamento_lojas.py)

## Lists

- [x] [01 — Relatório de vendas](04_lists/ex01_relatorio_vendas.py)
- [x] [02 — Edição de estoque](04_lists/ex02_editar_estoque.py)
- [x] [03 — Ordenação de fretes](04_lists/ex03_ordenar_fretes.py)
- [x] [04 — Rota de entregas](04_lists/ex04_rota_entregas.py)
- [x] [05 — Atualização de preços](04_lists/ex05_atualizar_precos.py)

## Conditionals

- [x] [01 — Perfil de investimento](05_conditionals/ex01_perfil_investimento.py)
- [x] [02 — Acesso ao sistema](05_conditionals/ex02_acesso_sistema.py)
- [x] [03 — Desconto progressivo](05_conditionals/ex03_desconto_progressivo.py)
- [x] [04 — Bônus por metas](05_conditionals/ex04_bonus_metas.py)
- [x] [05 — Triagem de e-mails](05_conditionals/ex05_triagem_emails.py)

## Dictionaries

- [x] [01 — Atualização de clientes](06_dictionaries/ex01_atualizar_clientes.py)
- [x] [02 — Consulta de estoque](06_dictionaries/ex02_consultar_estoque.py)
- [x] [03 — Faturamento por região](06_dictionaries/ex03_faturamento_regioes.py)
- [x] [04 — Média de desempenho](06_dictionaries/ex04_media_desempenho.py)
- [x] [05 — Remoção de produto](06_dictionaries/ex05_remover_produto.py)

## For loops

- [x] [01 — Lembretes de treinamento](07_for_loops/ex01_lembretes_treinamento.py)
- [x] [02 — Comissão de vendas](07_for_loops/ex02_comissao_vendas.py)
- [x] [03 — Estoque crítico](07_for_loops/ex03_estoque_critico.py)
- [x] [04 — Custos mensais](07_for_loops/ex04_custos_mensais.py)
- [x] [05 — Reajuste de preços](07_for_loops/ex05_reajustar_precos.py)

## Functions

- [x] [01 — Padronização de produtos](08_functions/ex01_padronizar_produtos.py)
- [x] [02 — Cálculo de ISS](08_functions/ex02_calcular_iss.py)
- [x] [03 — Análise de margem](08_functions/ex03_analisar_margem.py)
- [x] [04 — Verificação de metas](08_functions/ex04_verificar_metas.py)
- [x] [05 — Conversão de moeda](08_functions/ex05_converter_moeda.py)

## Tuples

- [x] [01 — Coordenadas de entrega](09_tuples/ex01_coordenadas_entrega.py)
- [ ] [02 — Folha de pagamento](09_tuples/ex02_folha_pagamento.py)
- [ ] [03 — Vendas por produto](09_tuples/ex03_vendas_produtos.py)
- [ ] [04 — Vendas por filial](09_tuples/ex04_vendas_filiais.py)
- [ ] [05 — Resumo de chamados](09_tuples/ex05_resumo_chamados.py)
