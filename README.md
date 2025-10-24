# Teste Lógico 2025 — Soluções em Python

Este repositório contém soluções **claras, testadas e bem documentadas** para as quatro questões do teste.
As instruções abaixo permitem executar tudo de ponta a ponta, sem dependências externas além do Python.

## Requisitos
- Python 3.10+
- (Opcional) `venv` para ambiente isolado
- `pytest` para rodar os testes

## Como rodar

```bash
# 1) Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
# source .venv/bin/activate

# 2) Instale o pytest
pip install pytest

# 3) Rode os testes automatizados
pytest

# 4) Execute o script demonstrativo (permite testar no terminal)
python scripts/run_all.py
```

## Estrutura do projeto
```
teste-logico-2025/
├─ pyproject.toml
├─ README.md
├─ uso_de_ia.md
├─ src/
│  └─ perguntas/
│     ├─ __init__.py
│     ├─ estruturas.py
│     ├─ pergunta1.py  # "1" à esquerda (estável)
│     ├─ pergunta2.py  # Busca em árvore binária de palavras (retorna caminho)
│     ├─ pergunta3.py  # Two-sum (combinação soma = X)
│     └─ pergunta4.py  # Completar intervalo 0..n no próprio array
├─ tests/
│  ├─ test_pergunta1.py
│  ├─ test_pergunta2.py
│  ├─ test_pergunta3.py
│  └─ test_pergunta4.py
└─ scripts/
   └─ run_all.py
```

## Estratégias (resumo)
- **Q1**: *stable-partition* em lugar, mantendo a ordem dos não-1. Implementado por fatiamento (atribuição por `[:]`).
- **Q2**: Busca em árvore binária **DFS** (pré-ordem) que retorna o **caminho** (`A -> B -> ...`) até o alvo.
- **Q3**: *Two-sum* em **O(n)** via `set` de complementos.
- **Q4**: Reconstrói o intervalo **0..n** onde `n = max(array)`, inserindo faltantes e **preservando ordenação** final crescente.

## Como validar manualmente
Use `scripts/run_all.py` para ver exemplos em execução (entrada/saída) e validar rapidamente os resultados.

## Transparência sobre IA
Veja `uso_de_ia.md` descrevendo como a IA foi empregada, com senso crítico e validações.


