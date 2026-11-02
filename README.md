# Python Mentor

Português | [English](README.en.md)

O Python Mentor é um projeto para aprender Python do zero com exercícios e
mentoria de IA. A proposta é desenvolver a lógica de programação e uma base
na linguagem antes de estudar Django como primeiro framework web em Python.

Os exercícios trabalham situações como calcular comissões, atualizar estoques
e organizar dados de clientes. Esta branch contém apenas os enunciados e espaço
para suas tentativas. Vou acrescentar novos exercícios conforme meus estudos avançarem.

## Learning path

Os assuntos seguem esta ordem:

| Pasta | O que praticar |
| --- | --- |
| [01_variables](exercises/pt/01_variables/) | Variáveis, operações aritméticas, porcentagens e comparações |
| [02_strings](exercises/pt/02_strings/) | Formatação, métodos de texto e fatiamento |
| [03_inputs](exercises/pt/03_inputs/) | Entrada de dados e conversão de tipos |
| [04_lists](exercises/pt/04_lists/) | Índices, alterações, ordenação e cálculos com listas |
| [05_conditionals](exercises/pt/05_conditionals/) | Decisões com `if`, `elif`, `else` e operadores lógicos |
| [06_dictionaries](exercises/pt/06_dictionaries/) | Chaves, valores, consultas e atualização de dados |
| [07_for_loops](exercises/pt/07_for_loops/) | Repetições, filtros e acumuladores |
| [08_functions](exercises/pt/08_functions/) | Parâmetros, retorno e reutilização de código |
| [09_tuples](exercises/pt/09_tuples/) | Tuplas, desempacotamento e retornos com múltiplos valores |

Os nomes das pastas e os títulos das seções estão em inglês. Em `exercises/pt/`,
os enunciados e nomes dos arquivos estão em português. Em `exercises/en/`,
eles estão em inglês. Todos os arquivos começam sem solução.

## Choosing a branch

| Branch | Conteúdo |
| --- | --- |
| `main` | Exercícios para começar do zero em português e inglês, sem soluções |
| `my-practice` | Minhas soluções em português e meu progresso pessoal |

Esta é a versão para começar do zero. Escolha um idioma:

- [Português](exercises/pt/): 43 enunciados, com checklist neste README.
- [English](README.en.md): 43 enunciados em `exercises/en/`, com guia e checklist em inglês.

Os exercícios correspondentes praticam os mesmos conceitos. Cada idioma tem seu
próprio progresso; basta estudar na versão que preferir. Os enunciados em inglês
traduzem as instruções, os nomes das funções e as mensagens solicitadas. Nomes
próprios e alguns dados de exemplo foram preservados e explicados quando necessário.

O clone abaixo baixa apenas o estado atual da `main`, sem o histórico com
respostas. Você também pode baixar o ZIP da `main` pelo GitHub. As respostas
pessoais continuam públicas na
[branch my-practice](https://github.com/joaogabrielcode/python-mentor/tree/my-practice).

Para publicar sua própria evolução, faça um fork e use seu endereço no clone.
Depois de clonar, crie uma branch de estudo antes de resolver os exercícios:

```sh
git switch -c my-study
```

## Getting started

Você precisa de Python 3, Git para clonar o repositório, um editor de texto ou
código e um terminal.
Os exercícios atuais usam recursos da própria linguagem, sem bibliotecas
externas para instalar.

Clone o repositório e entre na pasta:

```sh
git clone --depth 1 --single-branch --branch main https://github.com/joaogabrielcode/python-mentor.git
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
dados necessários. Escreva sua tentativa na área indicada por `# Sua solução:`.
Os arquivos iniciais contêm apenas comentários. Antes de escrever uma solução,
executá-los não imprime nenhum resultado. Depois de escrever sua tentativa,
execute o arquivo a partir da raiz do projeto:

```sh
python3 exercises/pt/01_variables/ex01_bonus_vendas.py
```

Nos exercícios com `input`, o programa espera que você digite os dados no
terminal. Para praticar entrada de valores, por exemplo:

```sh
python3 exercises/pt/03_inputs/ex03_faturamento_lojas.py
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
Quero estudar a versão portuguesa em exercises/pt/.
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
Terminei exercises/pt/01_variables/ex01_bonus_vendas.py.
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

O checklist no final deste README acompanha somente os exercícios em português.
O [README em inglês](README.en.md) tem seu próprio checklist. Ambos começam
em 0/43, sem revisões anteriores. Resolva e salve suas tentativas na sua branch
de estudo.

Para sincronizar os totais, sem concluir outro exercício:

```sh
python3 progresso.py
```

Depois de revisar e aprovar uma solução, registre sua conclusão. Exemplo para
o exercício de bônus de vendas, somente quando ele estiver aprovado:

```sh
python3 progresso.py concluir exercises/pt/01_variables/ex01_bonus_vendas.py
```

Para voltar esse exercício a pendente:

```sh
python3 progresso.py reabrir exercises/pt/01_variables/ex01_bonus_vendas.py
```

O script atualiza `README.md` e `PROGRESSO.md`. Ele não executa a solução,
não atribui nota nem cria commits. No fluxo com a IA, o histórico de revisão
é atualizado separadamente, seguindo as orientações da mentoria.

Os commits usam inglês e descrevem a ação implementada, como
`feat(variables): calculate sales bonuses and remaining revenue`.
Quando um arquivo contém apenas o enunciado, o commit informa essa adição.

Para estudar em inglês, use o [guia em inglês](README.en.md). Os comandos
aceitam `--language en`, e os registros ficam em `PROGRESS.en.md` e
`MENTORING.en.md`, sem alterar o progresso em português.

## Adding exercises

Vou expandir este repositório com novos problemas conforme aprender outros
conceitos. Para adicionar um exercício, crie os arquivos `.py` correspondentes em
`exercises/pt/` e `exercises/en/`, escreva os enunciados nos comentários e
acrescente cada item à seção correspondente do README do idioma. Se for um novo assunto, crie também uma pasta numerada e uma
seção com título `##` no checklist.

Depois de adicionar o item, execute `python3 progresso.py` e `python3 progresso.py --language en`
para atualizar os totais de cada idioma. O script lê os exercícios desse checklist e verifica se os arquivos
indicados existem. A próxima etapa de estudos continua sendo o primeiro
exercício pendente na ordem do checklist.


## Variables

- [ ] [01 — Bônus de vendas](exercises/pt/01_variables/ex01_bonus_vendas.py)
- [ ] [02 — Controle de estoque](exercises/pt/01_variables/ex02_controle_estoque.py)
- [ ] [03 — Divisão de cargas](exercises/pt/01_variables/ex03_divisao_cargas.py)
- [ ] [04 — Margem de lucro](exercises/pt/01_variables/ex04_margem_lucro.py)
- [ ] [05 — Tempo de contrato](exercises/pt/01_variables/ex05_tempo_contrato.py)

## Strings

- [ ] [01 — Relatório de lucro](exercises/pt/02_strings/ex01_relatorio_lucro.py)
- [ ] [02 — Padronização de cadastro](exercises/pt/02_strings/ex02_padronizar_cadastro.py)
- [ ] [03 — Troca de domínio](exercises/pt/02_strings/ex03_trocar_dominio.py)
- [ ] [04 — Extração de usuário](exercises/pt/02_strings/ex04_extrair_usuario.py)
- [ ] [05 — Saudação ao cliente](exercises/pt/02_strings/ex05_saudacao_cliente.py)

## User input

- [ ] [01 — Imposto sobre vendas](exercises/pt/03_inputs/ex01_imposto_vendas.py)
- [ ] [02 — Cadastro de colaborador](exercises/pt/03_inputs/ex02_cadastro_colaborador.py)
- [ ] [03 — Faturamento das lojas](exercises/pt/03_inputs/ex03_faturamento_lojas.py)

## Lists

- [ ] [01 — Relatório de vendas](exercises/pt/04_lists/ex01_relatorio_vendas.py)
- [ ] [02 — Edição de estoque](exercises/pt/04_lists/ex02_editar_estoque.py)
- [ ] [03 — Ordenação de fretes](exercises/pt/04_lists/ex03_ordenar_fretes.py)
- [ ] [04 — Rota de entregas](exercises/pt/04_lists/ex04_rota_entregas.py)
- [ ] [05 — Atualização de preços](exercises/pt/04_lists/ex05_atualizar_precos.py)

## Conditionals

- [ ] [01 — Perfil de investimento](exercises/pt/05_conditionals/ex01_perfil_investimento.py)
- [ ] [02 — Acesso ao sistema](exercises/pt/05_conditionals/ex02_acesso_sistema.py)
- [ ] [03 — Desconto progressivo](exercises/pt/05_conditionals/ex03_desconto_progressivo.py)
- [ ] [04 — Bônus por metas](exercises/pt/05_conditionals/ex04_bonus_metas.py)
- [ ] [05 — Triagem de e-mails](exercises/pt/05_conditionals/ex05_triagem_emails.py)

## Dictionaries

- [ ] [01 — Atualização de clientes](exercises/pt/06_dictionaries/ex01_atualizar_clientes.py)
- [ ] [02 — Consulta de estoque](exercises/pt/06_dictionaries/ex02_consultar_estoque.py)
- [ ] [03 — Faturamento por região](exercises/pt/06_dictionaries/ex03_faturamento_regioes.py)
- [ ] [04 — Média de desempenho](exercises/pt/06_dictionaries/ex04_media_desempenho.py)
- [ ] [05 — Remoção de produto](exercises/pt/06_dictionaries/ex05_remover_produto.py)

## For loops

- [ ] [01 — Lembretes de treinamento](exercises/pt/07_for_loops/ex01_lembretes_treinamento.py)
- [ ] [02 — Comissão de vendas](exercises/pt/07_for_loops/ex02_comissao_vendas.py)
- [ ] [03 — Estoque crítico](exercises/pt/07_for_loops/ex03_estoque_critico.py)
- [ ] [04 — Custos mensais](exercises/pt/07_for_loops/ex04_custos_mensais.py)
- [ ] [05 — Reajuste de preços](exercises/pt/07_for_loops/ex05_reajustar_precos.py)

## Functions

- [ ] [01 — Padronização de produtos](exercises/pt/08_functions/ex01_padronizar_produtos.py)
- [ ] [02 — Cálculo de ISS](exercises/pt/08_functions/ex02_calcular_iss.py)
- [ ] [03 — Análise de margem](exercises/pt/08_functions/ex03_analisar_margem.py)
- [ ] [04 — Verificação de metas](exercises/pt/08_functions/ex04_verificar_metas.py)
- [ ] [05 — Conversão de moeda](exercises/pt/08_functions/ex05_converter_moeda.py)

## Tuples

- [ ] [01 — Coordenadas de entrega](exercises/pt/09_tuples/ex01_coordenadas_entrega.py)
- [ ] [02 — Folha de pagamento](exercises/pt/09_tuples/ex02_folha_pagamento.py)
- [ ] [03 — Vendas por produto](exercises/pt/09_tuples/ex03_vendas_produtos.py)
- [ ] [04 — Vendas por filial](exercises/pt/09_tuples/ex04_vendas_filiais.py)
- [ ] [05 — Resumo de chamados](exercises/pt/09_tuples/ex05_resumo_chamados.py)
