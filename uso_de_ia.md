# uso_de_ia.md — Transparência sobre o uso de IA

**Ferramenta**: ChatGPT (modelo GPT-5 Thinking).  
**Objetivo**: Acelerar brainstorming, estruturar projeto, sugerir testes e conferir bordas.

## Como as sugestões foram aplicadas ou descartadas
1. **Arquitetura do projeto**: aceitei a sugestão de organizar `src/`, `tests/` e `scripts/` para facilitar execução e avaliação.
2. **Q1 (stable-partition)**: aceitei a ideia de usar atribuição por fatiamento (`lst[:] = ...`) para manter *in-place*.
3. **Q2 (árvore binária)**: aceitei DFS pré-ordem retornando caminho; descartei BFS por simplicidade e porque não altera a complexidade para este caso.
4. **Q3 (two-sum)**: aceitei uso de `set` de complementos em O(n); adicionei testes com números repetidos.
5. **Q4 (intervalo 0..n)**: aceitei reconstruir o intervalo ordenado e reatribuir no próprio array; incluí validação para lista vazia.
6. **Testes**: aceitei criar suíte `pytest` para garantir robustez e evitar regressões.
7. **Documentação**: aceitei incluir README detalhado com passos e exemplos.

## Validação humana
- Revisei cada solução comparando com o enunciado, rodei os testes e validei exemplos práticos.
- Chequei casos de borda (listas vazias, números repetidos, busca inexistente na árvore, etc.).

## Prompts (resumo)
- “Gerar estrutura de projeto em Python com testes e CLI para resolver Q1..Q4 do teste lógico.”
- “Implementar DFS que retorne caminho em string ‘A -> B -> C’.”
- “Criar testes para cobrir cenários de borda.”

## Responsabilidade
- Conferi manualmente as respostas; o uso de IA **não substituiu** a checagem técnica nem o bom-senso na implementação.
