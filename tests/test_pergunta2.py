from perguntas.pergunta2 import montar_arvore_exemplo, caminho_ate_palavra

def test_q2_caminhos_basicos():
    root = montar_arvore_exemplo()
    assert caminho_ate_palavra(root, "Maçã") == "Maçã"
    assert caminho_ate_palavra(root, "Goiaba") == "Maçã -> Morango -> Goiaba"
    assert caminho_ate_palavra(root, "Cebola") == "Maçã -> Pera -> Laranja -> Cebola"
    assert caminho_ate_palavra(root, "Inexistente") is None
