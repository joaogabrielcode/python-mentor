"""Registra a conclusão dos exercícios em Markdown, sem executar soluções."""

import argparse
from pathlib import Path
import re


RAIZ = Path(__file__).resolve().parent
ARQUIVO = RAIZ / "PROGRESSO.md"
README = RAIZ / "README.md"
ITEM = re.compile(r"^- \[([ xX])\] \[(.+?)\]\(([^)]+)\)$", re.MULTILINE)


def listar_exercicios():
    grupos = {}
    assunto = None
    for linha in README.read_text(encoding="utf-8").splitlines():
        if linha.startswith("## "):
            assunto = linha[3:]
        elif correspondencia := ITEM.fullmatch(linha):
            _, titulo, caminho = correspondencia.groups()
            if assunto is None or not (RAIZ / caminho).is_file():
                raise ValueError(f"Exercício inválido no README: {caminho}")
            grupos.setdefault(assunto, []).append((titulo, caminho))
    if not grupos:
        raise ValueError("Nenhum exercício encontrado no README.")
    return grupos


def ler_concluidos():
    origem = ARQUIVO if ARQUIVO.exists() else README
    return {
        caminho
        for marca, _, caminho in ITEM.findall(origem.read_text(encoding="utf-8"))
        if marca.lower() == "x"
    }


def salvar(grupos, concluidos):
    total = sum(len(itens) for itens in grupos.values())
    quantidade = len(concluidos)
    resumo = f"{quantidade}/{total} exercícios concluídos ({quantidade / total:.1%})."
    proximo = next(
        ((titulo, caminho) for itens in grupos.values() for titulo, caminho in itens
         if caminho not in concluidos),
        None,
    )
    atual = (
        f"Exercício atual: [{proximo[0]}]({proximo[1]})."
        if proximo else "Todos os exercícios foram concluídos."
    )
    linhas = [
        "# Progresso dos exercícios",
        "",
        resumo,
        "",
        atual,
        "",
        "Ao terminar e conferir sua solução, registre a conclusão:",
        "",
        "```sh",
        "python3 progresso.py concluir 01_variables/ex03_divisao_cargas.py",
        "```",
        "",
        "Para voltar um exercício a pendente, use `reabrir` no lugar de `concluir`.",
        "Use `python3 progresso.py` para atualizar os totais após editar o checklist",
        "manualmente. Os comandos também aceitam `python` no lugar de `python3`.",
        "O registro é manual e não verifica se a solução está correta.",
        "",
        "| Assunto | Concluídos | Progresso |",
        "| --- | --- | --- |",
    ]
    for assunto, itens in grupos.items():
        feitos = sum(caminho in concluidos for _, caminho in itens)
        linhas.append(f"| {assunto} | {feitos}/{len(itens)} | {feitos / len(itens):.0%} |")
    for assunto, itens in grupos.items():
        linhas.extend(["", f"## {assunto}", ""])
        for titulo, caminho in itens:
            marca = "x" if caminho in concluidos else " "
            linhas.append(f"- [{marca}] [{titulo}]({caminho})")
    ARQUIVO.write_text("\n".join(linhas) + "\n", encoding="utf-8")

    def sincronizar(correspondencia):
        _, titulo, caminho = correspondencia.groups()
        marca = "x" if caminho in concluidos else " "
        return f"- [{marca}] [{titulo}]({caminho})"

    atual = README.read_text(encoding="utf-8")
    atualizado = ITEM.sub(sincronizar, atual)
    if atualizado != atual:
        README.write_text(atualizado, encoding="utf-8")
    return resumo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("acao", nargs="?", default="status", choices=["status", "concluir", "reabrir"])
    parser.add_argument("exercicio", nargs="?", help="Caminho do arquivo .py do exercício")
    args = parser.parse_args()
    if args.acao != "status" and not args.exercicio:
        parser.error("Informe o caminho do exercício para concluir ou reabrir.")
    if args.acao == "status" and args.exercicio:
        parser.error("A ação status não recebe um exercício.")
    try:
        grupos = listar_exercicios()
        caminhos = {caminho for itens in grupos.values() for _, caminho in itens}
        concluidos = ler_concluidos() & caminhos
        if args.exercicio:
            alvo = Path(args.exercicio)
            if not alvo.is_absolute():
                alvo = RAIZ / alvo
            try:
                caminho = alvo.resolve().relative_to(RAIZ).as_posix()
            except ValueError:
                parser.error("O exercício deve pertencer a este projeto.")
            if caminho not in caminhos:
                parser.error("Exercício não encontrado no checklist do projeto.")
            if args.acao == "concluir":
                concluidos.add(caminho)
            else:
                concluidos.discard(caminho)
        print(salvar(grupos, concluidos))
    except (OSError, ValueError) as erro:
        parser.exit(1, f"Não foi possível atualizar o progresso: {erro}\n")


if __name__ == "__main__":
    main()
