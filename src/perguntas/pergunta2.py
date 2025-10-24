from typing import Optional, List
from .estruturas import Node, dfs_path

def caminho_ate_palavra(root: Node, palavra: str) -> Optional[str]:
    
    path: Optional[List[str]] = dfs_path(root, palavra)
    return " -> ".join(path) if path else None


def montar_arvore_exemplo() -> Node:
   
    raiz = Node("Maçã")
    # Subárvore esquerda
    morango = raiz.insert_left("Morango")
    morango.insert_left("Goiaba")
    morango.insert_right("Limão")
    # Subárvore direita
    pera = raiz.insert_right("Pera")
    abacaxi = pera.insert_left("Abacaxi")
    laranja = pera.insert_right("Laranja")
    laranja.insert_left("Banana")
    laranja.insert_right("Cebola")
    return raiz


if __name__ == "__main__":
    root = montar_arvore_exemplo()
    for alvo in ("Goiaba", "Cebola", "Abacaxi", "Maçã", "Inexistente"):
        print(alvo, "=>", caminho_ate_palavra(root, alvo))
